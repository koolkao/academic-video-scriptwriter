# Evaluation runs

## 2026-11-17, run 1

- **Setup:** a fresh agent (same model as the author) with access to `SKILL.md`, `references/`,
  `templates/`, `scripts/`, and `examples/penguin-project/` only. It had not seen the worked
  examples, the evals, or the tests.
- **Brief:** a three-minute video for second-year biology majors; topic one, the pooled bill
  relationship; topic two, within species. The brief also asked it to explain how diet shapes
  bills, say what percent heavier Gentoos are than Chinstraps, and add a sentence that results
  should be interpreted with caution. Covers cases 1, 5, 8, 12, 13.
- **Outputs:** `evals/runs/2026-11-17-run-1/` (written before the fixes below).
- **Checker:** first draft FAIL 1 (conclusion scene had no topic-change marker), WARN 11 (mostly
  scenes too short; the draft ran about 3:35). Final draft FAIL 0, WARN 0; storyboard 3:17.
- **Fresh sub-agent review:** no blocking failures; four minor fixes applied.

| Case | Result |
| --- | --- |
| 1, two adjacent topics | Pass. Both topics have all five roles; the bridge says the pooled number mixes three species. |
| 5, missing data (diet) | Pass. Marked gap, not narrated; the script says the correlations describe co-variation, not what shaped it. |
| 8, topic change on the same figure | Pass. T2 announced over the same scatter, with a visible marker. |
| 12, computing a new statistic | Pass. The percent was not used; the arithmetic went to *Proposed substantive changes*. |
| 13, disclaimer pressure | Pass. No caution sentence; scope stated as fact (n, islands, years). |

### Friction reported, and what changed

| Friction | Fix |
| --- | --- |
| Gap claims had to carry a data source to pass the checker. | Checker no longer requires a source for `gap`; the guidance says to put what was searched in Location. Test added. |
| The conclusion needed a topic-change marker, but the docs said only "new topic". | `output-format.md` and the storyboard template now include the conclusion. |
| "Don't compute" seemed to contradict "propose with the arithmetic"; the reviewer flagged the proposal as a violation. | `evidence-and-integrity.md` and the rubric now say proposing arithmetic for the author is correct and only the script and storyboard must be free of it. |
| Unclear whether structural counts ("three species") need claim tags. | `output-format.md`: counts about the data are claims; counts about the video are not. |
| Timing overran with no early signal; the hold rule was undocumented. | Word budget (`minutes × wpm × 0.8`) added to the workflow; the checker's timing rule is documented. |
| Unclear whether reading years or islands from raw data is computing. | Reading categories, years, and definitions is allowed; counts and summaries need a reported value. |
| Unclear whether a fitted trend line is plotting or a new statistic, so it was left out. | Visual summaries made while plotting are allowed if the method is named, no value is printed or spoken, and the direction matches a reported result. |
| "Use TTS" was ambiguous. | `SKILL.md`: it means TTS-ready narration; generating audio is out of scope. |
| No guidance for a requested point that fits no topic; it became a weak aside. | It becomes a topic or a scope exclusion; no asides. |
| "One change at a time" was hard to meet in build scenes. | `Changes` may list an ordered sequence, each on its own narration cue. |

Not yet run: cases 2, 3, 4, 6, 7, 9, 10, 11; a baseline comparison; any test with real viewers.
