# 3x3 oskuste hoov · Двор навыков 3x3

Iseseisev 3x3 korvpalli kursus Eesti naistele ja tüdrukutele, eelkõige 5v5 mängijatele, kes tahavad hooaja jooksul ise harjutada. Eesti ja vene keeles.

**Leht:** https://3x3-estonia.github.io/3x3-oskuste-hoov/ (tulevikus https://hoov.3x3estonia.com) · vene keeles lisa lõppu `#ru`

Claude Artifacti versioon (privaatne): https://claude.ai/artifact/YD3i4Z8g57rsydms1yr7hf

**Seadistamine (kontod ja aadress):** vt [`SEADISTAMINE.md`](SEADISTAMINE.md)

## Mis seal on

- **Kursus:** 10 põhioskust. Igal oskusel on selgitus, võtmepunktid, harjutused ja 2–3 videot. Vaadatud videod saab linnukesega märkida ja oskuse omandatuks märkida.
- **Planeerija:** koostab päeva-, nädala-, kuu- või aastaplaani valitud oskuse ja eesmärgi järgi. Nädalaplaan arvestab klubi trennipäevadega.
- **Minu plaanid:** salvestatud plaanid, mille osad saab tehtuks märkida.
- **Enesetestid:** 2-punktiline vise, lõpetamine, vastupidavus. Tulemused salvestuvad koos kuupäevaga.
- **Reeglid lühidalt** ja **head tavad**.

## Kuhu edenemine salvestub

- **Veebilehel (GitHub Pages):** kasutaja logib sisse Google'i kontoga või e-posti lingiga. Edenemine ja plaanid salvestuvad Firebase'i andmebaasi (Euroopas), igaüks näeb ainult enda omi (`firestore.rules`). Kuni Firebase pole seadistatud, jääb edenemine brauserisse.
- **Claude Artifactis:** claude.ai-sse sisse loginud vaataja privaatsesse kausta, teistel brauserisse.
- Kasutaja saab oma konto ja andmed ise kustutada. Privaatsusteade: `docs/privaatsus.html`.

## Failid

| Fail | Mis see on |
|---|---|
| `index.html` | Lähtekood: sisu, kujundus ja loogika. Sama fail on Claude Artifact (ilma `<html>`/`<head>`/`<body>` sildita). |
| `build.py` | Teeb `index.html`-ist veebilehe `docs/index.html` (lisab raami ja Firebase'i). Käivita pärast iga muudatust: `python3 build.py`. |
| `docs/` | GitHub Pagesi leht: `index.html` (genereeritud, ära muuda käsitsi), `firebase-config.js`, `privaatsus.html`. |
| `firestore.rules` | Andmebaasi turvareeglid. Kleebitakse Firebase'i konsooli. |
| `SEADISTAMINE.md` | Juhend: Firebase, Zone.ee DNS, GitHubi domeen. |
| `versioonid/v1-eesti-keeles.html` | Esimene versioon (14.11.2026), ainult eesti keeles. Alles võrdluseks. |

## Kuidas sisu muuta

Kõik tekstid on failis `index.html` objektides `T` (liidese tekstid), `S` (10 oskust), `RULES`, `PRACT` ja `TESTS`. Iga tekst on paarina `['eesti keeles', 'по-русски']`.

Videote vahetamiseks muuda oskuse `vids` loendit: `['YouTube ID', 'pealkiri', 'kanal', 'pikkus']`.

Pärast muutmist käivita `python3 build.py` ja pushi. Artifacti uuendamiseks ütle Claude'ile: *„avalda index.html uuesti lehele https://claude.ai/artifact/YD3i4Z8g57rsydms1yr7hf"*.

## Videod

Kõik 25 videot on kontrollitud (olemas, pealkiri ja kanal klapivad) 14.11.2026. Videod kuuluvad nende autoritele ja avanevad YouTube'is.
