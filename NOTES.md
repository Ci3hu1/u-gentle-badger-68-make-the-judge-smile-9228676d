# Notes — Make the Judge Smile

- Bounty: `u-gentle-badger-68-make-the-judge-smile-9228676d` — "Make the Judge Smile"
- Prize: $5 total, top 3 ($2 / $2 / $1), free entry, no prerequisites
- Entries close: 24 Nov 2026 12:50 WIB (05:50 UTC)
- Blind rounds: R1 cutoff 07:28 WIB, R2 10:09 WIB, final 12:50 WIB
- Field at build time: 25 submissions (small table)
- Judge: z-ai/glm-5.3-flash, pairwise on subject > warmth > surprise > one concrete detail > fresh wording
- Gate: program writes one UTF-8 line, 1–200 chars, not only whitespace, to `/output/entry.txt`

## Entry line (99 chars)
> The barista remembered my order, then slid a second coffee across: "for the walk home in the rain."

## Build
- Repo: https://github.com/Ci3hu1/u-gentle-badger-68-make-the-judge-smile-9228676d
- Kit: fresh download 24 Nov 2026 ~04:59 WIB from https://make.fun/c/<slug>/kit (7,916,282 bytes; first attempt hit a transient 503 "database out of reach", retried after 6s)
- main.py: pure stdlib, writes the line to /output/entry.txt, chmod 0644
- Tests: `python3 -m unittest discover -s tests -v` — 2 tests, both pass (line gate + exact program output)
- Kit check: see below

## Status
- Built 24 Nov 2026 ~05:05 WIB. NOT submitted — awaiting Joni's 'Setuju' on this exact entry.
- Live score / rank: none yet (blind rounds; nothing judged until R1 cutoff 07:28 WIB).
