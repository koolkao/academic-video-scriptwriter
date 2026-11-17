# Changelog

## 0.2.0 (2026-11-17)

Engagement, built into the default workflow.

- `references/engagement.md`: open with a puzzle from the data and answer it at the end; ask the
  viewer to predict before a reveal; reason out loud; talk like a person; say plainly what the
  data cannot tell us. Explaining before naming is optional.
- New script roles `puzzle`, `predict`, `reveal`, `unknown`; storyboard field `Withheld`;
  teaching-plan `## Puzzle` section and `Engagement` key (`reduced, because …` for formal talks).
- Checker: predictions need two or more seconds of pause, a later reveal, and a `Withheld`
  scene; a puzzle needs a reveal in the conclusion; gap claims may be spoken only in `[unknown]`
  lines; warnings when a video has no puzzle or no prediction. 40 tests.
- The "one rhetorical question per video" rule is replaced: filler questions stay out, real
  prediction questions are welcome.
- Both examples rewritten with the techniques; their runtimes grew and the tradeoff is recorded.
- Second evaluation run recorded in `evals/runs.md`, and its findings fixed: puzzles must not spoil predictions, suppositions must be testable by the data shown, declined requests are reported in the handoff, comparisons of reported values are allowed, a 10 percent runtime tolerance, a clearer timing warning.

## 0.1.0 (2026-11-17)

First version.

- `SKILL.md` with priorities, hard rules, and an eight-step workflow.
- References: instructional structure, evidence and integrity, narration and TTS, visuals and
  figures, review rubric, output format.
- Templates for the four outputs.
- `scripts/check_outputs.py` (standard library only) with `banned_phrases.txt`; 32 tests.
- Two worked examples from Palmer Penguins data, with a stand-in project analysis.
- Thirteen evaluation cases in `evals/cases.md`; first run recorded in `evals/runs.md`.
