# Phase A — Source and license review

Checked 2026-11-17 via the GitHub API. Factual license review, not legal advice.

| # | Source | Pinned revision (path last touched) | License | Reuse decision |
| --- | --- | --- | --- | --- |
| 1 | [skindhu/skind-skills](https://github.com/skindhu/skind-skills) `skills/educational-video-creator` (incl. `references/script-and-narration.md`) | HEAD `cda40dcb11adcd3c280526fff3ccfbbd64222822` (2026-02-25); path `c5217fe34efe08b03f8a9722282a79ed71ffa25c` (2026-02-05); script guide `6595c81ca35ee05da61707b789f76c20f982f5f4` (2026-02-04) | MIT (root `LICENSE`, "Copyright (c) 2026 long_long_ago") | Adaptation permitted. Keep MIT notice in an attribution file if any substantial portion is adapted. |
| 2 | [yigityildiz0/scientific-agent-skills](https://github.com/yigityildiz0/scientific-agent-skills) `skills/codex/academic-presentations` | HEAD `5996deb3a2c7bb260b3d7aae4ab3e087077afb11` (2026-10-14); path `4c3c01434e73b06af77c3019c39f1ad589064b64` (2026-10-05) | **None asserted.** Root MIT explicitly excludes `skills/`; listed under `license_gaps` in `provenance-current.json`. | Ideas only. Write all text originally; do not copy or closely paraphrase. |
| 3 | [OpenMontageInc/OpenMontage](https://github.com/OpenMontageInc/OpenMontage) `skills/pipelines/explainer/script-director.md` | HEAD `2e003e65fa99a0f329478a2c1cdcf26bc481933a` (2026-11-16); file `9482eddeff1f11cc352ca1d2d49ce26981ee3023` (2026-08-03) | AGPL-3.0 (root `LICENSE`) | Ideas only. Adapting text would make the skill an AGPL derivative. |
| 4 | Same repo, `skills/creative/storytelling.md` | file `fdd6457fed4d00aef47e40cc0a7635e6d37d5729` (2026-04-28) | AGPL-3.0 | Ideas only. Its header cites third-party sources (Mayer, 3Blue1Brown, etc.) whose rights are separate. |

## Consequences for Phase B

- All skill text is written originally. Source 1 is the only one whose wording may be adapted, and only with its MIT notice kept.
- Never mix text from sources 3–4 into the skill unless the whole skill is licensed AGPL-3.0.
- Unverified: real identity of source 1's copyright holder; OpenMontage's copyright holder.
- Re-check these revisions before any later adaptation; do not auto-import upstream changes.
