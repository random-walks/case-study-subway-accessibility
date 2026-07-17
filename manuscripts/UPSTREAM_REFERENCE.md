# Upstream reference

This repo mirrors the April 2026 vintage of the NYC subway
accessibility analysis published as the canonical CASESTUDY of the
[`subway-access`](https://github.com/random-walks/subway-access) v0.5.1
library. The 15 figures and the headline numbers inlined in this
package are pre-rendered snapshots — they are not recomputed by the
notebooks here.

The runnable pipeline that produces them lives upstream:

- **Library**: [`random-walks/subway-access`](https://github.com/random-walks/subway-access)
  — typed Python toolkit for reproducible NYC subway accessibility
  analysis. Version 0.5.1 (the pinned release) ships the factor-factory
  engine-audit Appendix D and the jellycell reporting bridge.
- **Example pipeline**: [`examples/accessibility-change-over-time/`](https://github.com/random-walks/subway-access/tree/main/examples/accessibility-change-over-time)
  — `main.py` is the entry point that fetches the MTA + ACS data,
  runs the factor-factory / DiD / spatial pipeline, and emits the
  figures and tables embedded here.
- **Upstream CASESTUDY**: `examples/accessibility-change-over-time/CASESTUDY.md`
  in the upstream repo.
- **FOIL request gap**: see §3.5 of the upstream CASESTUDY for the
  provenance discussion — the request chases the 56 missing station
  upgrade dates from the MTA Key Station Program. A ready-to-send
  template is in this file, under [FOIL request gap](#foil-request-gap-data-provenance-caveat) below.

## Regenerating against a later vintage

To regenerate against fresh data (e.g., later MTA snapshots or the
2020–2024 ACS vintage):

```bash
git clone https://github.com/random-walks/subway-access
cd subway-access/examples/accessibility-change-over-time
uv sync
python main.py
```

`uv sync` pulls in factor-factory and jellycell automatically — the
example project depends on `subway-access[all]`, which bundles both
(Python 3.12+ required for those components). The `factor-factory` and
`tearsheets` extras belong to the root `subway-access` package, not
this example project, so they can't be requested with `--extra` here.

The output figures, tables, and the auto-generated report
(`accessibility-change-report.md`) land in `reports/` under the
upstream example directory. To refresh this wrapper:

1. Replace `artifacts/figures/figure-*.png` with the regenerated
   figures (keep the filenames — notebook 02 inlines by exact path).
2. Update the headline-numbers dict at the top of
   `notebooks/01_context_and_pointer.py` to reflect the new vintage.
3. If any numerical result drifts enough to invalidate the cross-walk
   row, update `notebooks/03_cross_walk.py` accordingly.
4. Re-run the notebooks from this repo's root to refresh the
   artifacts and the journal:

   ```bash
   uv sync
   for nb in notebooks/[0-9]*.py; do uv run jellycell run "$nb"; done
   ```

5. `jellycell run` does not touch the tearsheets — export them
   separately (and optionally re-render the HTML catalogue under
   `site/`):

   ```bash
   for nb in notebooks/[0-9]*.py; do uv run jellycell export tearsheet "$nb"; done
   uv run jellycell render
   ```

## FOIL request gap (data provenance caveat)

Of the 157 currently accessible NYC subway stations, 101 have ADA
upgrade years traced to MTA press releases, Governor's announcements,
MTA Capital Program records, Wikipedia station articles, and news
coverage spanning 1987–2026. The remaining 56 — primarily Key Station
Program stations from the 1990s–2010s — use a deterministic hash-based
fallback because per-station completion records are not publicly
documented at time of publication. A FOIL request to the MTA for the
complete Key Station Program completion schedule would close this gap
and enable fully credible DiD identification.

A minimal FOIL request template:

```
To: FOIL Officer, Metropolitan Transportation Authority
Re: FOIL request — Key Station Program completion schedule

Under Article 6 of the Public Officers Law, I request records
identifying the completion date (month and year) of each subway
station ADA upgrade performed under the Key Station Program
(1994–2020). For each station, please provide:

  - Station name and complex ID
  - ADA completion date (month / year)
  - Funding source (Key Station Program, Capital Program cycle, other)
  - Primary accessibility feature completed (elevator, ramp, etc.)

Electronic records (spreadsheet or CSV) preferred. If records are
maintained across multiple offices, please coordinate the response.

Sincerely,
<name> <affiliation>
```

## Version pinning

This wrapper depends on `subway-access >= 0.5, < 0.6` via this
repository's `pyproject.toml`. The pin intentionally excludes 0.6
because the CASESTUDY
numbers and figure set are expected to refresh at that minor version.
When 0.6 ships, bump the pin and re-run the regeneration recipe above.
