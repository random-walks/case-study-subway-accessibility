# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

# %% [markdown]
# # 01 — Context & system-wide coverage
#
# **NYC subway ADA accessibility, April 2026.** This notebook sets the
# stage: the system snapshot, borough-level disparities, and the
# tract-level coverage map. Full prose context is in
# [`manuscripts/CASESTUDY_FULL.md`](../manuscripts/CASESTUDY_FULL.md)
# §1 (Introduction), §2 (Background), §3.1 (Data Sources), §4.1
# (System-Wide Coverage), §4.2 (Borough Disparities).
#
# Figures and tables here are rendered from the verbatim April 2026
# analysis output of the [`subway-access`](https://github.com/random-walks/subway-access)
# library; the underlying pipeline is preserved at
# [`manuscripts/UPSTREAM_REFERENCE.md`](../manuscripts/UPSTREAM_REFERENCE.md).

# %% tags=["jc.setup"]
# Imports that must be available to every cell, including re-executed cells
# whose neighbors were served from cache.
import jellycell.api as jc
from IPython.display import Image

# %% tags=["jc.load", "name=system_snapshot"]

snapshot = {
    "snapshot_date": "2026-04-09",
    "system_total_stations": 493,
    "ada_accessible_stations": 157,
    "ada_pct": 31.8,
    "tract_count": 2317,
    "uncovered_tract_count": 1416,
    "uncovered_tract_pct": 61.1,
    "uncovered_population": 4_717_140,
    "study_population": 8_507_596,
    "uncovered_pop_pct": 55.4,
    "catchment_meters": 800,
    "acs_vintage": "2023 5-year",
}
jc.save(
    snapshot,
    "artifacts/system_snapshot.json",
    caption="System-wide ADA coverage snapshot, April 2026",
    notes="55.4% of NYC residents live in tracts >800m from any ADA-accessible station.",
)
print(f"{snapshot['ada_accessible_stations']}/{snapshot['system_total_stations']} stations accessible ({snapshot['ada_pct']}%)")
print(f"{snapshot['uncovered_population']:,} / {snapshot['study_population']:,} residents in gap tracts ({snapshot['uncovered_pop_pct']}%)")

# %% [markdown]
# ## Borough disparities
#
# Coverage varies by an order of magnitude across boroughs — Manhattan
# at 77%, Staten Island at 9%. Queens carries the largest absolute gap
# population (1.75 M residents) despite having more stations than the
# Bronx; mean walking distance to the nearest accessible station spans
# from 584 m (Manhattan) to nearly 3 km (Staten Island).

# %% tags=["jc.step", "name=borough_table", "deps=system_snapshot"]
import pandas as pd

boroughs = pd.DataFrame(
    [
        ("Manhattan", 151, 61, 309, 238, 77, 361_154, 584),
        ("Brooklyn", 169, 43, 800, 326, 41, 1_467_660, 1007),
        ("Queens", 82, 26, 723, 159, 22, 1_752_073, 1966),
        ("Bronx", 70, 21, 360, 167, 46, 690_126, 980),
        ("Staten Island", 21, 6, 125, 11, 9, 446_127, 2983),
    ],
    columns=[
        "borough",
        "stations",
        "ada_stations",
        "tracts",
        "covered",
        "coverage_pct",
        "gap_population",
        "mean_distance_m",
    ],
)
jc.table(boroughs, name="borough_comparison", caption="Borough comparison: stations, ADA coverage, gap population")
print(boroughs.to_string(index=False))

# %% [markdown]
# ### Figure 1 — Coverage rate by borough

# %% tags=["jc.figure", "name=fig1_coverage_by_borough"]
Image("artifacts/figures/figure-1-coverage-by-borough.png")

# %% [markdown]
# ### Figure 2 — Absolute gap population by borough
#
# Queens dominates by population uncovered, despite having more stations
# than the Bronx. The geographic asymmetry — 82 stations across 283 km² —
# drives the gap.

# %% tags=["jc.figure", "name=fig2_gap_population"]
Image("artifacts/figures/figure-2-gap-population.png")

# %% [markdown]
# ### Figure 5 — Tract-level coverage choropleth
#
# Manhattan as an island of accessibility; outer-borough gaps as broad
# swaths. The pattern is the visual crux of the equity argument that
# follows in notebooks 03–04.

# %% tags=["jc.figure", "name=fig5_choropleth_coverage"]
Image("artifacts/figures/figure-5-choropleth-coverage-status.png")

# %% [markdown]
# ---
#
# **Continue to** [`02_reliability_and_gap_scores.py`](02_reliability_and_gap_scores.py)
# — what happens to coverage when we factor in actual elevator uptime.
