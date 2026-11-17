#!/usr/bin/env python3
"""Check the four academic-video-scriptwriter output files for consistency.

Usage:
    python3 check_outputs.py OUTPUT_DIR [--wpm N] [--phrases FILE]

OUTPUT_DIR must contain teaching-plan.md, script.md, storyboard.md, and
evidence-and-review.md in the format described in references/output-format.md.

Two tiers:
    FAIL  a rule the skill treats as blocking (untraced number, missing topic role,
          banned phrase, digit in narration, broken ID reference). Exit code 1.
    WARN  something a person should look at (unverified claim, long sentence,
          acronym without pronunciation, scene that may be too short for its narration).

Standard library only. The checker reads files and prints a report; it changes nothing.
It cannot tell whether a claim is true or a transition is good. Those need a reviewer.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

FILES = ("teaching-plan.md", "script.md", "storyboard.md", "evidence-and-review.md")
ROLES = {"goal", "hook", "puzzle", "roadmap", "announce", "introduce", "explain", "predict", "reveal",
         "unknown", "wrap-up", "bridge", "synthesis"}
MIN_THINK = 2.0  # seconds of pause a [predict] line must give the viewer
TOPIC_ROLES = ("announce", "introduce", "explain", "wrap-up", "bridge")
RESERVED_TOPICS = ("opening", "conclusion")
FOCUS_VALUES = {"figure", "cursor", "figure + cursor"}
MOTION_VERBS = {
    "build", "reveal", "highlight", "dim", "split", "merge", "transform", "compare",
    "zoom in", "pull back", "trace", "rotate", "hold", "cut", "draw", "fade", "move",
}
STATUSES = {"verified", "unverified", "gap"}
PAUSE_SECONDS = {"beat": 0.75, "break": 1.5}
NUMBER_WORDS = {
    "zero", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
    "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
    "eighty", "ninety", "hundred", "hundreds", "thousand", "thousands", "million",
    "millions", "billion", "percent", "percentage", "half", "halves", "third", "thirds",
    "quarter", "quarters", "double", "twice", "triple", "tripled", "doubled", "minus",
}
SYMBOLS = set("%<>=±/&+×^~$#@|\\")
LONG_SENTENCE = 28

MARK_RE = re.compile(r"\{([^}]*)\}")
SEGMENT_RE = re.compile(r"^\[(S\d+)\]\s*\[([a-z+\-]+)\]\s*(.*)$")
SCRIPT_HEAD_RE = re.compile(r"^##\s+(Opening|Conclusion|T\d+)\b\s*(?:[·:\-—]\s*(.*))?$")
BLOCK_HEAD_RE = re.compile(r"^###\s+([SF]\d+)\s*(?:·\s*(.*))?$")
FIELD_RE = re.compile(r"^-\s+([A-Za-z][A-Za-z ]*?):\s*(.*)$")
NUM_RE = re.compile(r"(?<![\w.])[-−]?\d+(?:,\d{3})*(?:\.\d+)?(?:[eE][-−]?\d+)?")
ID_RE = re.compile(r"\b([OTSFCD]\d+)\b")


@dataclass
class Report:
    fails: list = field(default_factory=list)
    warns: list = field(default_factory=list)
    notes: list = field(default_factory=list)

    def fail(self, where, msg):
        self.fails.append(f"{where}: {msg}")

    def warn(self, where, msg):
        self.warns.append(f"{where}: {msg}")


# ---------------------------------------------------------------- parsing helpers

def sections(lines):
    """Map '## Heading' text -> list of (lineno, line) under it (until next ## heading)."""
    out, current = {}, None
    for i, line in enumerate(lines, 1):
        if line.startswith("## "):
            current = line[3:].strip()
            out[current] = []
        elif current is not None:
            out[current].append((i, line))
    return out


def find_section(secs, name):
    for key, body in secs.items():
        if key.lower().startswith(name.lower()):
            return body
    return None


def table(body):
    """Parse the first markdown table in a section body -> list of (lineno, {header: cell})."""
    rows, headers = [], None
    for lineno, line in body or []:
        s = line.strip()
        if not s.startswith("|"):
            if headers and rows:
                break
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if headers is None:
            headers = [h.lower() for h in cells]
        elif all(set(c) <= set("-: ") for c in cells):
            continue
        else:
            rows.append((lineno, dict(zip(headers, cells))))
    return rows


def col(row, *names):
    for n in names:
        for k, v in row.items():
            if k.startswith(n):
                return v
    return ""


def parse_seconds(text):
    if not text:
        return None
    t = text.strip().lower()
    m = re.match(r"^(\d+):(\d{1,2})", t)
    if m:
        return int(m.group(1)) * 60 + int(m.group(2))
    m = re.match(r"^~?\s*(\d+(?:\.\d+)?)\s*(m|min|minutes?)\b", t)
    if m:
        return float(m.group(1)) * 60
    m = re.match(r"^~?\s*(\d+(?:\.\d+)?)\s*(s|sec|seconds?)?\b", t)
    if m:
        return float(m.group(1))
    return None


def norm_num(s):
    return s.replace("−", "-").replace(",", "").lstrip("+").lower()


def numbers_in(text):
    return {norm_num(m) for m in NUM_RE.findall(text)}


def spoken(text):
    return re.sub(r"\s+", " ", MARK_RE.sub(" ", text).replace("*", "")).strip()


def norm_words(text):
    return re.sub(r"[^a-z0-9 ]+", " ", text.lower().replace("’", "'").replace("'", "")).split()


def contains_phrase(text, phrase):
    t, p = norm_words(text), norm_words(phrase)
    return any(t[i:i + len(p)] == p for i in range(len(t) - len(p) + 1)) if p else False


def load_phrases(path):
    if not path.exists():
        return []
    return [l.strip() for l in path.read_text(encoding="utf-8").splitlines()
            if l.strip() and not l.lstrip().startswith("#")]


# ---------------------------------------------------------------- the checks

def check(out_dir: Path, wpm_override=None, phrases_path=None) -> Report:
    rep = Report()
    text = {}
    for name in FILES:
        p = out_dir / name
        if not p.exists():
            rep.fail(name, "file missing")
        else:
            text[name] = p.read_text(encoding="utf-8").splitlines()
    if rep.fails:
        return rep

    # ---- teaching plan
    plan = sections(text["teaching-plan.md"])
    brief = {}
    for _, line in find_section(plan, "Brief") or []:
        m = FIELD_RE.match(line.strip())
        if m:
            brief[m.group(1).strip().lower()] = m.group(2).strip()
    target = parse_seconds(brief.get("target duration", ""))
    wpm = wpm_override
    if wpm is None:
        m = re.search(r"(\d+)", brief.get("speech rate", ""))
        wpm = int(m.group(1)) if m else 150
    if target is None:
        rep.warn("teaching-plan.md", "no parseable 'Target duration' in Brief")

    topics = {}  # id -> title, in order
    for lineno, row in table(find_section(plan, "Topics")):
        tid = col(row, "id")
        if re.fullmatch(r"T\d+", tid):
            topics[tid] = col(row, "title")
    if not topics:
        rep.fail("teaching-plan.md", "no topics found in '## Topics' table")
    topic_order = list(topics)

    covered = set()
    for lineno, row in table(find_section(plan, "Objectives")):
        oid, t = col(row, "id"), col(row, "topic")
        for tid in re.findall(r"T\d+", t):
            if tid not in topics:
                rep.fail(f"teaching-plan.md:{lineno}", f"objective {oid} points to unknown topic {tid}")
            covered.add(tid)
    for tid in topics:
        if tid not in covered:
            rep.warn("teaching-plan.md", f"topic {tid} has no learning objective")

    pron_terms = {col(r, "term") for _, r in table(find_section(plan, "Pronunciation"))}

    # ---- evidence
    ev = sections(text["evidence-and-review.md"])
    data_ids = {col(r, "id") for _, r in table(find_section(ev, "Data sources"))}
    if not data_ids:
        rep.warn("evidence-and-review.md", "no data sources listed")
    claims = {}
    for lineno, row in table(find_section(ev, "Claims")):
        cid = col(row, "id")
        if not re.fullmatch(r"C\d+", cid):
            continue
        src, status = col(row, "source"), col(row, "status").lower()
        claims[cid] = {"values": col(row, "values"), "status": status, "line": lineno}
        where = f"evidence-and-review.md:{lineno}"
        srcs = re.findall(r"D\d+", src)
        if not srcs and status != "gap":
            rep.fail(where, f"claim {cid} has no data source (a D ID)")
        for d in srcs:
            if d not in data_ids:
                rep.fail(where, f"claim {cid} cites unknown data source {d}")
        if status not in STATUSES:
            rep.fail(where, f"claim {cid} status '{status}' is not verified / unverified / gap")
        elif status == "unverified":
            rep.warn(where, f"claim {cid} is unverified; confirm it against {src} before production")
        if not col(row, "location"):
            rep.warn(where, f"claim {cid} has no location inside its source")

    used_claims = set()

    def use_claim(cid, where, roles=()):
        used_claims.add(cid)
        if cid not in claims:
            rep.fail(where, f"claim {cid} is not in the Claims table")
        elif claims[cid]["status"] == "gap" and "unknown" not in roles:
            rep.fail(where, f"claim {cid} is a gap (no supporting data); it may be spoken only in an [unknown] line")

    # ---- script
    phrases = load_phrases(phrases_path)
    cur = None
    seen_topics, script_scene_topic, scene_words, scene_pause = [], {}, {}, {}
    roles_by_section = {}
    lines_by_section = {}
    pending_predicts = {}  # section -> [lineno, ...] awaiting a [reveal]
    predict_scenes = set()
    for i, line in enumerate(text["script.md"], 1):
        s = line.strip()
        where = f"script.md:{i}"
        h = SCRIPT_HEAD_RE.match(s)
        if h:
            cur = h.group(1).lower() if h.group(1) in ("Opening", "Conclusion") else h.group(1)
            seen_topics.append(cur)
            roles_by_section.setdefault(cur, set())
            lines_by_section.setdefault(cur, [])
            if cur not in RESERVED_TOPICS and cur not in topics:
                rep.fail(where, f"section {cur} is not a topic in the teaching plan")
            continue
        if not s or s.startswith(("#", ">", "<!--")):
            continue
        m = SEGMENT_RE.match(s)
        if not m:
            if cur is not None:
                rep.warn(where, "line is not a [S..] [role] segment; it will not be narrated")
            continue
        if cur is None:
            rep.fail(where, "segment appears before the first section heading")
            continue
        sid, roles, body = m.group(1), m.group(2).split("+"), m.group(3)
        for r in roles:
            if r not in ROLES:
                rep.fail(where, f"unknown role '{r}'")
            roles_by_section[cur].add(r)
        prev = script_scene_topic.get(sid)
        if prev and prev != cur:
            rep.fail(where, f"scene {sid} carries lines from two topics ({prev}, {cur}); split the scene")
        script_scene_topic[sid] = cur

        line_claims = []
        pause = 0.0
        for mark in MARK_RE.findall(body):
            mark = mark.strip()
            if re.fullmatch(r"C\d+", mark):
                line_claims.append(mark)
                use_claim(mark, where, roles)
            elif mark in PAUSE_SECONDS:
                pause += PAUSE_SECONDS[mark]
            elif re.fullmatch(r"look:\s*\d+(\.\d+)?", mark):
                pause += float(mark.split(":")[1])
            else:
                rep.fail(where, f"unknown mark {{{mark}}}")
        say = spoken(body)
        lines_by_section[cur].append((i, roles, say))
        if "predict" in roles and "reveal" in roles:
            rep.fail(where, "a prediction and its reveal cannot share a line; give the viewer time")
        elif "predict" in roles:
            pending_predicts.setdefault(cur, []).append(i)
            predict_scenes.add(sid)
            if pause < MIN_THINK:
                rep.fail(where, f"[predict] gives {pause:.1f}s to think; add {{look:3}} or longer")
            if "?" not in say:
                rep.warn(where, "[predict] line asks no question")
        elif "reveal" in roles and pending_predicts.get(cur):
            pending_predicts[cur].pop(0)
        if "unknown" in roles and not any(claims.get(c, {}).get("status") == "gap" for c in line_claims):
            rep.warn(where, "[unknown] line should cite the gap claim it refers to")
        scene_words[sid] = scene_words.get(sid, 0) + len(say.split())
        scene_pause[sid] = scene_pause.get(sid, 0.0) + pause

        if re.search(r"\d", say):
            rep.fail(where, "digit in narration; spell it as it should be spoken")
        bad = sorted({c for c in say if c in SYMBOLS})
        if bad:
            rep.fail(where, f"symbol(s) {' '.join(bad)} in narration; write them as words")
        if "(" in say or ")" in say:
            rep.warn(where, "parentheses in narration; TTS reads them flatly, rewrite as a sentence")
        for ph in phrases:
            if contains_phrase(say, ph):
                rep.fail(where, f"banned phrase '{ph}'")
        for ac in sorted(set(re.findall(r"\b[A-Z]{2,}s?\b", say))):
            if ac not in pron_terms and ac.rstrip("s") not in pron_terms:
                rep.warn(where, f"'{ac}' is not in the Pronunciation table")
        for sent in re.split(r"(?<=[.!?])\s+", say):
            if len(sent.split()) > LONG_SENTENCE:
                rep.warn(where, f"sentence of {len(sent.split())} words; split it for the ear")
        if not line_claims and set(norm_words(say)) & NUMBER_WORDS:
            rep.warn(where, "states a quantity but carries no {C..} claim tag")

    # structure
    for name in RESERVED_TOPICS:
        if name not in roles_by_section:
            rep.fail("script.md", f"missing '## {name.title()}' section")
    expected = ["opening"] + topic_order + ["conclusion"]
    got = [t for t in seen_topics if t in expected]
    if got != [t for t in expected if t in got]:
        rep.fail("script.md", f"sections out of outline order: {' → '.join(got)}")
    for tid in topic_order:
        if tid not in roles_by_section:
            rep.fail("script.md", f"topic {tid} ({topics[tid]}) has no section")
            continue
        missing = [r for r in TOPIC_ROLES if r not in roles_by_section[tid]]
        if missing:
            rep.fail("script.md", f"topic {tid} is missing: {', '.join(missing)}")
        title = topics[tid]
        announce = " ".join(say for _, roles, say in lines_by_section[tid] if "announce" in roles)
        if title and announce and not contains_phrase(announce, title):
            rep.fail("script.md", f"topic {tid} announcement does not say its title '{title}'")
    opening = roles_by_section.get("opening", set())
    for r in ("goal", "roadmap"):
        if r not in opening:
            rep.fail("script.md", f"opening is missing: {r}")
    roadmap = " ".join(say for _, roles, say in lines_by_section.get("opening", []) if "roadmap" in roles)
    for tid, title in topics.items():
        if roadmap and title and not contains_phrase(roadmap, title):
            rep.fail("script.md", f"roadmap does not name topic {tid} '{title}'")
    if "synthesis" not in roles_by_section.get("conclusion", set()):
        rep.fail("script.md", "conclusion is missing: synthesis")

    # engagement
    for sec, linenos in pending_predicts.items():
        for ln in linenos:
            rep.fail(f"script.md:{ln}", f"[predict] has no later [reveal] in the same section ({sec})")
    reduced = brief.get("engagement", "").lower().startswith("reduced")
    if "puzzle" in opening and "reveal" not in roles_by_section.get("conclusion", set()):
        rep.fail("script.md", "the opening poses a [puzzle] but the conclusion has no [reveal] that answers it")
    if not reduced:
        if "puzzle" not in opening:
            rep.warn("script.md", "the opening has no [puzzle]; see references/engagement.md "
                                  "(or set 'Engagement: reduced, because …' in the Brief)")
        if not any("predict" in r for r in roles_by_section.values()):
            rep.warn("script.md", "no [predict] anywhere; one or two predictions hold attention")

    # ---- storyboard
    sb = text["storyboard.md"]
    blocks, cur_block = {}, None
    order = []
    for i, line in enumerate(sb, 1):
        s = line.strip()
        h = BLOCK_HEAD_RE.match(s)
        if h:
            cur_block = h.group(1)
            if cur_block in blocks:
                rep.fail(f"storyboard.md:{i}", f"{cur_block} is defined twice")
            blocks[cur_block] = {"_line": i, "_head": (h.group(2) or "").strip(), "_fields": {}}
            order.append(cur_block)
            continue
        if s.startswith("## ") or s.startswith("### "):
            cur_block = None
            continue
        m = FIELD_RE.match(s)
        if cur_block and m:
            blocks[cur_block]["_fields"][m.group(1).strip().lower()] = (i, m.group(2).strip())

    figures = {k: v for k, v in blocks.items() if k.startswith("F")}
    scenes = [k for k in order if k.startswith("S")]

    def fval(block, key):
        return block["_fields"].get(key, (block["_line"], ""))

    figure_claims = {}
    for fid, b in figures.items():
        where = f"storyboard.md:{b['_line']}"
        for key in ("type", "data", "encodings", "reading steps"):
            if not fval(b, key)[1]:
                rep.fail(where, f"figure {fid} is missing '{key}'")
        data = fval(b, "data")[1]
        for d in re.findall(r"D\d+", data):
            if d not in data_ids:
                rep.fail(where, f"figure {fid} uses unknown data source {d}")
        if data and not re.findall(r"D\d+", data) and "none" not in data.lower():
            rep.fail(where, f"figure {fid} names no data source (D ID), and is not marked 'none (conceptual)'")
        fc = re.findall(r"C\d+", fval(b, "claims")[1])
        for c in fc:
            use_claim(c, where)
        figure_claims[fid] = fc

    prev_topic = None
    seen_sb_topics = []
    total = 0.0
    for sid in scenes:
        b = blocks[sid]
        where = f"storyboard.md:{b['_line']}"
        head = b["_head"].split()[0] if b["_head"] else ""
        topic = head.lower() if head.lower() in RESERVED_TOPICS else head
        if not topic:
            rep.fail(where, f"scene {sid} heading has no topic ('### {sid} · T1')")
        elif topic not in RESERVED_TOPICS and topic not in topics:
            rep.fail(where, f"scene {sid} names unknown topic {topic}")
        if topic and topic not in seen_sb_topics:
            seen_sb_topics.append(topic)
        st = script_scene_topic.get(sid)
        narration = fval(b, "narration")[1].lower()
        silent = "silent" in narration or narration.startswith("none")
        if st is None and not silent:
            rep.fail(where, f"scene {sid} has no narration lines in script.md and is not marked silent")
        elif st is not None and topic and st != topic:
            rep.fail(where, f"scene {sid} is {topic} here but its narration sits under {st} in script.md")
        if sid in predict_scenes and not fval(b, "withheld")[1]:
            rep.fail(where, f"scene {sid} asks the viewer to predict but has no 'Withheld' field "
                            "saying what stays off screen until the reveal")
        for key in ("look at", "focus by", "stays", "changes", "duration"):
            if not fval(b, key)[1]:
                rep.fail(where, f"scene {sid} is missing '{key}'")
        focus = fval(b, "focus by")[1].lower()
        if focus and focus not in FOCUS_VALUES:
            rep.fail(where, f"scene {sid} 'Focus by' must be figure, cursor, or figure + cursor")
        if prev_topic is not None and topic != prev_topic:
            tc = fval(b, "topic change")[1]
            if not tc or tc.lower().startswith("no"):
                rep.fail(where, f"scene {sid} starts {topic} but has no visible 'Topic change' marker")
        prev_topic = topic
        motion = fval(b, "motion")[1].lower()
        if motion:
            for verb in re.split(r"[,;+]|\bthen\b", motion):
                v = verb.strip()
                if v and v not in MOTION_VERBS:
                    rep.warn(where, f"motion '{v}' is not in the motion-verb list")
        dur = parse_seconds(fval(b, "duration")[1])
        if dur is None:
            rep.fail(where, f"scene {sid} duration is not parseable")
        else:
            total += dur
            need = scene_words.get(sid, 0) / wpm * 60 + scene_pause.get(sid, 0.0)
            hold = parse_seconds(fval(b, "hold")[1]) or 0
            required = need + hold * 0.5
            if dur + 0.5 < required:
                rep.warn(where, f"scene {sid} lasts {dur:.0f}s but needs about {required:.0f}s "
                                f"({need:.0f}s of narration and pauses at {wpm} wpm, plus half "
                                f"its {hold:.0f}s hold)")

        listed = re.findall(r"C\d+", fval(b, "claims")[1])
        for c in listed:
            use_claim(c, where)
        fig = re.findall(r"F\d+", fval(b, "figure")[1])
        allowed = set()
        for f in fig:
            if f not in figures:
                rep.fail(where, f"scene {sid} uses unknown figure {f}")
            listed += figure_claims.get(f, [])
        for c in listed:
            if c in claims:
                allowed |= numbers_in(claims[c]["values"])
        lineno, onscreen = fval(b, "on screen")
        for n in sorted(numbers_in(onscreen)):
            if n not in allowed:
                rep.fail(f"storyboard.md:{lineno}",
                         f"on-screen number {n} in {sid} is not in the Values of any claim the scene lists")

    for sid in script_scene_topic:
        if sid not in blocks:
            rep.fail("script.md", f"scene {sid} is narrated but not in storyboard.md")
    exp_sb = [t for t in expected if t in seen_sb_topics]
    if seen_sb_topics != exp_sb:
        rep.warn("storyboard.md", f"topics appear out of outline order: {' → '.join(seen_sb_topics)}")

    for cid in claims:
        if cid not in used_claims:
            rep.notes.append(f"claim {cid} is listed but not used in the script or storyboard")

    # ---- timing summary
    words = sum(scene_words.values())
    pauses = sum(scene_pause.values())
    narr = words / wpm * 60 + pauses
    rep.notes.append(f"{len(topics)} topics, {len(scenes)} scenes, {len(figures)} figures, "
                     f"{len(claims)} claims ({sum(1 for c in claims.values() if c['status'] == 'verified')} verified)")
    rep.notes.append(f"narration: {words} words at {wpm} wpm + {pauses:.1f}s pauses ≈ {fmt(narr)}")
    rep.notes.append(f"storyboard total: {fmt(total)}" + (f"; target {fmt(target)}" if target else ""))
    if target and total > target * 1.1:
        rep.warn("storyboard.md", f"runs {fmt(total)}, more than 10% over the {fmt(target)} target; "
                                  "cut scope rather than speed up")
    if total and narr > total * 1.05:
        rep.warn("storyboard.md", f"narration ({fmt(narr)}) is longer than the storyboard ({fmt(total)})")
    return rep


def fmt(sec):
    sec = int(round(sec or 0))
    return f"{sec // 60}:{sec % 60:02d}"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("out_dir", type=Path)
    ap.add_argument("--wpm", type=int, help="override the speech rate in the teaching plan")
    ap.add_argument("--phrases", type=Path, default=Path(__file__).with_name("banned_phrases.txt"))
    args = ap.parse_args(argv)
    if not args.out_dir.is_dir():
        print(f"not a directory: {args.out_dir}", file=sys.stderr)
        return 2
    rep = check(args.out_dir, args.wpm, args.phrases)
    print(f"# check_outputs: {args.out_dir}\n")
    print(f"FAIL {len(rep.fails)} · WARN {len(rep.warns)}\n")
    for title, items in (("FAIL", rep.fails), ("WARN", rep.warns), ("Summary", rep.notes)):
        if items:
            print(f"## {title}\n")
            for it in items:
                print(f"- {it}")
            print()
    print("This check covers structure, traceability, and TTS-readiness only. "
          "It does not verify that claims are true or that the video is easy to follow.")
    return 1 if rep.fails else 0


if __name__ == "__main__":
    sys.exit(main())
