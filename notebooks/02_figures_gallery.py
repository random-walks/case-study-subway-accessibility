# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

# %% [markdown]
# # 02 — Figures gallery
#
# The 15 figures from the upstream CASESTUDY, inlined via
# `IPython.display.Image` as static images so the gallery renders
# portably in any notebook viewer. The PNGs are committed as regular
# git binaries under `artifacts/figures/`, with their full commit
# history carried in this repository.
#
# Captions summarize what each figure shows; the full methodological
# context lives in §2–§4 of the upstream CASESTUDY.

# %% tags=["jc.figure", "name=fig1_coverage_by_borough", "tearsheet"]
from IPython.display import Image
Image("artifacts/figures/figure-1-coverage-by-borough.png")
# Figure 1: Tract-level ADA coverage rate by borough. Manhattan 77%,
# Brooklyn 41%, Bronx 46%, Queens 22%, Staten Island 9%. See §4.2.

# %% tags=["jc.figure", "name=fig2_gap_population", "tearsheet"]
from IPython.display import Image
Image("artifacts/figures/figure-2-gap-population.png")
# Figure 2: Gap population by borough — residents in tracts without an
# ADA station within 800 m. Queens carries the largest absolute gap
# (1,752,073). See §4.2.

# %% tags=["jc.figure", "name=fig3_reliability_nominal_vs_effective", "tearsheet"]
from IPython.display import Image
Image("artifacts/figures/figure-3-reliability-nominal-vs-effective.png")
# Figure 3: Nominal vs. elevator-uptime-weighted coverage. Manhattan
# drops 77% -> 71% when the 12-month May 2025-April 2026 uptime
# window is applied. See §4.3.

# %% tags=["jc.figure", "name=fig4_choropleth_gap_score", "tearsheet"]
from IPython.display import Image
Image("artifacts/figures/figure-4-choropleth-gap-score.png")
# Figure 4: Choropleth of tract-level gap score (mean of disability,
# senior, poverty rates for uncovered tracts; zero for covered). High-
# gap corridors cluster visibly in southeast Queens, central
# Brooklyn, and northern Bronx. See §4.1, §4.8.

# %% tags=["jc.figure", "name=fig5_choropleth_coverage_status", "tearsheet"]
from IPython.display import Image
Image("artifacts/figures/figure-5-choropleth-coverage-status.png")
# Figure 5: Tract coverage status (binary). Manhattan appears as an
# island of coverage surrounded by outer-borough inaccessibility.
# See §4.1.

# %% tags=["jc.figure", "name=fig6_coverage_progression", "tearsheet"]
from IPython.display import Image
Image("artifacts/figures/figure-6-coverage-progression.png")
# Figure 6: Coverage progression 2017-2023 across the 7-period panel.
# 16.8% -> 35.9% of tracts, 1.62M -> 3.52M residents. See §4.4.

# %% tags=["jc.figure", "name=fig7_treatment_vs_control_balance", "tearsheet"]
from IPython.display import Image
Image("artifacts/figures/figure-7-treatment-vs-control-balance.png")
# Figure 7: Treatment (n=831) vs. control (n=1,486) balance on
# disability, senior, and poverty rates. Welch's t-tests show small
# but significant imbalances; DiD with fixed effects is required to
# absorb baseline differences. See §4.5.

# %% tags=["jc.figure", "name=fig8_need_score_distribution", "tearsheet"]
from IPython.display import Image
Image("artifacts/figures/figure-8-need-score-distribution.png")
# Figure 8: Need score distribution across 2,317 tracts. Moderate
# right skew (0.73) and mild leptokurtosis; Jarque-Bera rejects
# normality but CLT handles inference at this N. See §4.6.

# %% tags=["jc.figure", "name=fig9_distance_decay", "tearsheet"]
from IPython.display import Image
Image("artifacts/figures/figure-9-distance-decay.png")
# Figure 9: Distance-decay curve validating the 800 m catchment.
# Coverage is near-total within 800 m and drops sharply beyond it.
# See §4.6.

# %% tags=["jc.figure", "name=fig10_gap_vs_distance_scatter", "tearsheet"]
from IPython.display import Image
Image("artifacts/figures/figure-10-gap-vs-distance-scatter.png")
# Figure 10: Gap score vs. distance to nearest ADA station. High-
# population tracts appear at every distance range; Pearson r = .42,
# p < .001. See §4.7.

# %% tags=["jc.figure", "name=fig11_correlation_heatmap", "tearsheet"]
from IPython.display import Image
Image("artifacts/figures/figure-11-correlation-heatmap.png")
# Figure 11: Pearson/Spearman correlation matrix across demographic
# and accessibility variables. Disability and poverty rates correlate
# strongly (r = .70), driving the VIF pattern in the equity
# regression. See §4.7.

# %% tags=["jc.figure", "name=fig12_gap_vs_poverty_scatter", "tearsheet"]
from IPython.display import Image
Image("artifacts/figures/figure-12-gap-vs-poverty-scatter.png")
# Figure 12: Gap score vs. poverty rate scatter. Poverty is a
# significant OLS predictor (b = .164, t = 4.99, p < .001). See §4.7.

# %% tags=["jc.figure", "name=fig13_gap_vs_disability_scatter", "tearsheet"]
from IPython.display import Image
Image("artifacts/figures/figure-13-gap-vs-disability-scatter.png")
# Figure 13: Gap score vs. disability rate scatter. Disability is not
# significant in the multivariate OLS (t = 0.21) due to collinearity
# with poverty — the shared variance is absorbed. See §4.7.

# %% tags=["jc.figure", "name=fig14_gap_vs_poverty_map", "tearsheet"]
from IPython.display import Image
Image("artifacts/figures/figure-14-gap-vs-poverty-map.png")
# Figure 14: Side-by-side choropleth of gap score and poverty rate.
# Visual confirmation that high-poverty tracts overlap spatially with
# high-gap-score tracts. See §4.8.

# %% tags=["jc.figure", "name=fig15_gap_vs_disability_map", "tearsheet"]
from IPython.display import Image
Image("artifacts/figures/figure-15-gap-vs-disability-map.png")
# Figure 15: Side-by-side choropleth of gap score and disability
# rate. High-disability tracts overlap with high-gap-score tracts;
# Moran's I = .28 for disability confirms clustering. See §4.8.

# %% [markdown]
# ## Figure inventory summary
#
# All 15 figures from the April 2026 upstream vintage are inlined
# above, committed as regular git binaries so a checkout renders the
# gallery with no extra tooling. See notebook 03 for the engine
# cross-walk that ties each figure to a `factor-factory` engine family.
