---
name: committed-tearsheets
description: How this wrapper's committed tearsheets and pinned JSON artifacts regenerate cleanly. Apply when setting up the manuscripts/ dir or reviewing why a notebook re-run produces git-noisy diffs.
---

# Committed tearsheets, clean regen

This case study is a **thin portfolio wrapper** over the upstream
`subway-access` analysis. It computes no DiD and ships **no** `FINDINGS.md`.
Its committed outputs are three per-notebook tearsheets plus a small set of
pinned JSON artifacts and mirrored figures (repo root):

```
manuscripts/
├── tearsheets/
│   ├── 01_context_and_pointer.md  ← one per notebook, exported, committed
│   ├── 02_figures_gallery.md
│   └── 03_cross_walk.md
├── MANUSCRIPT.md                  ← hand-authored paper, committed
└── UPSTREAM_REFERENCE.md          ← hand-authored pointer to the canonical study, committed
artifacts/
├── headline_numbers.json          ← pinned headline dict (hard-coded in notebook 01), committed (plain git)
├── cross_walk.json                ← engine cross-walk (hard-coded in notebook 03), committed (plain git)
├── cross_walk_table.parquet       ← the cross-walk as a table, committed (plain git)
└── figures/*.png                  ← figures mirrored from an upstream clone, committed (plain git)
```

## The pinned-artifact pattern

**Important**: jellycell ≥ 1.4.0 (see `pyproject.toml`) ships a
`jellycell.tearsheets` Python API — `jt.findings()`, `jt.methodology()`,
`jt.audit()` (see `jellycell-gotchas.md` §5). This wrapper does not emit a
`FINDINGS.md`, so it doesn't call `jt.findings()`; a study that *does*
synthesize findings should prefer that API. There is **no** `_helpers`
module in this repo.

Because there is no recomputation here, byte-stability is structural: the
headline numbers are a **hard-coded dict** in `notebooks/01_context_and_pointer.py`
(persisted to `artifacts/headline_numbers.json`) and the engine cross-walk
is hard-coded in `notebooks/03_cross_walk.py` (persisted to
`artifacts/cross_walk.json` + `cross_walk_table.parquet`). A bare re-run
recomputes neither — it just re-serializes the pinned values, so the JSON
diff is empty unless you edited the dict. To bump the upstream, follow the
steps in `CLAUDE.md` (raise the `subway-access` pin, re-copy the figures
from an upstream clone, hand-update the headline / cross-walk dicts, then
re-run).

Per-notebook tearsheets (`manuscripts/tearsheets/*.md`) are exported via
the CLI:

```bash
uv run jellycell export tearsheet notebooks/03_cross_walk.py \
    --output manuscripts/tearsheets/03_cross_walk.md
```

`jellycell export tearsheet` is its own command — `jellycell render` builds
the HTML catalogue under `site/` and does **not** rewrite the committed
markdown. (Each tearsheet carries a `last run` timestamp line, so that one
line is expected to move when you re-export.)

## Regen check

Re-run the notebooks (not `jellycell render`, which only rebuilds `site/`)
and confirm the pinned JSON artifacts are unchanged:

```bash
cp artifacts/headline_numbers.json /tmp/before.json
uv run jellycell run notebooks/01_context_and_pointer.py
diff -u /tmp/before.json artifacts/headline_numbers.json
# empty diff expected (the dict is hard-coded)
```

If the diff isn't empty and you didn't touch the dict, look for a
nondeterministic field that slipped into the notebook: `datetime.now()`,
`socket.gethostname()`, `uuid.uuid4()`.

## Committed binaries — separate concern

Figures and parquet are committed as **plain git blobs** — this repo uses
**no** Git LFS (see `.gitattributes`: the binary formats carry
`!text !filter !merge !diff` only to stop git mangling them, and the header
notes they are "left over from the LFS export"). Keep each committed
artifact under the `max_committed_size_mb = 50` cap in `jellycell.toml`.
The figures are copied verbatim from an upstream `subway-access` clone, so
the committed blob is byte-identical to the upstream render — don't
re-render them locally.

## Tearsheets ≠ the paper

- `tearsheets/*.md` = auto-generated per notebook, committed.
- `MANUSCRIPT.md` = hand-authored paper prose (see `paper-cadence` skill), never templated.
- `UPSTREAM_REFERENCE.md` = hand-authored pointer to the canonical study.

Do not hand-edit the tearsheets — edits get overwritten on next export. Put
prose in `MANUSCRIPT.md`; change the headline / cross-walk numbers by
editing the pinned dicts in `notebooks/01_context_and_pointer.py` and
`notebooks/03_cross_walk.py`.

## When to invoke this skill

- Setting up the `manuscripts/` dir.
- Seeing git noise in a tearsheet or a pinned JSON artifact after re-running a notebook with no real changes.
- Reviewing a PR that hand-edits a tearsheet — reject hand edits, redirect to notebook changes.

## When NOT to invoke this skill

- `README.md` or `UPSTREAM_REFERENCE.md` — both are hand-authored, no templating involved.
- `MANUSCRIPT.md` — hand-authored, follows `paper-cadence` skill instead.
