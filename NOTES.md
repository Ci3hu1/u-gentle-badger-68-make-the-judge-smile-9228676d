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
- Kit check (`node cli/makefun.mjs check --repo ... --commit d06bcc3...`, 24 Nov ~05:07 WIB): 4 passed (competition_open, snapshot, license_osi, entrypoint), 1 failed — transcripts_present (no bundle yet; bundle is made at submit time by the top-level agent), 14 skipped, 5 checks deferred to submission (repo_public, repo_owner, repo_created_after_open, commit_in_repo, duplicate_snapshot). No local grade for this bounty — the server grades every entry.

## Status
- Built 24 Nov 2026 ~05:05 WIB. NOT submitted — awaiting Joni's 'Setuju' on this exact entry.
- Live score / rank: none yet (blind rounds; nothing judged until R1 cutoff 07:28 WIB).

## Revision + submit (24 Nov 2026 ~11:47 WIB)
- First submit attempt FAILED kit check on thinking_revised only (main.py written in 1 message). Fix on Joni's "Setuju, perbaiki dan submit keduanya" (11:44 WIB): genuine revision — extracted validate() (gate check: 1-200 chars, not blank, single line, no control chars) + output read-back self-check, plus 2 new tests. Entry line UNCHANGED (99 chars). Tests 4/4.
- New entry commit ef6a18d49c11e96192184aa64880ba935a94b764 (main), pushed, ls-remote verified.
- Bundle ~/workspace/tools/makefun/bundles/u-gentle-badger-68-make-the-judge-smile-9228676d.tar.gz sha256 fbb1f63d8c67a797f7e0ce696ce210cb660b0ba798a450f83418087dbd59cea8 (232,370 B; fresh level-40 kit; sessions builder 583bfe2b + revision 530a0704; 1 usage row).
- Kit check on ef6a18d4: ok=true, failed [] (thinking_revised PASS).
- SUBMITTED 24 Nov ~11:48 WIB: submission 01a20be1-3719-767c-a866-b9f0efb040ba, stage checked (passed its checks). Blind, 3 rounds — counts from round 3 of 3, the final at the deadline 12:50 WIB. Claim code ONLY in ~/.config/makefun/u-gentle-badger-68-make-the-judge-smile-9228676d-submission.json (0600).
