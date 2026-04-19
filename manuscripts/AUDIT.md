# Audit — subway-accessibility showcase

A statistical / methodological audit. This showcase is a *verbatim
mirror* of the April 2026 NYC subway ADA accessibility analysis from
`subway-access` — figures, prose, supplementary docs all preserved.
The audit's scope is therefore narrower than for the 311 showcases:
"is the mirror faithful + complete?" rather than "is the analysis
correct?" (the underlying analysis lives upstream and was peer-style
authored by Blaise).

---

## What's strong

- **Verbatim preservation** of the 48 KB CASESTUDY.md, 15 figures,
  and 3 supplementary methodology docs. Reviewers can read the same
  document the upstream analysis published.
- **Five focused notebooks** navigate the analytical arc (system
  snapshot → reliability → temporal/equity → spatial → discussion)
  without re-running anything — each notebook is essentially a
  guided tour with cross-links to the full manuscript.
- **Headline numbers extracted to JSON artifacts** (system snapshot,
  reliability summary, OLS regression output, Moran's I table) —
  every number cited in the prose has a machine-readable source.
- **Per-notebook tearsheets** under `manuscripts/tearsheets/` — five
  of them, regenerable via `jellycell export tearsheet`.
- **`UPSTREAM_REFERENCE.md`** — explicit pointer back to
  `subway-access/examples/accessibility-change-over-time/` for anyone
  who wants to regenerate the figures against a fresh data pull.

## What's gappy (in the mirror, not the underlying analysis)

- **No dynamic re-run path.** The mirror ships pre-rendered PNGs;
  there's no way to re-run a figure against fresh MTA data without
  going upstream. For a static archive that's fine — for a "live
  showcase" it's a limitation. Could be addressed by importing
  `subway_access` (the upstream package) and re-running the figure
  pipeline inside notebook 02 + 03 + 04 as a subprocess + data-fetch
  flag, similar to how `RESOLUTION_EQUITY_LIVE_FETCH=1` works in the
  resolution-equity showcase.
- **No analytical extensions.** The original case study is a finished
  piece; we didn't add fresh analysis. If we wanted to, the obvious
  extensions would be: (a) replacing Euclidean catchments with
  network-distance catchments via OSMnx, (b) extending the temporal
  panel with a real outcome variable so the DiD framework actually
  estimates β, (c) adding Local Indicators of Spatial Association
  (LISA) to the global Moran's I.

## What I'd want for a "proper paper" version

The underlying case study is already structured like a paper. The
mirror's job is to make it browsable, which it does. If we wanted to
upgrade *this* (the showcase), not the upstream paper:

### Polish

- **Inline the supplementary docs.** Currently three small markdown
  files under `manuscripts/supplementary/`. The notebooks could
  inline-render them as appendix-style markdown cells so reviewers
  see the full methodology without leaving the rendered HTML.
- **Add a "regenerate figures" notebook (06).** A single notebook
  that imports `subway_access`, re-runs the figure pipeline against
  whatever MTA snapshot is current, and overwrites
  `artifacts/figures/`. Would close the loop between the static
  mirror and the live data.
- **Add a side-by-side comparison artifact.** When/if we regenerate
  against fresh MTA data, save the delta — which figures changed,
  which numbers shifted. Useful for "what's different about the
  May 2027 snapshot vs. the April 2026 baseline?"

### Narrative

- **Add a brief "what to look at first" header to the index.** The
  catalogue currently just lists notebooks 01–05; a one-line lead
  ("Start at notebook 01 for the policy framing; jump to notebook 04
  if you want the spatial-clustering map") would help reviewers
  navigate.

## Status of each notebook

| Notebook | Coverage | Status |
|---|---|---|
| 01 | §1, §2, §4.1–4.2 + Figs 1, 2, 5 | OK (mirror) |
| 02 | §3.2–3.4, §4.3 + Figs 3, 8, 9, 10 | OK (mirror) |
| 03 | §3.5, §4.4–4.7 + Figs 6, 7, 11–13 | OK (mirror) |
| 04 | §3.6, §4.8 + Figs 4, 14, 15 | OK (mirror) |
| 05 | §5 (limitations + policy) | OK (mirror) |

## Pointers

- Full case study prose: [`CASESTUDY_FULL.md`](CASESTUDY_FULL.md)
- Supplementary methodology: [`supplementary/`](supplementary/)
- Per-notebook tearsheets: [`tearsheets/`](tearsheets/)
- Upstream re-generation: [`UPSTREAM_REFERENCE.md`](UPSTREAM_REFERENCE.md)
