"""Tests for scripts/check_outputs.py.

Each test copies the passing short example, breaks one rule, and checks that the checker
reports it at the right tier. Run: python3 -m unittest discover tests
"""

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_outputs  # noqa: E402

SHORT = ROOT / "examples" / "short-body-mass"
COMPLEX = ROOT / "examples" / "bill-paradox"
PHRASES = ROOT / "scripts" / "banned_phrases.txt"


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        for f in check_outputs.FILES:
            shutil.copy(SHORT / f, self.tmp / f)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def edit(self, name, old, new, count=1):
        p = self.tmp / name
        text = p.read_text(encoding="utf-8")
        self.assertIn(old, text, f"fixture text not found in {name}: {old!r}")
        p.write_text(text.replace(old, new, count), encoding="utf-8")

    def run_check(self):
        return check_outputs.check(self.tmp, phrases_path=PHRASES)

    def assertFails(self, fragment):
        rep = self.run_check()
        self.assertTrue(any(fragment in f for f in rep.fails),
                        f"expected FAIL containing {fragment!r}; got {rep.fails}")

    def assertWarns(self, fragment):
        rep = self.run_check()
        self.assertTrue(any(fragment in w for w in rep.warns),
                        f"expected WARN containing {fragment!r}; got {rep.warns}")


class ExamplesPass(unittest.TestCase):
    def test_examples_have_no_fail(self):
        for d in (SHORT, COMPLEX):
            rep = check_outputs.check(d, phrases_path=PHRASES)
            self.assertEqual(rep.fails, [], f"{d.name}: {rep.fails}")


class Narration(Base):
    def test_digit_in_narration(self):
        self.edit("script.md", "about five thousand grams", "about 5000 grams")
        self.assertFails("digit in narration")

    def test_symbol_in_narration(self):
        self.edit("script.md", "Each dot is one bird.", "Each dot = one bird.")
        self.assertFails("symbol")

    def test_banned_phrase(self):
        self.edit("script.md", "Each dot is one bird.", "It's important to note that each dot is one bird.")
        self.assertFails("banned phrase")

    def test_hedge_stack(self):
        self.edit("script.md", "So it's the Gentoo.", "So it could potentially be the Gentoo.")
        self.assertFails("could potentially")

    def test_unknown_mark(self):
        self.edit("script.md", "{beat}", "{pause}")
        self.assertFails("unknown mark")

    def test_acronym_without_pronunciation(self):
        self.edit("script.md", "Each dot is one bird.", "Each dot is one bird from the LTER.")
        self.assertWarns("'LTER' is not in the Pronunciation table")

    def test_quantity_without_claim(self):
        self.edit("script.md", "Each dot is one bird.", "Each dot is one of three hundred birds.")
        self.edit("script.md", "{C01} {C02} {beat}", "{beat}")
        self.assertWarns("no {C..} claim tag")


class Structure(Base):
    def test_missing_wrap_up(self):
        self.edit("script.md", "[S04] [wrap-up+bridge]", "[S04] [bridge]")
        self.assertFails("topic T1 is missing: wrap-up")

    def test_announcement_without_title(self):
        self.edit("script.md", "[S02] [announce+introduce] Weight by species.", "[S02] [announce+introduce] Part one.")
        self.assertFails("announcement does not say its title")

    def test_roadmap_missing_topic(self):
        self.edit("script.md", "Then, the Gentoo gap.", "Then, the difference.")
        self.assertFails("roadmap does not name topic T2")

    def test_missing_conclusion(self):
        self.edit("script.md", "## Conclusion", "## Ending")
        self.assertFails("missing '## Conclusion' section")

    def test_scene_spans_two_topics(self):
        self.edit("script.md", "[S05] [announce+introduce]", "[S04] [announce+introduce]")
        self.assertFails("carries lines from two topics")

    def test_topic_change_marker_required(self):
        self.edit("storyboard.md", "- Topic change: outline item one lights up\n", "")
        self.assertFails("has no visible 'Topic change' marker")

    def test_scene_missing_focus(self):
        self.edit("storyboard.md", "- Look at: the empty axes\n", "")
        self.assertFails("missing 'look at'")

    def test_bad_focus_value(self):
        self.edit("storyboard.md", "- Focus by: figure + cursor", "- Focus by: spotlight")
        self.assertFails("'Focus by' must be")

    def test_narrated_scene_missing_from_storyboard(self):
        self.edit("script.md", "[S07] [synthesis]", "[S08] [synthesis]")
        self.assertFails("scene S08 is narrated but not in storyboard.md")

    def test_objective_unknown_topic(self):
        self.edit("teaching-plan.md", "| O2 | read an estimate with its interval and say whether it could be zero | T2 |",
                  "| O2 | read an estimate with its interval and say whether it could be zero | T9 |")
        self.assertFails("unknown topic T9")

    def test_missing_file(self):
        (self.tmp / "storyboard.md").unlink()
        self.assertFails("file missing")


