# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

# %% [markdown]
# # 03 — Temporal panel + OLS equity regression
#
# This notebook covers the DiD panel construction (§3.5), temporal
# coverage progression (§4.4), treatment-control balance (§4.5),
# distribution diagnostics (§4.6), and the OLS equity regression
# (§4.7). The detailed correlation matrix is in
# [`manuscripts/supplementary/correlation-analysis.md`](../manuscripts/supplementary/correlation-analysis.md).

# %% tags=["jc.setup"]
import jellycell.api as jc
import pandas as pd
from IPython.display import Image

# %% tags=["jc.load", "name=panel_summary"]

panel = {
    "panel_dimensions": "2317 tracts × 7 periods (2017–2023)",
    "total_observations": 16_219,
    "treatment_tracts": 831,
    "control_tracts": 1_486,
    "stations_with_sourced_dates": 101,
    "stations_with_approximate_dates": 56,
    "sourced_pct": round(101 / 157 * 100, 1),
    "coverage_progression_2017_pct": 16.8,
    "coverage_progression_2023_pct": 35.9,
}
jc.save(panel, "artifacts/panel_summary.json", caption="Temporal panel construction summary")
print(f"Panel: {panel['panel_dimensions']} ({panel['total_observations']:,} obs)")
print(f"Treatment / control: {panel['treatment_tracts']} / {panel['control_tracts']} tracts")
print(f"Sourced upgrade dates: {panel['stations_with_sourced_dates']} / 157 ({panel['sourced_pct']}%)")

# %% [markdown]
# ## DiD specification
#
# ```
# Y_it = α + β · Treatment_it + γ · X_it + δ_i + τ_t + ε_it
# ```
#
# Tract fixed effects (δ_i) absorb time-invariant tract characteristics;
# period fixed effects (τ_t) absorb city-wide temporal trends. The
# coefficient β is the average treatment effect of gaining an accessible
# station. The panel currently lacks an outcome variable Y — defining
# and linking ridership / property-value / population-change outcomes is
# explicit future work (§5.5, item 6). The current panel supports
# treatment-control comparison and balance diagnostics only.

# %% tags=["jc.step", "name=balance_table", "deps=panel_summary"]
balance = pd.DataFrame(
    [
        ("disability_rate", 0.049, 0.039, +0.010, 6.40, "<.001", 0.29, "small"),
        ("senior_rate", 0.150, 0.162, -0.012, -3.34, "<.001", -0.14, "negligible"),
        ("poverty_rate", 0.074, 0.056, +0.018, 6.42, "<.001", 0.28, "small"),
    ],
    columns=["variable", "treatment_mean", "control_mean", "diff", "t_stat", "p", "cohens_d", "magnitude"],
)
balance["p"] = balance["p"].astype(str)  # avoid pyarrow mixed-type inference
jc.table(
    balance,
    name="treatment_control_balance",
    caption="Welch's t-test: treatment vs. control tracts on demographic predictors",
    notes="All differences statistically significant; effect sizes small/negligible. Direction (treatment > control on disability/poverty) is consistent with vertical-equity targeting.",
)
print(balance.to_string(index=False))

# %% [markdown]
# ### Figure 6 — Coverage progression 2017 → 2023

# %% tags=["jc.figure", "name=fig6_coverage_progression"]
Image("artifacts/figures/figure-6-coverage-progression.png")

# %% [markdown]
# ### Figure 7 — Treatment vs. control balance check

# %% tags=["jc.figure", "name=fig7_balance"]
Image("artifacts/figures/figure-7-treatment-vs-control-balance.png")

# %% [markdown]
# ## OLS equity regression — gap score on demographics
#
# Heteroskedasticity-consistent (HC1) robust standard errors. VIFs
# below 2.3 across all three predictors — no problematic multicollinearity.

# %% tags=["jc.step", "name=ols_regression", "deps=balance_table"]
ols = pd.DataFrame(
    [
        ("(Constant)",       -0.000, 0.003, -0.00,  "0.999", ""),
        ("Poverty rate",      0.164, 0.033,  4.99,  "<.001", "***"),
        ("Disability rate",   0.013, 0.063,  0.21,  "0.84",  ""),
        ("Senior rate",       0.263, 0.017, 15.93,  "<.001", "***"),
    ],
    columns=["variable", "b", "se", "t", "p", "sig"],
)
jc.table(
    ols,
    name="ols_gap_on_demographics",
    caption="OLS: gap score on demographic predictors (HC1 robust SE)",
    notes="N=2317. R²=.202, Adj R²=.201. F(3,2313)=108.83, p<.001. Senior rate is the strongest predictor; disability is collinear with poverty (r=.70).",
)
print(ols.to_string(index=False))

ols_summary = {
    "n": 2317,
    "r_squared": 0.202,
    "adj_r_squared": 0.201,
    "f_stat": 108.83,
    "f_df": [3, 2313],
    "f_p": "<.001",
    "strongest_predictor": "senior_rate",
    "strongest_t": 15.93,
    "vif": {"disability": 2.28, "poverty": 2.24, "senior": 1.17},
}
jc.save(ols_summary, "artifacts/ols_summary.json", caption="OLS regression summary statistics")

# %% [markdown]
# ### Figure 11 — Pearson correlation heatmap

# %% tags=["jc.figure", "name=fig11_correlation"]
Image("artifacts/figures/figure-11-correlation-heatmap.png")

# %% [markdown]
# ### Figure 12 — Gap × poverty scatter

# %% tags=["jc.figure", "name=fig12_gap_vs_poverty"]
Image("artifacts/figures/figure-12-gap-vs-poverty-scatter.png")

# %% [markdown]
# ### Figure 13 — Gap × disability scatter

# %% tags=["jc.figure", "name=fig13_gap_vs_disability"]
Image("artifacts/figures/figure-13-gap-vs-disability-scatter.png")

# %% [markdown]
# ---
#
# **Continue to** [`04_spatial_clustering.py`](04_spatial_clustering.py)
# — global Moran's I and the geographic comparison maps.
