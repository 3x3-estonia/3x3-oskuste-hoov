// Firebase'i veebirakenduse seadistus. Vt SEADISTAMINE.md, samm 4.
// Need väärtused on avalikud ja tohivad olla siin failis: andmeid kaitsevad
// Firestore'i reeglid (firestore.rules), mitte see fail.
// Kuni siin on null, töötab leht ilma kontodeta (edenemine jääb brauserisse).
window.HOOV_FIREBASE = null;
/* Näide, kuidas see välja näeb pärast täitmist:
window.HOOV_FIREBASE = {
  apiKey: "...",
  authDomain: "....firebaseapp.com",
  projectId: "...",
  storageBucket: "....appspot.com",
  messagingSenderId: "...",
  appId: "..."
};
*/