class Evidence(Base):
    def test_untraced_onscreen_number(self):
        self.edit("storyboard.md", '- On screen: "Adelie 3700.7 g" · "Chinstrap 3733.1 g" · "Gentoo 5076.0 g"',
                  '- On screen: "Adelie 3700.7 g" · "Chinstrap 3733.1 g" · "Gentoo 5100 g"')
        self.assertFails("on-screen number 5100")

    def test_orientation_numbers_not_checked(self):
        self.edit("storyboard.md", '- Orientation text: "The Gentoo gap"', '- Orientation text: "2 / 2 · The Gentoo gap"')
        rep = self.run_check()
        self.assertEqual(rep.fails, [])

    def test_unknown_claim(self):
        self.edit("script.md", "{C03} {beat}", "{C99} {beat}")
        self.assertFails("claim C99 is not in the Claims table")

    def test_gap_claim_used(self):
        self.edit("evidence-and-review.md", "| D01 | species Gentoo, body_mass_g | verified |",
                  "| D01 | species Gentoo, body_mass_g | gap |")
        self.assertFails("claim C03 is a gap")

    def test_unverified_claim_warns(self):
        self.edit("evidence-and-review.md", "| D01 | species Gentoo, body_mass_g | verified |",
                  "| D01 | species Gentoo, body_mass_g | unverified |")
        self.assertWarns("claim C03 is unverified")

    def test_claim_without_source(self):
        self.edit("evidence-and-review.md", "| D01 | species Gentoo, body_mass_g | verified |",
                  "| — | species Gentoo, body_mass_g | verified |")
        self.assertFails("claim C03 has no data source")

    def test_gap_claim_needs_no_source(self):
        self.edit("evidence-and-review.md", "verified |\n\n## Simplifications and analogies",
                  "verified |\n| C99 | Diet shapes bills | — | — | no diet variable in D04 | gap |\n\n## Simplifications and analogies")
        rep = self.run_check()
        self.assertEqual(rep.fails, [])
        self.assertTrue(any("C99" in n for n in rep.notes), "C99 row was not parsed")

    def test_figure_without_data_source(self):
        self.edit("storyboard.md", "- Data: D02, row \"Welch difference\", columns estimate and ci95",
                  "- Data: the Welch row")
        self.assertFails("figure F02 names no data source")


class Engagement(Base):
    def test_predict_needs_thinking_time(self):
        self.edit("script.md", "which is the heavy one? {look:3}", "which is the heavy one? {beat}")
        self.assertFails("gives 0.8s to think")

    def test_predict_needs_reveal(self):
        self.edit("script.md", "[S03] [reveal] Each dot", "[S03] [explain] Each dot")
        self.assertFails("has no later [reveal]")

    def test_predict_and_reveal_cannot_share_a_line(self):
        self.edit("script.md", "[S02] [predict]", "[S02] [predict+reveal]")
        self.assertFails("cannot share a line")

    def test_predict_scene_needs_withheld(self):
        self.edit("storyboard.md", "- Withheld: every dot; the three species columns stay empty through the guess\n", "")
        self.assertFails("has no 'Withheld' field")

    def test_puzzle_needs_answer(self):
        self.edit("script.md", "[S07] [reveal]", "[S07] [synthesis]")
        self.assertFails("the conclusion has no [reveal]")

    def test_no_puzzle_warns_unless_reduced(self):
        self.edit("script.md", "[S01] [puzzle+goal]", "[S01] [goal]")
        self.assertWarns("the opening has no [puzzle]")
        self.edit("teaching-plan.md", "- Engagement: full", "- Engagement: reduced, because formal talk")
        rep = self.run_check()
        self.assertFalse(any("[puzzle]" in w for w in rep.warns))

    def test_gap_claim_allowed_in_unknown_line(self):
        self.edit("evidence-and-review.md", "verified |\n\n## Simplifications and analogies",
                  "verified |\n| C07 | Why Gentoos are heavier | — | — | no diet or ecology variables in D04 | gap |\n\n## Simplifications and analogies")
        self.edit("script.md", "[S07] [synthesis] Adelie", "[S07] [unknown] These data can't say why Gentoos are heavier. {C07}\n[S07] [synthesis] Adelie")
        rep = self.run_check()
        self.assertEqual(rep.fails, [])

    def test_gap_claim_outside_unknown_fails(self):
        self.edit("evidence-and-review.md", "verified |\n\n## Simplifications and analogies",
                  "verified |\n| C07 | Why Gentoos are heavier | — | — | no diet or ecology variables in D04 | gap |\n\n## Simplifications and analogies")
        self.edit("script.md", "[S07] [synthesis] Adelie", "[S07] [explain] Gentoos are heavier because of their diet. {C07}\n[S07] [synthesis] Adelie")
        self.assertFails("may be spoken only in an [unknown] line")


class Timing(Base):
    def test_over_target(self):
        self.edit("teaching-plan.md", "- Target duration: 2:00", "- Target duration: 0:45")
        self.assertWarns("over the 0:45 target")

    def test_scene_too_short(self):
        self.edit("storyboard.md", "- Duration: 16s", "- Duration: 4s")
        self.assertWarns("scene S03 lasts 4s but needs about")


class Helpers(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(check_outputs.numbers_in("r = −0.24 · 2007–2009 · 5,076 g"),
                         {"-0.24", "2007", "2009", "5076"})

    def test_seconds(self):
        self.assertEqual(check_outputs.parse_seconds("1:45"), 105)
        self.assertEqual(check_outputs.parse_seconds("12s"), 12)
        self.assertEqual(check_outputs.parse_seconds("2 min"), 120)

    def test_phrase_matching_is_word_bounded(self):
        self.assertTrue(check_outputs.contains_phrase("Let's dive into it", "dive into"))
        self.assertFalse(check_outputs.contains_phrase("the divers went in", "dive"))


if __name__ == "__main__":
    unittest.main()
