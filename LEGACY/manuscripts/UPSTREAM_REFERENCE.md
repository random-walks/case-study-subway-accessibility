# Upstream reference

This jellycell showcase mirrors a snapshot of the NYC subway
accessibility analysis published April 2026. The figures, tables, and
prose are preserved verbatim — they are not recomputed by the notebooks
in this showcase.

The runnable pipeline that produces them lives upstream:

- **Library:** [`random-walks/subway-access`](https://github.com/random-walks/subway-access)
  — typed Python toolkit for reproducible NYC subway accessibility analysis.
- **Example pipeline:** [`examples/accessibility-change-over-time/`](https://github.com/random-walks/subway-access/tree/main/examples/accessibility-change-over-time)
  — `main.py` is the entry point that fetches MTA + ACS data, runs the
  factor / DiD / spatial pipeline, and emits the figures and tables
  embedded here.

To regenerate against fresh data (e.g., later MTA snapshots or the
2024–2028 ACS vintage):

```bash
git clone https://github.com/random-walks/subway-access
cd subway-access/examples/accessibility-change-over-time
uv sync
python main.py
```

The output figures and `CASESTUDY.md` will land in `reports/` under
the example directory. Replace this showcase's `artifacts/figures/` and
`manuscripts/CASESTUDY_FULL.md` with the regenerated artifacts and
re-run `pnpm showcase:render showcase-subway-accessibility` to refresh
the rendered HTML.
