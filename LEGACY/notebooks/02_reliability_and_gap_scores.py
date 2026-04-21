# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

# %% [markdown]
# # 02 — Reliability & gap scores
#
# Nominal ADA designation does not guarantee functional access. Of the
# 157 accessible stations, 49 operated below 95% elevator uptime over
# the May 2025–April 2026 observation window. This notebook covers the
# accessibility model (§3.2), need/gap score construction (§3.3),
# reliability weighting (§3.4), and the reliability analysis results
# (§4.3) plus distance-decay validation (§4.6).

# %% tags=["jc.setup"]
import jellycell.api as jc
import pandas as pd
from IPython.display import Image

# %% tags=["jc.load", "name=fragile_stations"]

# The five most fragile stations — selected from the larger sample of
# 49 stations operating below 95% uptime. Source: MTA E&E availability
# records, 12-month rolling window May 2025 – April 2026.
fragile = pd.DataFrame(
    [
        ("59 St-Columbus Circle", 0.0),
        ("Lexington Av/53 St", 9.3),
        ("42 St-Port Authority Bus Terminal", 13.6),
        ("34 St-Hudson Yards", 32.8),
        ("34 St-Herald Square", 51.3),
    ],
    columns=["station", "uptime_pct"],
)
jc.table(
    fragile,
    name="most_fragile_stations",
    caption="Most fragile ADA stations — 12-month elevator uptime <60%",
    notes="49 of 157 ADA stations operated below 95% uptime over the window.",
)
print(fragile.to_string(index=False))

# %% tags=["jc.step", "name=reliability_summary", "deps=fragile_stations"]
reliability = {
    "ada_stations_total": 157,
    "below_95pct_uptime": 49,
    "below_95pct_pct": round(49 / 157 * 100, 1),
    "manhattan_coverage_nominal_pct": 77,
    "manhattan_coverage_effective_pct": 71,
    "reliability_drop_pp": 6,
    "observation_window": "2025-05 to 2026-04",
}
jc.save(
    reliability,
    "artifacts/reliability_summary.json",
    caption="Reliability-weighted coverage drop, Manhattan",
    notes="Manhattan loses 6 percentage points of effective coverage due to elevator downtime.",
)
print(f"{reliability['below_95pct_uptime']}/{reliability['ada_stations_total']} stations <95% uptime ({reliability['below_95pct_pct']}%)")
print(f"Manhattan coverage: {reliability['manhattan_coverage_nominal_pct']}% nominal → {reliability['manhattan_coverage_effective_pct']}% effective")

# %% [markdown]
# ## The need / gap score model
#
# Each tract receives a **composite need score** — the unweighted mean
# of disability rate, senior rate, and poverty rate. The **gap score**
# operationalizes unmet need: for uncovered tracts, gap score = need
# score; for covered tracts, gap score = 0. Highest gap scores
# concentrate where vulnerability stacks (disability + age + poverty)
# *and* coverage is absent.
#
# ```
# NeedScore_i = (disability_rate_i + senior_rate_i + poverty_rate_i) / 3
# GapScore_i  = NeedScore_i × (1 − Covered_i)
# ```

# %% [markdown]
# ### Figure 3 — Reliability: nominal vs. effective coverage
#
# The bar pair shows what happens to nominal "ADA-accessible" coverage
# when discounted by 12-month elevator uptime. The system-wide drop is
# modest in percentage points but concentrated at high-ridership stations.

# %% tags=["jc.figure", "name=fig3_reliability"]
Image("artifacts/figures/figure-3-reliability-nominal-vs-effective.png")

# %% [markdown]
# ### Figure 8 — Need score distribution
#
# Right-skewed with moderate kurtosis; the bulk of tracts cluster around
# the median (8.5%) but a long tail of high-need tracts drives the equity
# argument.

# %% tags=["jc.figure", "name=fig8_need_distribution"]
Image("artifacts/figures/figure-8-need-score-distribution.png")

# %% [markdown]
# ### Figure 9 — Distance-decay: validation of the 800 m catchment
#
# Coverage is near-total within 800 m and drops sharply beyond it,
# confirming the empirical break that justifies the 800 m threshold.

# %% tags=["jc.figure", "name=fig9_distance_decay"]
Image("artifacts/figures/figure-9-distance-decay.png")

# %% [markdown]
# ### Figure 10 — Gap × distance scatter
#
# High-population tracts appear at every distance range, not only the
# urban periphery — a systemic problem affecting the urban core.

# %% tags=["jc.figure", "name=fig10_gap_vs_distance"]
Image("artifacts/figures/figure-10-gap-vs-distance-scatter.png")

# %% [markdown]
# ---
#
# **Continue to** [`03_temporal_and_equity.py`](03_temporal_and_equity.py)
# — DiD panel construction and the OLS equity regression.
