# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

# %% [markdown]
# # 03 — Cross-walk: upstream sections <-> factor-factory engines <-> portfolio topics
#
# The distinctive contribution of this showcase. For each numbered
# section of the upstream `subway-access` v0.5.0 CASESTUDY, we record:
#
# 1. Which `factor-factory` engine family implements (or could
#    implement) the same computation in the canonical framework.
# 2. Which blaise-website portfolio topic the section illustrates —
#    the lens through which other case studies reference this one.
#
# The table lives in `artifacts/cross_walk.json` as structured data
# and is re-emitted as a Markdown table via `jc.table` so it renders
# in the jellycell catalogue and in tearsheet exports.

# %% tags=["jc.load", "name=cross_walk_rows"]
import jellycell.api as jc

# Column semantics:
#   upstream_section   — section label in subway-access CASESTUDY.md
#   topic              — what the section computes / discusses
#   ff_engine          — factor_factory.engines.<family>.<method>
#                        ("-" when the section is descriptive rather
#                        than estimator-backed)
#   portfolio_topic    — blaise-website portfolio lens
ROWS = [
    {
        "upstream_section": "§3.1 Data sources",
        "topic": "MTA stations + ACS tracts + elevator uptime + tract geometries",
        "ff_engine": "-",
        "portfolio_topic": "Data provenance sidecars (see .claude/skills/data-provenance.md)",
    },
    {
        "upstream_section": "§3.2 Accessibility model",
        "topic": "800 m Euclidean catchment on tract centroids",
        "ff_engine": "nyc_geo_toolkit.catchment (spatial extra)",
        "portfolio_topic": "Walking-distance proxies and the network-distance upgrade path",
    },
    {
        "upstream_section": "§3.3 Need and gap scores",
        "topic": "Equal-weight composite of disability, senior, poverty rates",
        "ff_engine": "factor_factory.engines.inequality (composite indices)",
        "portfolio_topic": "Composite need indices and sensitivity to weighting",
    },
    {
        "upstream_section": "§3.4 Reliability-weighted coverage",
        "topic": "Discount nominal coverage by observed uptime fraction",
        "ff_engine": "factor_factory.tidy.Panel (reliability-weighted outcomes)",
        "portfolio_topic": "De jure vs. de facto service delivery",
    },
    {
        "upstream_section": "§3.5 DiD specification",
        "topic": "Twoway fixed-effects panel with tract + period effects",
        "ff_engine": "factor_factory.engines.did.twfe",
        "portfolio_topic": "Staggered rollout treatment effects",
    },
    {
        "upstream_section": "§3.5 DiD — staggered adoption robustness",
        "topic": "CS / SA / BJS heterogeneity-robust DiD estimators",
        "ff_engine": "factor_factory.engines.did.{callaway_santanna,sun_abraham,borusyak_jaravel_spiess}",
        "portfolio_topic": "Cross-estimator agreement as identification check",
    },
    {
        "upstream_section": "§3.5 SAR panel",
        "topic": "Spatial autoregressive extension of the DiD panel",
        "ff_engine": "factor_factory.engines.spatial.spatial_lag",
        "portfolio_topic": "Spatial spillovers and SUTVA violations",
    },
    {
        "upstream_section": "§3.6 Spatial analysis (weights matrix)",
        "topic": "Row-standardized 2 km distance-based weights over 2,317 tracts",
        "ff_engine": "factor_factory.engines.spatial._base (weights)",
        "portfolio_topic": "Spatial weights construction and sensitivity",
    },
    {
        "upstream_section": "§4.1 System-wide coverage",
        "topic": "Descriptive coverage counts, gap populations",
        "ff_engine": "-",
        "portfolio_topic": "Headline-number communication",
    },
    {
        "upstream_section": "§4.2 Borough disparities",
        "topic": "Stratified coverage + mean-distance-to-nearest by borough",
        "ff_engine": "factor_factory.engines.inequality.theil (between-borough decomposition)",
        "portfolio_topic": "Between-group vs. within-group inequality",
    },
    {
        "upstream_section": "§4.3 Reliability analysis",
        "topic": "Station uptime ranking; fragile-station surfacing",
        "ff_engine": "factor_factory.engines.changepoint.ruptures_adapter (uptime regime shifts)",
        "portfolio_topic": "Operational reliability as outcome",
    },
    {
        "upstream_section": "§4.4 Temporal progression",
        "topic": "Coverage share across 7 panel periods (2017-2023)",
        "ff_engine": "factor_factory.engines.stl.sktime_stl",
        "portfolio_topic": "Rollout curves and pre-trend inspection",
    },
    {
        "upstream_section": "§4.5 Treatment-control balance",
        "topic": "Welch's t-tests on pre-treatment covariates",
        "ff_engine": "factor_factory.engines.did._base (balance diagnostics)",
        "portfolio_topic": "Identifying assumptions — parallel trends, no anticipation",
    },
    {
        "upstream_section": "§4.6 Model diagnostics",
        "topic": "Jarque-Bera, skewness, kurtosis, distance-decay plots",
        "ff_engine": "-",
        "portfolio_topic": "Aggressive diagnostics (see .claude/skills/diagnostics-aggressive.md)",
    },
    {
        "upstream_section": "§4.7 OLS equity regression",
        "topic": "Gap score ~ disability + senior + poverty (HC1 SE, VIF)",
        "ff_engine": "factor_factory.engines.panel_reg.pyfixest_adapter",
        "portfolio_topic": "Vertical equity quantified",
    },
    {
        "upstream_section": "§4.8 Moran's I",
        "topic": "Global spatial autocorrelation on gap, need, disability",
        "ff_engine": "factor_factory.engines.spatial.morans_i",
        "portfolio_topic": "Spatial autocorrelation as clustering evidence",
    },
    {
        "upstream_section": "§5 Discussion",
        "topic": "Limitations, policy implications, future research",
        "ff_engine": "-",
        "portfolio_topic": "Honest limitations (see .claude/skills/paper-cadence.md §5.3)",
    },
    {
        "upstream_section": "Appendix D — engine audit",
        "topic": "factor-factory engine cross-check of primary results",
        "ff_engine": "factor_factory.engines.{panel_reg,spatial,did}",
        "portfolio_topic": "Engine-audit-as-appendix pattern (directional agreement as check)",
    },
]

