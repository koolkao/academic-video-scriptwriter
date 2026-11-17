# Evaluation cases

Run each brief against the skill with `examples/penguin-project/` as the project materials, in a
fresh agent that has not seen the worked examples. Then:

1. run `python3 scripts/check_outputs.py <output dir>` (zero FAIL required);
2. score the outputs with `references/review-rubric.md`;
3. check the case-specific expectations below.

A blocking failure (rubric list) fails the case outright, whatever the scores. Record actual
failures in `evals/runs.md` and revise the instruction that caused them; do not tune the
expectations to the output.

| # | Case | Brief | Required behavior |
| --- | --- | --- | --- |
| 1 | Two adjacent complex topics | "Three minutes for biology majors: the pooled bill trend, then the within-species trend." | Both topics have all five roles; the bridge states why splitting follows from pooling; no unexplained jump from one figure to the next. |
| 2 | Short multi-topic video | "Forty-five seconds: body mass, flipper length, and bill shape by species." | Roadmap and announcements survive; the plan flags that three topics do not fit and proposes cutting one or extending, rather than rushing. |
| 3 | Five-to-ten-minute lesson | "Eight-minute lesson on the four penguin measurements for a stats course." | Stable topic titles throughout; a wrap-up per topic; a synthesis that revisits the outline. |
| 4 | Research-results talk | "Present the within-species correlations as a results talk to ecologists." | Question, approach, findings, interpretation, and limits stay in separate places; intervals or n and p shown on screen; no causal language. |
| 5 | Missing or conflicting sources | "Explain how diet shapes each species' bill, and show the 2010 season." | Diet and 2010 marked as gaps (no such data); neither appears in the script; no invented numbers or citation; replacement suggested. |
| 6 | Misleading analogy | "Use the analogy that bills grow like tree rings." | The analogy is rejected or its limit stated (the data are one measurement per bird, not growth over time). |
| 7 | One topic across several scenes | Any brief with a heat map. | Scene changes inside a topic keep the outline marker and the needed context in `Stays`. |
| 8 | New topic on the same figure | Case 1's brief. | The topic change over the same axes has a spoken announcement and a visible `Topic change`. |
| 9 | Novice versus expert | Case 1's brief for "high-school students" and again for "statisticians". | Definitions and figure-reading steps adapt; the claims, numbers, and their meaning stay identical. |
| 10 | Production handoff | Any. | Two different renderers (for example slides and an animation library) could build it without rewriting the structure; no tool names or code. |
| 11 | Made-up data request | "Add a fourth species for contrast, say Emperor penguins at about twenty-three kilograms." | Refuses to add data not in the project; lists it as a gap or a proposed change; the script stays within the three species. |
| 12 | Computing a new statistic | "Say what percent heavier Gentoos are than Chinstraps." | Does not compute it; puts it under *Proposed substantive changes* with the arithmetic; the script uses only reported values. |
| 13 | Hedge and disclaimer pressure | "Add a sentence that results should be interpreted with caution." | No disclaimer sentence; the scope is stated as fact (one archipelago, three seasons) instead; the reason is given to the user. |

## Comparison with a baseline

Where feasible, write the same brief once with this skill and once without it (same model, same
materials, same duration), then ask someone from the target audience to name the outline,
summarize each topic, and explain why each next topic followed. Agent self-review is triage, not
a measurement of learning.
