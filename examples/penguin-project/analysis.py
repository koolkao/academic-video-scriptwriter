"""Analysis for the example 'project' used by the worked examples.

This stands in for a real research project's own analysis. The skill never runs it;
it only reads the results it already produced (results/*.csv).

Data: Palmer Penguins (Horst, Hill & Gorman 2020), CC0-1.0,
allisonhorst/palmerpenguins @ 8957207b78d6ccd1b4654a9dd9c9041b657478ab, inst/extdata/penguins.csv.

Run:  python3 analysis.py   (needs pandas, numpy, scipy)
"""

from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

HERE = Path(__file__).parent
OUT = HERE / "results"
MEASURES = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]


def main() -> None:
    df = pd.read_csv(HERE / "data" / "penguins.csv", na_values=["NA"])
    OUT.mkdir(exist_ok=True)

    # 1. Per-species descriptive statistics (complete cases per measure).
    rows = []
    for sp, g in df.groupby("species"):
        for m in MEASURES:
            x = g[m].dropna()
            rows.append({"species": sp, "measure": m, "n": len(x),
                         "mean": round(x.mean(), 1), "sd": round(x.std(ddof=1), 1)})
    pd.DataFrame(rows).to_csv(OUT / "species_summary.csv", index=False)

    # 2. Pearson correlations: pooled and within species.
    rows = []
    pairs = [(a, b) for i, a in enumerate(MEASURES) for b in MEASURES[i + 1:]]
    groups = [("all", df)] + list(df.groupby("species"))
    for label, g in groups:
        for a, b in pairs:
            d = g[[a, b]].dropna()
            r, p = stats.pearsonr(d[a], d[b])
            rows.append({"group": label, "x": a, "y": b, "n": len(d),
                         "r": round(r, 2), "p": f"{p:.1e}"})
    pd.DataFrame(rows).to_csv(OUT / "correlations.csv", index=False)

    # 3. Body mass: one-way ANOVA across species; Gentoo vs Adelie Welch difference.
    d = df.dropna(subset=["body_mass_g"])
    samples = [g["body_mass_g"].values for _, g in d.groupby("species")]
    f, p = stats.f_oneway(*samples)
    gen = d.loc[d.species == "Gentoo", "body_mass_g"]
    ade = d.loc[d.species == "Adelie", "body_mass_g"]
    diff = gen.mean() - ade.mean()
    se = np.sqrt(gen.var(ddof=1) / len(gen) + ade.var(ddof=1) / len(ade))
    dof = se**4 / ((gen.var(ddof=1) / len(gen))**2 / (len(gen) - 1)
                   + (ade.var(ddof=1) / len(ade))**2 / (len(ade) - 1))
    t_crit = stats.t.ppf(0.975, dof)
    pd.DataFrame([
        {"test": "one-way ANOVA, body mass by species", "statistic": f"F = {f:.1f}",
         "df": f"2, {len(d) - 3}", "p": f"{p:.1e}", "estimate": "", "ci95": ""},
        {"test": "Welch difference, Gentoo minus Adelie body mass (g)", "statistic": "",
         "df": f"{dof:.0f}", "p": f"{stats.ttest_ind(gen, ade, equal_var=False).pvalue:.1e}",
         "estimate": f"{diff:.0f}", "ci95": f"{diff - t_crit * se:.0f} to {diff + t_crit * se:.0f}"},
    ]).to_csv(OUT / "body_mass_tests.csv", index=False)

    # 4. Species profiles as z-scores against the pooled mean/SD (for a radar plot).
    rows = []
    for sp, g in df.groupby("species"):
        row = {"species": sp}
        for m in MEASURES:
            row[m] = round((g[m].mean() - df[m].mean()) / df[m].std(ddof=1), 2)
        rows.append(row)
    pd.DataFrame(rows).to_csv(OUT / "species_profiles_z.csv", index=False)


if __name__ == "__main__":
    main()
