# Seadistamine: kontod ja oma aadress

Kolm osa. Igaüks võtab 5–15 minutit. Tee need järjekorras.

1. **Firebase** — kasutajakontod ja andmebaas (tasuta)
2. **Zone.ee** — aadress `hoov.3x3estonia.com`
3. **GitHub** — aadress lehe külge

Leht töötab juba enne seadistamist aadressil https://3x3-estonia.github.io/3x3-oskuste-hoov/ — ainult ilma kontodeta (edenemine jääb brauserisse).

---

## 1. Firebase (kasutajakontod)

Kasuta klubi Google'i kontot (**3x3estonia@gmail.com**), et projekt jääks klubile, mitte ühele inimesele.

### Samm 1: projekt

1. Ava https://console.firebase.google.com ja logi sisse klubi Google'i kontoga.
2. Vajuta **Create a project** (või „Loo projekt").
3. Nimi: `3x3-oskuste-hoov`. Vajuta **Continue**.
4. **Google Analytics:** lülita **välja** (pole vaja). Vajuta **Create project**.

Plaan jääb tasuta **Spark** plaanile. Krediitkaarti pole vaja.

### Samm 2: sisselogimine

1. Vasakult menüüst **Build → Authentication** → **Get started**.
2. Vahekaart **Sign-in method**:
   - Vali **Google** → lülita **Enable** sisse → **Project support email**: 3x3estonia@gmail.com → **Save**.
   - Vajuta **Add new provider** → **Email/Password** → lülita sisse **Email link (passwordless sign-in)** → **Save**. (Ülemist „Email/Password" lülitit pole vaja.)
3. Vahekaart **Settings → Authorized domains** → **Add domain** ja lisa mõlemad:
   - `3x3-estonia.github.io`
   - `hoov.3x3estonia.com`

### Samm 3: andmebaas

1. Vasakult **Build → Firestore Database** → **Create database**.
2. **Location:** vali **eur3 (europe-west)**. *Seda ei saa hiljem muuta — vali kindlasti Euroopa.*
3. Vali **Start in production mode** → **Create**.
4. Ava vahekaart **Rules**. Kustuta seal olev tekst ja kleebi asemele kogu faili [`firestore.rules`](firestore.rules) sisu. Vajuta **Publish**.

Need reeglid lubavad igal kasutajal näha ja muuta ainult oma andmeid.

### Samm 4: veebirakenduse seadistus

1. Vasakul üleval hammasratas ⚙️ → **Project settings**.
2. All **Your apps** → vajuta veebi ikooni **`</>`**.
3. Nimi: `hoov`. **Firebase Hosting** linnukest **ära pane**. Vajuta **Register app**.
4. Näed koodiplokki, kus on `const firebaseConfig = { apiKey: "...", ... }`.
5. **Kopeeri see plokk (alates `{` kuni `}`) ja saada Claude'ile.** Need väärtused on avalikud ja võivad olla avalikus repos — andmeid kaitsevad 3. sammu reeglid. Claude paneb need faili `docs/firebase-config.js`.

### Samm 5: e-kirjade keel (valikuline)

**Authentication → Templates** → saad muuta sisselogimiskirja saatja nime (nt „3x3 oskuste hoov") ja vaikekeelt.

---

## 2. Zone.ee (aadress hoov.3x3estonia.com)

See ei muuda praegust veebilehte 3x3estonia.com. Lisame ainult uue alamaadressi.

1. Logi sisse https://my.zone.eu (Minu Zone).
2. Vali domeen **3x3estonia.com**.
3. Ava **DNS** seaded (menüüs „Domeenid" → domeeni juures **DNS** või „Halda DNS-kirjeid").
4. Lisa uus kirje:

   | Väli | Väärtus |
   |---|---|
   | Tüüp | **CNAME** |
   | Nimi / Host | **hoov** |
   | Väärtus / Sihtmärk | **3x3-estonia.github.io.** (punktiga lõpus, kui Zone seda lubab; kui annab vea, siis ilma punktita) |
   | TTL | vaikimisi (nt 3600) |

5. Salvesta.

DNS-i muudatus jõuab kohale 5 minutist kuni mõne tunnini.

**Kui Zone'is on DNS hallatud mujal** (nt Canva või Cloudflare näitab nimeservereid): lisa sama CNAME-kirje seal, kus DNS-i hallatakse. Zone'i halduses on see vaikimisi Zone ise.

---

## 3. GitHub (aadress lehe külge)

Kui oled Zone'is CNAME-kirje lisanud, ütle Claude'ile: *„CNAME on lisatud"*. Claude:

1. lisab faili `docs/CNAME` sisuga `hoov.3x3estonia.com`,
2. seab GitHub Pagesis kohandatud domeeni ja HTTPS-i.

Või tee ise: repo **Settings → Pages → Custom domain** → `hoov.3x3estonia.com` → **Save**. Kui kontroll on läbi, pane linnuke **Enforce HTTPS**.

---

## Kontroll pärast seadistamist

- Ava https://hoov.3x3estonia.com
- Jaotises **Minu plaanid** peab olema kast **Sinu konto** nuppudega „Jätka Google'iga" ja „Saada link".
- Logi sisse, märgi üks video vaadatuks, ava leht teises seadmes ja logi sama kontoga sisse: linnuke peab olema ka seal.