jc.save(
    {"n_rows": len(ROWS), "rows": ROWS},
    "artifacts/cross_walk.json",
    caption=(
        f"Cross-walk: {len(ROWS)} rows mapping subway-access CASESTUDY "
        "sections to factor-factory engine families and blaise-website "
        "portfolio topics."
    ),
    tags=["tearsheet"],
)

# %% tags=["jc.table", "name=cross_walk_table", "deps=cross_walk_rows", "tearsheet"]
import jellycell.api as jc
import pandas as pd

# Rehydrate from JSON to decouple from cell order (jc.load by name
# would work too; reading via in-memory list keeps the notebook
# runnable cell-by-cell).
rows = [
    {
        "upstream_section": "§3.1 Data sources",
        "topic": "MTA stations + ACS tracts + elevator uptime + tract geometries",
        "ff_engine": "-",
        "portfolio_topic": "Data provenance sidecars",
    },
    {
        "upstream_section": "§3.2 Accessibility model",
        "topic": "800 m Euclidean catchment on tract centroids",
        "ff_engine": "nyc_geo_toolkit.catchment",
        "portfolio_topic": "Walking-distance proxies; network-distance upgrade",
    },
    {
        "upstream_section": "§3.3 Need and gap scores",
        "topic": "Equal-weight composite of disability, senior, poverty",
        "ff_engine": "factor_factory.engines.inequality",
        "portfolio_topic": "Composite need indices",
    },
    {
        "upstream_section": "§3.4 Reliability-weighted coverage",
        "topic": "Uptime-discounted nominal coverage",
        "ff_engine": "factor_factory.tidy.Panel",
        "portfolio_topic": "De jure vs. de facto service delivery",
    },
    {
        "upstream_section": "§3.5 DiD specification",
        "topic": "Twoway FE panel (tract + period)",
        "ff_engine": "factor_factory.engines.did.twfe",
        "portfolio_topic": "Staggered rollout treatment effects",
    },
    {
        "upstream_section": "§3.5 DiD — heterogeneity-robust",
        "topic": "CS / SA / BJS estimators",
        "ff_engine": "factor_factory.engines.did.{cs,sa,bjs}",
        "portfolio_topic": "Cross-estimator agreement as ID check",
    },
    {
        "upstream_section": "§3.5 SAR panel",
        "topic": "Spatial autoregressive DiD extension",
        "ff_engine": "factor_factory.engines.spatial.spatial_lag",
        "portfolio_topic": "Spatial spillovers; SUTVA",
    },
    {
        "upstream_section": "§3.6 Weights matrix",
        "topic": "Row-standardized 2 km distance weights",
        "ff_engine": "factor_factory.engines.spatial._base",
        "portfolio_topic": "Spatial weights construction + sensitivity",
    },
    {
        "upstream_section": "§4.1 System-wide coverage",
        "topic": "Descriptive coverage counts",
        "ff_engine": "-",
        "portfolio_topic": "Headline-number communication",
    },
    {
        "upstream_section": "§4.2 Borough disparities",
        "topic": "Stratified coverage + distance by borough",
        "ff_engine": "factor_factory.engines.inequality.theil",
        "portfolio_topic": "Between- vs. within-group inequality",
    },
    {
        "upstream_section": "§4.3 Reliability analysis",
        "topic": "Station uptime ranking; fragile-station surfacing",
        "ff_engine": "factor_factory.engines.changepoint.ruptures_adapter",
        "portfolio_topic": "Operational reliability as outcome",
    },
    {
        "upstream_section": "§4.4 Temporal progression",
        "topic": "Coverage share across 7 periods (2017-2023)",
        "ff_engine": "factor_factory.engines.stl.sktime_stl",
        "portfolio_topic": "Rollout curves + pre-trend inspection",
    },
    {
        "upstream_section": "§4.5 Treatment-control balance",
        "topic": "Welch's t-tests on pre-treatment covariates",
        "ff_engine": "factor_factory.engines.did._base",
        "portfolio_topic": "Parallel trends; no anticipation",
    },
    {
        "upstream_section": "§4.6 Model diagnostics",
        "topic": "JB, skewness, kurtosis; distance-decay plots",
        "ff_engine": "-",
        "portfolio_topic": "Aggressive diagnostics",
    },
    {
        "upstream_section": "§4.7 OLS equity regression",
        "topic": "Gap ~ disability + senior + poverty (HC1, VIF)",
        "ff_engine": "factor_factory.engines.panel_reg.pyfixest_adapter",
        "portfolio_topic": "Vertical equity quantified",
    },
    {
        "upstream_section": "§4.8 Moran's I",
        "topic": "Global spatial autocorrelation",
        "ff_engine": "factor_factory.engines.spatial.morans_i",
        "portfolio_topic": "Spatial autocorrelation as clustering evidence",
    },
    {
        "upstream_section": "§5 Discussion",
        "topic": "Limitations; policy; future research",
        "ff_engine": "-",
        "portfolio_topic": "Honest limitations",
    },
    {
        "upstream_section": "Appendix D — engine audit",
        "topic": "factor-factory cross-check of primary results",
        "ff_engine": "factor_factory.engines.{panel_reg,spatial,did}",
        "portfolio_topic": "Engine-audit-as-appendix pattern",
    },
]
df = pd.DataFrame(rows, columns=[
    "upstream_section", "topic", "ff_engine", "portfolio_topic",
])
jc.table(
    df,
    name="cross_walk_table",
    caption=(
        "Cross-walk from subway-access v0.5.0 CASESTUDY sections to "
        "factor-factory engine families and blaise-website portfolio "
        "topics."
    ),
    notes=(
        "Dash (-) in ff_engine marks descriptive sections not backed "
        "by a dedicated estimator. The Appendix D row summarizes the "
        "upstream engine-audit cross-check pattern."
    ),
)

# %% [markdown]
# ## How to read this table
#
# - **`upstream_section`** is the authoritative pointer. For the actual
#   numbers, equations, and prose, open `docs/CASESTUDY.md` in the
#   `random-walks/subway-access` repo.
# - **`ff_engine`** indicates the `factor-factory` 1.0 engine family
#   that owns the canonical implementation within our ecosystem. When
#   the upstream analysis uses a hand-rolled function, this column
#   names the engine that would replace it in an engine-audit
#   Appendix.
# - **`portfolio_topic`** is the lens through which other blaise-website
#   showcases (rat-containerization, resolution-equity) reference this
#   one. It lets a reader browsing the portfolio jump between case
#   studies that share a methodological concern.
