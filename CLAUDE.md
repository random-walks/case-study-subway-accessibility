# CLAUDE.md — case-study-subway-accessibility

One node of the blaise-oss ecosystem, developed from the
`blaise-dev-workspace` meta-repo (checked out at
`repos/published-case-studies/case-study-subway-accessibility/`).
Rules here win over workspace-level rules.

## What this repo is

The standalone home of the subway-accessibility case-study WRAPPER —
extracted from `blaise-website` `packages/python-showcase/` with full
history (2026-07). The canonical analysis lives UPSTREAM in
`random-walks/subway-access`
(`examples/accessibility-change-over-time/CASESTUDY.md`); this repo
mirrors its figures, publishes the 18-row engine cross-walk, and pins
the headline numbers as JSON.

- Stack: Python 3.12, uv (never pip), jellycell, subway-access (pinned).
- Run: `uv sync`, then `uv run jellycell run notebooks/<nb>.py` in order.
- Bumping the upstream: raise the `subway-access` pin in pyproject.toml,
  regenerate the figures from an upstream clone and copy them into
  `artifacts/figures/`, hand-update the headline dict in notebook 01
  (and notebook 03 if a cross-walk row drifts), then re-run the
  notebooks to refresh the JSON artifacts + tearsheets, and update
  version mentions in the manuscript. The notebooks inline pre-rendered
  figures and hard-coded headline numbers — a bare re-run recomputes
  neither. See `manuscripts/UPSTREAM_REFERENCE.md`.

## Publishing contract

`manuscripts/MANUSCRIPT.md` is the source of truth for the published
post at https://blaiseoss.com/posts/subway-accessibility-gaps (slug is
historical — do not change it). To publish: land changes here, then run
`./scripts/sync-case-study.sh subway` from the workspace root (two
cross-referenced commits). Plain-APA citations only; no hard-wrapped
hyphenated words; `artifacts/` and tearsheets are regenerated — never
hand-edit.
