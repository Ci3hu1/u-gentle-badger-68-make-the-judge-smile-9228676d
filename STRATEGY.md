# Strategy — Make the Judge Smile

## What the judge rewards (in order)
1. Subject: one line about a small good thing that happened today.
2. Warmth: a small kindness or piece of luck that feels genuinely felt.
3. Surprise: a turn somewhere unexpected, in the thing or in the telling.
4. Concreteness: one real small detail (a name, a sound, a time of day).
5. Fresh wording: its own words and rhythm, no greeting-card phrasing.

## Our line (99 chars)
> The barista remembered my order, then slid a second coffee across: "for the walk home in the rain."

## Why this line
- **Subject**: a small good thing today — a free second coffee from a barista.
- **Warmth**: an unasked kindness, remembered order + gift, genuinely felt.
- **Surprise**: the turn is the quoted reason — the coffee is not for drinking
  here, it is "for the walk home in the rain", reframing the gift.
- **Concreteness**: one detail doing double work — the second coffee and the
  rain outside, a time-and-weather anchor in a single image.
- **Fresh wording**: plain spoken scene, no greeting-card sentiment, no
  "grateful/blessed" stock phrasing; the quote carries the voice.
- **Short on purpose**: 99 chars, well under the 200 cap. Judge-feel
  competitions reward a short line with one image and a turn, not a paragraph.
  Length for its own sake does not count (per the judge brief).

## What we did not do
- No address to the judge (allowed, but the scene stands on its own).
- No generic sentiment ("today was a beautiful day") — the brief's first
  criterion loses to any line about a concrete small good thing.
- No second detail competing for attention: one detail, one turn.

## Program
Pure-stdlib `main.py` writes the line verbatim to `/output/entry.txt`
(1–200 chars, UTF-8, not whitespace-only), chmod 0644 so the grader can
collect it. Nothing is read from the network, the git history, or any
secret; everything the entry runs is in this repository.
