# Example project: Palmer Penguins

This folder plays the part of a research project whose data and results already exist. The
worked examples read these files; the skill never runs the analysis and never computes new
numbers.

- `data/penguins.csv`: Palmer Penguins raw data, 344 rows. Horst AM, Hill AP, Gorman KB (2020).
  palmerpenguins: Palmer Archipelago (Antarctica) penguin data. Data collected by Dr. Kristen
  Gorman with the Palmer Station, Antarctica LTER. License CC0-1.0. Copied from
  [allisonhorst/palmerpenguins](https://github.com/allisonhorst/palmerpenguins) at commit
  `8957207b78d6ccd1b4654a9dd9c9041b657478ab`, `inst/extdata/penguins.csv`.
- `analysis.py`: the "project's" analysis. Re-run with `python3 analysis.py` (pandas, numpy,
  scipy).
- `results/`: what the analysis produced.

| File | Contents | sha256 |
| --- | --- | --- |
| `data/penguins.csv` | raw rows | `f204db2c753b0937caac3cb35258562c14f073e4bbc76be24b4c51ce22767a93` |
| `results/species_summary.csv` | n, mean, SD per species and measure | `44ac13cc1268ffd0403bcb8aa946be52a9d3acf7375307cb495271b82098b45d` |
| `results/correlations.csv` | Pearson r, pooled and within species | `adea0068f40a32fbca1f530710e5072b44a65888cfb4164068f472bb6836a73f` |
| `results/body_mass_tests.csv` | ANOVA; Welch difference Gentoo − Adelie | `f09ce2de52e96d7fd7ef8a55db1fb27f5a3eecd4e9bca4358f05ddd6dadb1a7f` |
| `results/species_profiles_z.csv` | species means as z-scores of pooled mean and SD | `2bd621ffa7787abc19ccb9aef2de2f52dac3582797e8e64724f1b1f7f166703b` |
