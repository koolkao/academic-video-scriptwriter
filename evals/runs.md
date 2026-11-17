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

## 2026-11-17, run 2 (v0.2, engagement)

- **Setup and brief:** identical to run 1, on the v0.2 skill.
- **Outputs:** `evals/runs/2026-11-17-run-2/` (written before the fixes below).
- **Checker:** first draft FAIL 1 (the diet gap claim listed on a storyboard scene), WARN 12 (ten
  timing: 530 words against a 360-word budget, so it cut hard; two untagged quantities). Final FAIL
  0, WARN 0; storyboard 3:08 against 3:00.
- **Fresh sub-agent review:** one blocking failure the checker cannot see. A reasoning-out-loud
  line ("suppose bigger birds just have bigger bills") widened the claim to body size, which the
  figure did not show. Rewritten.

| Technique | Use |
| --- | --- |
| Puzzle | Pooled r = −0.24 posed as "that's odd"; answered in the conclusion. |
| Prediction | "Inside each species, up, or down?" with four seconds, species colors withheld. |
| Reasoning out loud | Two suppositions (a trade-off versus long-and-deep together), tested on screen. |
| Conversational register | "you", contractions, a line for viewers who guessed down. |
| Stated unknown | One `[unknown]` line: correlational data, diet not measured. |

Cases 1, 5, 8, 12, 13 pass again.

### Friction reported, and what changed

| Friction | Fix |
| --- | --- |
| The engagement guide's sample puzzle stated the within-species answer, which spoils a later prediction. The author's own complex example had the same flaw. | The guide now says the puzzle poses the question and must not leak a prediction's answer (check the goal line too). The example's puzzle and goal were rewritten. |
| Reasoning out loud pulled toward mechanisms the data cannot support (the blocking failure). | Suppositions must be testable by the data on screen, in its own terms; explanations of why a pattern appears are listed as interpretation. The complex example's supposition was rewritten the same way. |
| All three special requests conflict with hard rules, and the skill declines them without asking, which may frustrate the user. | The handoff step now requires saying what was asked, what was done instead, and what would make the original possible. |
| A 360-word budget barely holds a puzzle, roadmap, two topics, and a prediction. | Short-video guidance: puzzle shares the goal line, compressed roles, one prediction at most; cut content, not orientation. |
| Is "stronger than pooled" a computation? | Comparing reported values (larger, smaller, opposite sign) is reading; by how much is computing. |
| How far over target is acceptable? | Within 10 percent; beyond that, cut or tell the user. |
| The checker warned "lasts 17s but needs about 17s". | The message now shows the hold allowance it adds. |

Not yet run: cases 2, 3, 4, 6, 7, 9, 10, 11; a baseline comparison; any test with real viewers.
