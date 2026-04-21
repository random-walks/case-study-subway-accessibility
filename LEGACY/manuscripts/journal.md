# showcase-subway-accessibility — analysis journal

Append-only run log written by `jellycell run`. Each section below is
one invocation: timestamp, notebook, cell-change summary, and any new
or updated artifacts. Safe to hand-edit for commentary — the next
`jellycell run` only appends at the bottom.

Disable via `[journal] enabled = false` in `jellycell.toml`.

## 2026-04-19T07:41:25+00:00 — `notebooks/01_context_and_coverage.py`

> **Status:** error · 1 ran · 0 cached · 1 errored · 1598ms

**Artifacts:**
- `artifacts/system_snapshot.json` (361 B) — System-wide ADA coverage snapshot, April 2026

**Errors:**
- `01_context_and_coverage:3 (borough_table)` — ImportError: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - `Import pyarrow` failed. pyarrow is required for parquet support. Use pip or conda to install the pyarrow package.
 - `Import fastparquet` failed. fastparquet is required for parquet support. Use pip or conda to install the fastparquet package.

## 2026-04-19T07:41:26+00:00 — `notebooks/02_reliability_and_gap_scores.py`

> **Status:** error · 0 ran · 0 cached · 1 errored · 1082ms

**Errors:**
- `02_reliability_and_gap_scores:1 (fragile_stations)` — ImportError: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - `Import pyarrow` failed. pyarrow is required for parquet support. Use pip or conda to install the pyarrow package.
 - `Import fastparquet` failed. fastparquet is required for parquet support. Use pip or conda to install the fastparquet package.

## 2026-04-19T07:41:28+00:00 — `notebooks/03_temporal_and_equity.py`

> **Status:** error · 1 ran · 0 cached · 1 errored · 1104ms

**Artifacts:**
- `artifacts/panel_summary.json` (341 B) — Temporal panel construction summary

**Errors:**
- `03_temporal_and_equity:3 (balance_table)` — ImportError: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - `Import pyarrow` failed. pyarrow is required for parquet support. Use pip or conda to install the pyarrow package.
 - `Import fastparquet` failed. fastparquet is required for parquet support. Use pip or conda to install the fastparquet package.

## 2026-04-19T07:41:29+00:00 — `notebooks/04_spatial_clustering.py`

> **Status:** error · 0 ran · 0 cached · 1 errored · 1079ms

**Errors:**
- `04_spatial_clustering:1 (morans_i_table)` — ImportError: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - `Import pyarrow` failed. pyarrow is required for parquet support. Use pip or conda to install the pyarrow package.
 - `Import fastparquet` failed. fastparquet is required for parquet support. Use pip or conda to install the fastparquet package.

## 2026-04-19T07:41:31+00:00 — `notebooks/05_discussion_and_forward.py`

> **Status:** ok · 1 ran · 0 cached · 0 errored · 880ms

**Artifacts:**
- `artifacts/summary_findings.json` (369 B) — Summary findings + headline numbers

## 2026-04-19T07:41:52+00:00 — `notebooks/01_context_and_coverage.py`

> **Status:** ok · 4 ran · 1 cached · 0 errored · 2990ms

**Artifacts:**
- `artifacts/borough_comparison.parquet` (5.8 KB) — Borough comparison: stations, ADA coverage, gap population

## 2026-04-19T07:41:53+00:00 — `notebooks/02_reliability_and_gap_scores.py`

> **Status:** ok · 6 ran · 0 cached · 0 errored · 1035ms

**Artifacts:**
- `artifacts/most_fragile_stations.parquet` (2.3 KB) — Most fragile ADA stations — 12-month elevator uptime <60%
- `artifacts/reliability_summary.json` (242 B) — Reliability-weighted coverage drop, Manhattan

## 2026-04-19T07:41:55+00:00 — `notebooks/03_temporal_and_equity.py`

> **Status:** error · 3 ran · 1 cached · 1 errored · 1192ms

**Artifacts:**
- `artifacts/treatment_control_balance.parquet` (5.5 KB) — Welch's t-test: treatment vs. control tracts on demographic predictors

**Errors:**
- `03_temporal_and_equity:9 (ols_regression)` — ArrowInvalid: ("Could not convert '<.001' with type str: tried to convert to double", 'Conversion failed for column p with type object')

## 2026-04-19T07:41:57+00:00 — `notebooks/04_spatial_clustering.py`

> **Status:** ok · 5 ran · 0 cached · 0 errored · 1145ms

**Artifacts:**
- `artifacts/global_morans_i.parquet` (4.1 KB) — Global Moran's I for gap, need, disability — 2 km row-standardized weights
- `artifacts/spatial_summary.json` (432 B) — Spatial weights and clustering summary

## 2026-04-19T07:42:15+00:00 — `notebooks/03_temporal_and_equity.py`

> **Status:** error · 2 ran · 3 cached · 1 errored · 1063ms

**Artifacts:**
- `artifacts/treatment_control_balance.parquet` (5.5 KB) — Welch's t-test: treatment vs. control tracts on demographic predictors
- `artifacts/ols_gap_on_demographics.parquet` (4.1 KB) — OLS: gap score on demographic predictors (HC1 robust SE)
- `artifacts/ols_summary.json` (278 B) — OLS regression summary statistics

**Errors:**
- `03_temporal_and_equity:11 (fig11_correlation)` — NameError: name 'Image' is not defined

## 2026-04-19T07:43:01+00:00 — `notebooks/01_context_and_coverage.py`

> **Status:** ok · 6 ran · 0 cached · 0 errored · 1029ms

**Artifacts:**
- `artifacts/system_snapshot.json` (361 B) — System-wide ADA coverage snapshot, April 2026
- `artifacts/borough_comparison.parquet` (5.8 KB) — Borough comparison: stations, ADA coverage, gap population

## 2026-04-19T07:43:03+00:00 — `notebooks/02_reliability_and_gap_scores.py`

> **Status:** ok · 7 ran · 0 cached · 0 errored · 1029ms

**Artifacts:**
- `artifacts/most_fragile_stations.parquet` (2.3 KB) — Most fragile ADA stations — 12-month elevator uptime <60%
- `artifacts/reliability_summary.json` (242 B) — Reliability-weighted coverage drop, Manhattan

## 2026-04-19T07:43:04+00:00 — `notebooks/03_temporal_and_equity.py`

> **Status:** ok · 9 ran · 0 cached · 0 errored · 1033ms

**Artifacts:**
- `artifacts/panel_summary.json` (341 B) — Temporal panel construction summary
- `artifacts/treatment_control_balance.parquet` (5.5 KB) — Welch's t-test: treatment vs. control tracts on demographic predictors
- `artifacts/ols_gap_on_demographics.parquet` (4.1 KB) — OLS: gap score on demographic predictors (HC1 robust SE)
- `artifacts/ols_summary.json` (278 B) — OLS regression summary statistics

## 2026-04-19T07:43:06+00:00 — `notebooks/04_spatial_clustering.py`

> **Status:** ok · 6 ran · 0 cached · 0 errored · 1085ms

**Artifacts:**
- `artifacts/global_morans_i.parquet` (4.1 KB) — Global Moran's I for gap, need, disability — 2 km row-standardized weights
- `artifacts/spatial_summary.json` (432 B) — Spatial weights and clustering summary

## 2026-04-19T07:43:07+00:00 — `notebooks/05_discussion_and_forward.py`

> **Status:** ok · 1 ran · 0 cached · 0 errored · 819ms

**Artifacts:**
- `artifacts/summary_findings.json` (369 B) — Summary findings + headline numbers
