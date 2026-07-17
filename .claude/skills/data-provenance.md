---
name: data-provenance
description: Committed artifacts under `artifacts/` (figures, `headline_numbers.json`, `cross_walk.json`) carry `upstream_package`/`upstream_version`/`study_vintage` inline instead of a `data/`-style `.meta.json` sidecar, because this wrapper has no `data/` directory or live-fetch pipeline of its own. Apply when refreshing artifacts after bumping the `subway-access` pin, or auditing this repo for provenance gaps.
---

# Data provenance: upstream-pinned artifacts, not local `data/`

This repo has no `data/` directory and no live-fetch pipeline — see
`CLAUDE.md`. It's a thin wrapper: the MTA/ACS fetch, join, and
model-fitting pipeline lives upstream in
[`random-walks/subway-access`](https://github.com/random-walks/subway-access)
(pinned via `subway-access[factor-factory,tearsheets]` in
`pyproject.toml`). What's committed here — `artifacts/figures/*.png`,
`headline_numbers.json`, `cross_walk.json` / `cross_walk_table.parquet`
— is upstream's *output*, mirrored at a pinned vintage.

## Why

Nothing here is fetched live, so provenance isn't "which script produced
this file" — it's "which `subway-access` version, and when." Every
committed artifact should carry that inline rather than relying on a
separate `data/`-style sidecar.

## The pattern (already followed by `headline_numbers.json`)

```json
{
  "upstream_package": "subway-access",
  "upstream_version": "0.5.1",
  "study_vintage": "April 2026"
}
```

`notebooks/01_context_and_pointer.py` reads `upstream_version` from
`subway_access.__version__` at run time rather than hardcoding it, so it
can't drift silently from the pin.

## Regenerating

Don't hand-edit `artifacts/**` (see `CLAUDE.md`) — regenerate it. Bumping
the pin and re-running the notebooks is the `release-bump` skill's job;
for the upstream half of the refresh (pulling new figures/numbers out of
`subway-access` itself before they land here) see
`manuscripts/UPSTREAM_REFERENCE.md` → "Regenerating against a later
vintage."

## When to invoke this skill

- Raising the `subway-access` pin in `pyproject.toml`.
- Reviewing a PR that edits `artifacts/**` by hand instead of via the
  regenerate recipe above.
- Auditing this wrapper for a committed artifact missing its
  `upstream_package` / `upstream_version` / `study_vintage` fields.
