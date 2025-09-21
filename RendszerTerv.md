# Rendszerterv

## A rendszer célja
- Oktatás interaktívabbá tétele
- Diákok aktivitásának növelése
- Tanórák hangulatának javítása
- Nem cél a tanóra helyettesítése, csak kiegészítése

## Projektterv
- 4 fejlesztő
- Szerepkörök, felelősségek?
- 1 hét?
- Ütemterv?
- Mérföldkövek:
  - kezdőlap
  - játékos nevének bevitele
  - kérdések megjelenítése sorban
  - pontrendszer kialakítása
  - visszaszámlálás kérdésenként
  - kérdésbank kialakítása
  - ranglista kezelése
  - ranglista megjelenítése

## Üzleti folyamatok modellje
- Üzleti szereplők:
   - Tanár
      - Elindítja a játékot az órán
      - A játék végén látja az összesített eredményeket és a diákok teljesítményét
      - Felhasználja az eredményeket a tanóra értékeléséhez
   - Diák
      - Belép a játékba saját név megadásával
      - Válaszol a feltett kérdésekre a rendelkezésre álló időkereten belül
      - Azonnali visszajelzést kap a válasz helyességéről és pontszámáról
      - A játék végén megtekinti az összpontszámát, valamint az összes kérdést és helyes válaszokat
   - Rendszer (Quiz alkalmazás)
      - Kezeli a kérdésbázist (JSON fájl)
      - Véletlenszerűen kiválasztja a 10 kérdést a játékhoz
      - Időkeretet szab (20 másodperc)
      - Pontszámot számol a válasz helyessége és gyorsasága alapján
      - Nyilvántartja az eredményeket, és ranglistát készít
- Üzleti folyamatok:
  - Kvíz előkészítése
    - Tanár létrehozza vagy kiválasztja a kérdésbázist
    - Rendszer a kérdésbázisból véletlenszerűen 10 kérdést választ ki
  - Játék indítása
    - Tanár elindítja a kvízt
    - Diákok név megadásával csatlakoznak a játékhoz
    - Rendszer megjeleníti az első kérdést minden résztvevőnek
  - Kérdések megválaszolása
    - Rendszer megjelenít egy kérdést 4 válaszlehetőséggel
    - Diák kiválasztja a választ 20 másodpercen belül
    - Rendszer azonnali visszajelzést ad (helyes/nem helyes, pontszám)
    - A folyamat ismétlődik a 10 kérdésig
  - Pontozás és ranglista
    - A rendszer minden diákhoz hozzárendeli az összpontszámot
    - Játék végén rangsort készít (név + pontszám)
    - Megjeleníti a legjobb teljesítményt nyújtó diákokat
  - Eredmények áttekintése
    - Diák a játék után megtekintheti a helyes válaszokat
    - Tanár hozzáfér az összesített eredményekhez és statisztikákhoz
- Üzleti entitások:
  - Kérdés
    - Attribútumok: szöveg, válaszlehetőségek, helyes válasz
    - Forrás: JSON fájl
  - Diák
    - Attribútumok: név, adott játékban elért pontszám, válaszok
  - Pontszám
    - Attribútumok: helyesség (igen/nem), válaszidő, kiszámított pont
  - Játék (kvíz)
    - Attribútumok: 10 kiválasztott kérdés, időkeret, résztvevők listája, ranglista
  - Ranglista
    - Attribútumok: diák neve, összpontszám, sorrend            
## Követelmények
- Regisztráció és bejelentkezés:
  - Tanár és diák külön szerepkörökkel
 - Kvízek kezelése:
   - Elindítás, leállítás
   - Feleletválasztós/Igaz-Hamis
- Játékmenet:
  - Tanár indítja a kvízt, a diákok valós időben csatlakoznak egy nevet megadva
  - Kérdések időzítéssel jelennek meg
  - Automatikus pontozás a válaszok gyorsasága és helyessége alapján
- Eredmények megjelenítése:
  - Kvíz végén összesítés (helyes válaszok száma, pontszám)
- Felhasználói élmény:
  - Diákok telefonról könnyen tudják használni
  - Színes, játékos grafika a motiváció fenntartására

## Funkcionális terv
- Rendszerszereplők:
  -  Tanár: elindítja a játékot, összeválogatja a kérdéseket (opcionális)
  -  Diák: belép a rendszerbe, kitölti a kvízt, megkapja a pontszámot
- Rendszerhasználati esetek és lefutásaik
- Határ osztályok
- Menühierarchiák:
  -  Kezdőképernyő:
      - Név bevitel
      - Játék indítása
  -  Kérdés képernyő:
      - Kérdés + válaszlehetőségek
      - Időzítő
      - Ideiglenes pontszám
  -  Eredmény képernyő:
      - Helyes válaszok száma
      - Pontszám
      - Ranglista
      - Áttekintés gomb
  -  Áttekintés képernyő:
      - Kérdések listája
      - Helytelen válasz
      - Helyes válasz
      - Vissza gomb
- Képernyőtervek:
  <img width="1091" height="428" alt="Képernyőterv" src="https://github.com/user-attachments/assets/bac03afc-ff1b-4ffc-83fa-5497e2fbd730" />

  
