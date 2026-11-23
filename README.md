[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/akbare12/news-22-b11-inside-the-day/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/akbare12/news-22-b11-inside-the-day/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

# THE WORLD TODAY — Inside the Day, Sunday 22 November 2026

One image summing up the world's news of Sunday 22 November 2026, laid out
as a newspaper you can open: three heroes on the front page, then four
sections to step inside — A WORLD, B CLIMATE & ENERGY, C POLITICS & MARKETS,
D PEOPLE — 35 stories in all, every one first reported on 22 November 2026.

## The three heroes

1. **2 TANKERS HIT** — Two supertankers hit mines east of the Strait of
   Hormuz, both on fire. First reported 17:13 UTC. (Iran navy · AP)
2. **NO DEAL** — COP31 in Antalya collapses; the EU and ~130 parties reject
   a text with no fossil-fuel language. First collapse since 2009.
   (CNN · Reuters)
3. **258** — Democrats win the House, their largest majority since 1992;
   Hubbard beats Foxx by 330 votes in the North Carolina recount.
   (AP · Reuters)

## Inside the sections

- **SECTION A — WORLD (11 stories):** Dymer drone hits flats, 7 killed;
  Merkury hit at Benghazi (CLAIM); Khartoum drones kill 4 (CLAIM);
  Zelenskyy pleads for Patriots; Iran shows underground missile city;
  Saudis stop Houthi attack (CLAIM); Bahrain blames Iran; UAE condemns
  Bahrain strike; Europe protests, day 3, 144 held in France; settlers
  burn 12 West Bank cars; Benghazi depot blast.
- **SECTION B — CLIMATE & ENERGY (5 stories):** why the COP31 talks failed;
  Russian cargo ship burns in the Baltic; EU–Indonesia trade deal;
  Asian stocks slide; Fidan: war fallout hits markets.
- **SECTION C — POLITICS & MARKETS (6 stories):** Eisenkot–Likud unity
  talks stall; Finland: war spills over; Mongolia snap vote; Mexico cartel
  boss captured; Korea minister quits over AI-cheating scandal (111 device
  cases); Fidan: Israel may use Druze (CLAIM).
- **SECTION D — PEOPLE (10 stories):** Banten factory fire, 3 dead,
  36 missing; Gaza aid van strike — WCK: three killed were not its team;
  Gaza: 350,000 homeless; settlers attack Hebron homes; Gaza homes blocked
  (CLAIM); Germany urged to arrest soldier; Fred Nile dies at 92 (died
  21 Nov, announced 22 Nov); gamer, 16, and mother help FBI rescue missing
  girl; Gaza toll 1,661; Paolo Bulgari dies at 89 (death announced 22 Nov).

## How to read it

- **REPORTED** = confirmed by two or more sources.
  **CLAIM** = one side alleges, unverified. **ONGOING** = still developing.
- **NOT YET — DO NOT READ AS DONE:** 4 House races uncalled · COP32 venue
  not set · Gaza ceasefire talks: no deal announced.
- **DATE CHECK:** every story was first reported on 22 Nov 2026. Not 22 Nov
  and left out on purpose: El Chapo Isidro captured 20 Nov · BepiColombo
  Mercury orbit 21 Nov · ICJ Myanmar ruling 19 Nov · Wall St rout 20 Nov ·
  FBI NCIC hack first reported 21 Nov.
- Sources: AP · Reuters · BBC · CNN · France 24 · Al Jazeera · Guardian ·
  SCMP · Anadolu · WAFA · WCK · HRF · FBI.

## The program

`main.py` (Python 3, standard library only) copies `entry.png` to
`/output/entry.png` and verifies it first: PNG magic, 1024×1024 dimensions,
size and SHA-256. Run it with `MAKEFUN_OUTPUT_DIR=out python3 main.py`.
The image itself is drawn by `draw.py` (PIL), which lays out the masthead,
the three hero panels, the numbers strip, the four colour-banded sections
and the footer date-check from the story list in that file.

## License

MIT — see LICENSE.
