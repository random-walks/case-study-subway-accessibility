# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

# %% [markdown]
# # 01 — Context and pointer
#
# This case study is a **thin portfolio wrapper** around the canonical
# [`subway-access` v0.5.1 CASESTUDY](https://github.com/random-walks/subway-access/blob/main/examples/accessibility-change-over-time/CASESTUDY.md).
# The upstream library owns the live pipeline — fetching MTA Socrata
# endpoints, joining ACS 5-year estimates, computing 800 m catchments,
# fitting the OLS and Moran's *I* models, and emitting the 15 figures
# and the engine-audit appendix.
#
# What this repo adds is a **portfolio-specific lens**:
#
# 1. A browsable gallery of the 15 committed figures (notebook 02).
# 2. A cross-walk table mapping each CASESTUDY section to a
#    `factor-factory` engine family and the broader portfolio topic it
#    illustrates (notebook 03).
# 3. A short 1,000-word framing manuscript pointing at the upstream
#    source of truth (`manuscripts/MANUSCRIPT.md`).
#
# **We do not re-run the upstream pipeline here.** The 15 figures are
# pre-rendered snapshots committed as regular git binaries; regenerating requires
# cloning `random-walks/subway-access` and running the upstream
# example. See `manuscripts/UPSTREAM_REFERENCE.md` for the exact
# commands.
#
# Note: imports are inlined in every cell (no `jc.setup`), and figures
# are rendered as static images via `IPython.display.Image` so the
# gallery stays portable across notebook viewers.

# %% tags=["jc.load", "name=headline_numbers"]
import jellycell.api as jc
import subway_access

# The upstream package ships with the CASESTUDY and engine-audit
# appendix. We pin to >=0.5,<0.6 in pyproject.toml so these numbers
# stay locked to the upstream April 2026 vintage.
headline = {
    "upstream_package": "subway-access",
    "upstream_version": subway_access.__version__,
    "study_vintage": "April 2026",
    "n_stations_total": 493,
    "n_stations_ada": 157,
    "pct_stations_ada": 31.8,
    "n_tracts_analyzed": 2_317,
    "study_population": 8_507_596,
    "gap_population": 4_717_140,
    "gap_population_pct": 55.4,
    "n_figures_mirrored": 15,
    "ols_r_squared": 0.202,
    "ols_f_stat": 108.83,
    "ols_df_model": 3,
    "ols_df_resid": 2_313,
    "morans_i_gap": 0.2271,
    "morans_i_gap_z": 40.87,
    "n_stations_below_95pct_uptime": 49,
    "manhattan_coverage_nominal": 0.77,
    "manhattan_coverage_effective": 0.71,
}
jc.save(
    headline,
    "artifacts/headline_numbers.json",
    caption=(
        f"Headline numbers mirrored from subway-access v{subway_access.__version__} "
        "CASESTUDY (April 2026 vintage)."
    ),
    notes=(
        "Numbers are not recomputed here; they index the upstream "
        "analysis for portfolio browsing. See manuscripts/UPSTREAM_REFERENCE.md "
        "to regenerate against a later MTA/ACS vintage."
    ),
    tags=["tearsheet"],
)

# %% [markdown]
# ## Pointer to the canonical analysis
#
# - **Library**: [`random-walks/subway-access`](https://github.com/random-walks/subway-access) — typed
#   Python toolkit for reproducible NYC subway accessibility analysis.
# - **CASESTUDY**: `examples/accessibility-change-over-time/CASESTUDY.md`
#   in the upstream repo — abstract, §1–§5, Appendix D (factor-factory
#   engine audit).
# - **Example pipeline**: `examples/accessibility-change-over-time/main.py`
#   in the upstream repo. Running it produces the 15 figures committed here.
# - **Data provenance caveat**: 56 of 157 ADA station upgrade years use
#   a deterministic hash-based fallback pending a FOIL request to the
#   MTA Key Station Program — see §3.5 of the upstream CASESTUDY.
#
# The cross-walk (notebook 03) gives the structured map from upstream
# sections to portfolio-relevant engine families.
