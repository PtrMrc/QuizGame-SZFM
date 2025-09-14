# Követelményspecifikáció

## Jelenlegi helyzet:
- Pályakezdő tanárokként színesebbé szeretnénk tenni az óráinkat.
- Jelenleg az órák főként frontális oktatásra épülnek, ami kevésbé köti le a diákok figyelmét.
- Abból a célból, hogy óráinkat interaktívabbá tegyük, egy kvízt szeretnénk készíttetni.
- A tananyag ismétlése és számonkérése hagyományos formában történik, ami nem minden diáknak motiváló.
- A legjobban teljesítő diákokat jutalmaznánk, motiválva ezzel őket az órán való részvételre.
- A kvíz átfogó és változatos kérdéseket tartalmazzon, segítve ezzel az ismeretszerzést.
- A játék végeztével legyen lehetőségük átnézni a kérdésekre adott válaszokat, melyekből tanulhatnak.
- A tanulók aktivitása sokszor alacsony, és a visszajelzések lassan érkeznek a pedagógushoz.

## Jelenlegi üzleti folyamatok:
- Papíralapú felmérések
- Időigényes kiértékelés
- A kvízzel a gyerekek versenyszellemét is szeretnénk előcsalogatni.
- Túlságosan egysíkú pontrendszer
- Nehéz nyílvántartás
- Csalások kiküszöbölhetetlensége
- Manuálisan történő javítás
- Alacsony aktivitás
- Nem lehet értékelni a gyorsaságot
- Kérdések egyénileg összeválogatása


## Igényelt üzleti folyamatok:
- Webes megjelenítés
- Ranglista
- 20 másodperces időkeret
- Pontok nyílvántartása
- Kapott pontszám kiszámítása gyorsasághoz és helyességhez kötötten
- Utólagos áttekintés 

## Követelmény lista:
- A felhasználónak a játék kezdete előtt egy nevet kell megadnia, melyhez egy, az általa elért eredményt társítunk a játék végén.
- Egy játék 10 kérdésből áll.
- Az egy kérdésre kapott pontszám függ a válasz helyességétől és gyorsaságától is.
- Minden kérdéshez 4 válaszlehetőség tartozik, melyből pontosan 1 válasz helyes.
- A felhasználó kiválaszt egy választ, a program visszajelzést ad annak helyességéről és a kapott pontszámról.
- A program nyilvántartja a kör során megszerzett összpontszámot.
- A játék végeztével megjelenítődik képernyőn az elért pontszám, továbbá a korábbi játékosok nevei és pontszámai.
- A felhasználónak lehetősége van megtekinteni a kitöltött kvízt, ahol láthatja a hozzájuk tartozó helyes válaszokat is.
- A kérdések egy előre elkészítet json fájlból random kerülnek kiválasztásra.
- Egy kérdés megválaszolására 20 másodperc áll rendelkezésre.
