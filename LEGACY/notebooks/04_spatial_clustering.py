# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

# %% [markdown]
# # 04 — Spatial clustering
#
# Global Moran's *I* statistics confirm statistically significant
# positive spatial autocorrelation for gap scores, need scores, and
# disability rates — accessibility deficits concentrate in identifiable
# geographic corridors rather than scattering randomly.
#
# Methodology: 2 km distance-based spatial weights (mean 47.9 neighbors
# per unit, 2,315 / 2,317 units have ≥1 neighbor). Detail in
# [`manuscripts/supplementary/spatial-diagnostics.md`](../manuscripts/supplementary/spatial-diagnostics.md)
# and [`manuscripts/supplementary/model-specification.md`](../manuscripts/supplementary/model-specification.md).

# %% tags=["jc.setup"]
import jellycell.api as jc
import pandas as pd
from IPython.display import Image

# %% tags=["jc.load", "name=morans_i_table"]

morans = pd.DataFrame(
    [
        ("Gap score",       0.2271, -0.0004, 40.87, "<.001", "***"),
        ("Need score",      0.1991, -0.0004, 33.91, "<.001", "***"),
        ("Disability rate", 0.2757, -0.0004, 48.92, "<.001", "***"),
    ],
    columns=["variable", "morans_i", "expected_i", "z", "p", "sig"],
)
jc.table(
    morans,
    name="global_morans_i",
    caption="Global Moran's I for gap, need, disability — 2 km row-standardized weights",
    notes="All three variables exhibit strong positive spatial clustering. Implies OLS standard errors are likely understated.",
)
print(morans.to_string(index=False))

# %% tags=["jc.step", "name=spatial_summary", "deps=morans_i_table"]
spatial = {
    "weights_threshold_m": 2000,
    "units_total": 2317,
    "units_with_neighbors": 2315,
    "mean_neighbors": 47.9,
    "median_neighbors": 51,
    "max_neighbors": 86,
    "interpretation": (
        "Strong positive autocorrelation across all three variables. "
        "Gap score I=0.23 (z=40.87) — high-gap tracts cluster near other "
        "high-gap tracts. Geographic targeting of investment (vs. spatially "
        "uniform upgrades) implied as higher-yield policy."
    ),
}
jc.save(spatial, "artifacts/spatial_summary.json", caption="Spatial weights and clustering summary")

# %% [markdown]
# ### Figure 4 — Choropleth: gap score across NYC
#
# High-gap-score tracts concentrate in southeastern Queens, central
# Brooklyn, and the northern Bronx — the corridors flagged for targeted
# investment in §5.4.

# %% tags=["jc.figure", "name=fig4_choropleth_gap"]
Image("artifacts/figures/figure-4-choropleth-gap-score.png")

# %% [markdown]
# ### Figure 14 — Geographic comparison: gap × poverty
#
# High-poverty tracts spatially overlap with high-gap-score tracts;
# the visual confirmation of the OLS regression's poverty coefficient
# (b = 0.164, p < .001).

# %% tags=["jc.figure", "name=fig14_gap_vs_poverty_map"]
Image("artifacts/figures/figure-14-gap-vs-poverty-map.png")

# %% [markdown]
# ### Figure 15 — Geographic comparison: gap × disability
#
# Disability rate has the highest Moran's I (0.28) of the three variables,
# yet it is statistically insignificant in the OLS regression — a result
# of its high collinearity with poverty (r = .70). The geographic overlap
# is striking; the modeling difficulty is the multicollinearity.

# %% tags=["jc.figure", "name=fig15_gap_vs_disability_map"]
Image("artifacts/figures/figure-15-gap-vs-disability-map.png")

# %% [markdown]
# ## Inference implication
#
# Significant Moran's *I* values for gap, need, and disability indicate
# spatial dependence that violates the OLS independence assumption.
# HC1 robust SE corrects for heteroskedasticity but **not** for spatial
# autocorrelation. Spatial HAC standard errors (Conley, 1999) or a
# spatial regression model would provide more reliable inference. The
# *R*² of .202 and the regression coefficients in notebook 03 should
# be interpreted with this caveat in mind.
#
# ---
#
# **Continue to** [`05_discussion_and_forward.py`](05_discussion_and_forward.py)
# — limitations, policy implications, and future work.
