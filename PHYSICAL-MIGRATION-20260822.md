# Physical Repository Migration — 2026-08-22

Status: **CUTOVER COMPLETE — current standalone physical home**.

This repository is the prepared standalone physical home for **Ordivon Interlocus**. The move changes physical placement and Git topology only. It does **not** change semantic owner identity, referent, Foundation/derived-theory standing, historical authority publications, consumer semantics, or runtime/service topology.

## Source fence

- source repository: `ordivon-research`
- source revision: `6cee31e6c251e3c245ced73ea544f453a68f19e9`
- source subtree: `owners/network`
- source subtree tree: `b9ff41a62bd051791639b7d29b23ede32698ebad`

The filtered history preserves the owner-relevant genealogy and exact source-owner content at the migration fence. Historical publications that name the old repository/path remain immutable historical provenance and are not rewritten.

The physical repository name is `ordivon-interlocus`, while the stable semantic owner identity remains `research-owner:network` and authority identity remains `authority:ordivon:research-owner:network`. Historical NDF/NCT and `network-*` identifiers are unchanged.

## Cutover rule

Cutover is complete under `PHYSICAL-CUTOVER-20260822.json`. Atlas live discovery resolves this standalone repository and the old parent `main` path is a non-authoritative tombstone. Historical source revisions/publications remain immutable and Git-recoverable.
