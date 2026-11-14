# 3x3 oskuste hoov · Двор навыков 3x3

Iseseisev 3x3 korvpalli kursus Eesti naistele ja tüdrukutele, eelkõige 5v5 mängijatele, kes tahavad hooaja jooksul ise harjutada. Eesti ja vene keeles.

**Leht:** https://claude.ai/artifact/YD3i4Z8g57rsydms1yr7hf (vene keeles: lisa lingi lõppu `#ru`)

## Mis seal on

- **Kursus:** 10 põhioskust. Igal oskusel on selgitus, võtmepunktid, harjutused ja 2–3 videot. Vaadatud videod saab linnukesega märkida ja oskuse omandatuks märkida.
- **Planeerija:** koostab päeva-, nädala-, kuu- või aastaplaani valitud oskuse ja eesmärgi järgi. Nädalaplaan arvestab klubi trennipäevadega.
- **Minu plaanid:** salvestatud plaanid, mille osad saab tehtuks märkida.
- **Enesetestid:** 2-punktiline vise, lõpetamine, vastupidavus. Tulemused salvestuvad koos kuupäevaga.
- **Reeglid lühidalt** ja **head tavad**.

## Kuhu edenemine salvestub

- claude.ai-sse sisse loginud vaatajal salvestub edenemine tema kontole (`db` võimekus, privaatne kaust `data/users/<id>/`). Seda ei näe keegi teine, ka lehe omanik mitte.
- Teistel jääb edenemine ainult nende brauserisse (`localStorage`).

## Failid

| Fail | Mis see on |
|---|---|
| `index.html` | Kogu leht: sisu, kujundus ja loogika (Claude Artifact, ilma `<html>`/`<head>`/`<body>` sildita). |

## Kuidas sisu muuta

Kõik tekstid on failis `index.html` objektides `T` (liidese tekstid), `S` (10 oskust), `RULES`, `PRACT` ja `TESTS`. Iga tekst on paarina `['eesti keeles', 'по-русски']`.

Videote vahetamiseks muuda oskuse `vids` loendit: `['YouTube ID', 'pealkiri', 'kanal', 'pikkus']`.

Pärast muutmist ütle Claude'ile: *„avalda index.html uuesti lehele https://claude.ai/artifact/YD3i4Z8g57rsydms1yr7hf"*.

## Videod

Kõik 25 videot on kontrollitud (olemas, pealkiri ja kanal klapivad) 14.11.2026. Videod kuuluvad nende autoritele ja avanevad YouTube'is.
