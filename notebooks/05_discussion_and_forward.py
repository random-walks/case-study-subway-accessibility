# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

# %% [markdown]
# # 05 — Discussion, limitations, policy
#
# This notebook is pure prose — a navigable summary of §5 of the case
# study. Full text in
# [`manuscripts/CASESTUDY_FULL.md`](../manuscripts/CASESTUDY_FULL.md).

# %% tags=["jc.load", "name=summary_findings"]
import jellycell.api as jc

findings = {
    "headline": (
        "4,717,140 New Yorkers (55.4% of the study population) live in "
        "tracts with no ADA-accessible subway station within 800 m."
    ),
    "queens_gap_population": 1_752_073,
    "manhattan_nominal_coverage_pct": 77,
    "manhattan_effective_coverage_pct": 71,
    "system_full_accessibility_eta_at_current_pace": "mid-2050s",
    "settlement_target_2055": "95% of stations",
}
jc.save(findings, "artifacts/summary_findings.json", caption="Summary findings + headline numbers")
print(findings["headline"])

# %% [markdown]
# ## 5.1 Summary of findings
#
# - **4,717,140 New Yorkers** — more than the population of Los Angeles
#   — live in tracts with no ADA-accessible station within a 10-minute walk.
# - **Queens carries the largest absolute gap** (1.75M residents);
#   **Staten Island** has the lowest coverage rate (9%) but smaller absolute
#   gap.
# - **Manhattan, the best-covered borough at 77% nominal**, drops to **71%
#   effective** when reliability-weighted — capital investment without
#   matching elevator-maintenance investment produces the gap between
#   official accessibility statistics and lived experience.
# - **Senior rate** is the strongest demographic predictor of gap score
#   (β = 0.263, t = 15.93). Disability rate is collinear with poverty
#   (r = .70), so its coefficient is statistically washed out despite
#   the strong bivariate signal.
# - **Spatial clustering is significant** for all three variables
#   (Moran's I = .20–.28, p < .001). Gaps form identifiable corridors,
#   not random scatter — geographically targeted investment would yield
#   greater coverage gains per dollar than spatially uniform upgrades.

# %% [markdown]
# ## 5.3 Limitations (the honest list)
#
# - **Euclidean catchment overstates coverage.** Street network detours,
#   elevation, sidewalk infrastructure not modeled. Estimates are upper bounds.
# - **ACS data are stale.** 2023 5-year estimates reflect 2019–2023 surveys;
#   post-pandemic shifts in disability/poverty/mobility likely changed the
#   spatial distribution of need.
# - **Upgrade timeline is partially approximate.** 101/157 stations have
#   sourced dates from MTA/press records; 56 use deterministic hash-based
#   fallback dates pending a FOIL request for Key Station Program records.
# - **Panel lacks an outcome variable.** Treatment indicators + covariates
#   only; defining and linking outcomes is prerequisite for DiD estimation.
# - **800m may be too generous for the target population.** Mobility-impaired
#   individuals likely have shorter effective walking radius. Sensitivity
#   analysis at 400m and 600m would tighten estimates.
# - **OLS standard errors likely underestimated** due to spatial dependence
#   (Moran's I significant for all variables). Spatial HAC SE or SAR model
#   would be more reliable for inference.

# %% [markdown]
# ## 5.4 Policy implications for 2026
#
# - **Congestion pricing equity logic depends on transit substitutability.**
#   The Manhattan congestion pricing program (June 2024 launch, $9 peak toll)
#   assumes drivers shift to transit — an assumption that fails for ~68% of
#   stations a wheelchair user cannot use.
# - **Current capital pace projects full accessibility in the mid-2050s.**
#   The MTA's 2020–2024 Capital Program at 67 stations / 5 years is
#   historically unprecedented but still yields a multi-decade timeline.
# - **2022 settlement target: 95% accessibility by 2055** — at risk given
#   the elevator reliability data showing existing upgrades aren't being
#   maintained at functional levels.
# - **Geographic targeting > uniform investment.** Moran's I results
#   identify the corridors (southeastern Queens, central Brooklyn, northern
#   Bronx) where targeted upgrades would yield the most equity per dollar.

# %% [markdown]
# ## 5.5 Future research
#
# 1. **Network distance** — replace Euclidean with OSMnx street-network walking distances
# 2. **Complete upgrade dates** — FOIL request for Key Station Program records
# 3. **Multi-vintage ACS** — temporal variation in demographic covariates
# 4. **Local indicators (LISA)** — identify specific hot/cold spots at tract level
# 5. **Geographically weighted regression (GWR)** — spatially varying coefficients
# 6. **Outcome variables** — link panel to ridership / property values / population change for true DiD
# 7. **First-and-last-mile** — incorporate curb cuts, sidewalk condition, pedestrian infrastructure
#
# ---
#
# **End of showcase.** Full prose, references, and appendices in
# [`manuscripts/CASESTUDY_FULL.md`](../manuscripts/CASESTUDY_FULL.md).
# Reproducibility / regeneration via the upstream
# [`subway-access`](https://github.com/random-walks/subway-access) library —
# see [`manuscripts/UPSTREAM_REFERENCE.md`](../manuscripts/UPSTREAM_REFERENCE.md).
