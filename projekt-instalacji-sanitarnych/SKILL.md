---
name: "projekt-instalacji-sanitarnych"
description: "Domyślna struktura, zawartość i formatowanie polskiego projektu technicznego instalacji sanitarnych (wod.-kan., c.o., kotłownia/źródło ciepła, wentylacja, kanalizacja deszczowa, przyłącza, studnia, zbiorniki) – opis techniczny z obliczeniami, spis rysunków, tabelki rysunkowe. Użyj, gdy użytkownik prosi o napisanie, uzupełnienie, sprawdzenie lub sformatowanie projektu/opisu technicznego branży sanitarnej, o szkielet takiego projektu, listę rysunków, obliczenia (zapotrzebowanie na wodę, DU, zasobnik c.w.u., naczynie wzbiorcze, zawór bezpieczeństwa, zbiornik deszczowy, bilans powietrza), albo o ocenę kompletności dokumentacji sanitarnej – nawet gdy nie padnie słowo \"skill\" ani \"szablon\"."
---

# Projekt techniczny instalacji sanitarnych – struktura i formatowanie

Skill opisuje, jak ma wyglądać **domyślny projekt techniczny branży sanitarnej** w Polsce: z czego się składa, w jakiej kolejności, jak go sformatować i co w każdej części musi się znaleźć. Powstał na podstawie trzech przykładów z folderu `Przykł` (dwa kompletne projekty domów jednorodzinnych: opis + rysunki, oraz warunki przyłączenia do sieci od gestora). Wzorzec jest więc sprawdzony praktyką, ale wywodzi się z małych budynków mieszkalnych – dla obiektów innego typu (np. budynek użyteczności publicznej, jak świetlica wiejska) trzeba go uzupełnić (patrz „Dostosowanie do obiektu”).

## Jak pracować

1. **Ustal dane wejściowe.** Zanim cokolwiek napiszesz, zbierz: obiekt i lokalizację (nr działki, obręb), inwestora, projektanta i jego uprawnienia, stadium (projekt techniczny / element projektu budowlanego), zakres branży, źródło ciepła, sposób zaopatrzenia w wodę i odprowadzania ścieków, wydane warunki przyłączenia. Braki wypisz jako pytania – nie zgaduj.
2. **Dobierz moduły.** Opis składa się z modułów instalacyjnych (woda, kanalizacja, c.o., kotłownia, wentylacja, deszczowa, studnia/zbiorniki). Włącz tylko te, które wchodzą w zakres. Szczegóły i kolejność: `references/struktura-opisu-technicznego.md`.
3. **Napisz część opisową** według szkieletu (rozdziały 1–5), a w każdym module trzymaj stały podział: dane ogólne → opis rozwiązań → materiały i wymagania → próby/odbiór → obliczenia.
4. **Policz i pokaż obliczenia** w formie „Założenia / Obliczenia / Dobrano…” – wzorce w `references/obliczenia-wzorce.md`. Liczby bierz z danych wejściowych lub z wykonanych obliczeń; wartości z przykładów służą tylko jako ilustracja formatu.
5. **Przygotuj część graficzną**: spis rysunków z symbolami S1…Sn, zawartość rysunków i tabelkę rysunkową – `references/formatowanie-i-rysunki.md`.
6. **Sprawdź** dokument z `references/lista-kontrolna.md` (numeracja, spójność liczb między opisem, obliczeniami i rysunkami, aktualność przepisów oraz obecność nagłówka z nazwą firmy na każdej stronie).

## Szkielet dokumentu (kolejność stała)

| Część | Zawartość |
|---|---|
| Spis zawartości | A. Część opisowa (rozdz. 1–5) oraz B. Część graficzna (lista rysunków z symbolami S1…Sn) |
| A. Część opisowa | 1. Przedmiot opracowania · 2. Podstawa opracowania · 3. Zakres opracowania · 4. Rozwiązania techniczne (moduły 4.1…4.n) · 5. Uwagi końcowe + blok podpisu projektanta |
| B. Część graficzna | Rzuty kondygnacji osobno dla każdej instalacji, schemat technologiczny źródła ciepła, profile podłużne sieci zewnętrznych, schematy studni i zbiorników |

W przykładach brakuje elementów, które w pełnym projekcie są wymagane lub zwyczajowe – dodaj je, oznaczając wyraźnie jako uzupełnienie: strona tytułowa (obiekt, adres, inwestor, stadium, branża, projektant, sprawdzający, data), oświadczenie projektanta i zaświadczenie o przynależności do izby / uprawnienia, wykaz załączników (warunki przyłączenia od gestora, mapa do celów projektowych). Zakres formalny potwierdź w aktualnych przepisach (patrz niżej), a nie z pamięci.

## Zasady formatowania w skrócie

Pełne reguły i wzory tabel: `references/formatowanie-i-rysunki.md`.

- **Nagłówek dokumentu (obowiązkowy):** w nagłówku strony (header) każdej strony dokumentu umieść nazwę firmy – dla tego użytkownika **„ProduktywnyProjektant”**. Nagłówek ma być prawdziwym nagłówkiem edytora (Word: Wstawianie → Nagłówek), a nie tekstem w treści, żeby powtarzał się automatycznie na wszystkich stronach i dało się go zmienić w jednym miejscu. Nazwa firmy powinna też trafić do wiersza nagłówkowego tabelki rysunkowej (w miejsce „nazwa i logo biura projektowego”). Jeśli użytkownik poda inną firmę lub wersję nazwy, użyj jej; nazwy nie wymyślaj ani nie skracaj.
- Strony A4 pionowo, marginesy ok. 25 mm, tekst wyjustowany, krój bezszeryfowy wąski (w przykładach Arial Narrow ok. 10–11 pt), bez ozdobników.
- Numeracja dziesiętna: `4.` → `4.1.` → `4.1.1`. Nagłówki rozdziałów **WIELKIMI LITERAMI, pogrubione**; nagłówki modułów (4.1, 4.2…) dodatkowo podkreślone; nagłówki obliczeń („DOBÓR ZASOBNIKA CWU”) pogrubione, kursywa, podkreślone.
- Listy wypunktowane myślnikiem „–”. Zalecenia dla wykonawcy w trybie rozkazującym („wykonać”, „zabezpieczyć”), opis rozwiązań w czasie przyszłym/rozkazującym („zaprojektowano”, „należy”).
- Obliczenia w blokach: wiersz = `symbol – opis` po lewej, wartość z jednostką po prawej; wynik i dobrany element **pogrubione**.
- Tabele z numerem porządkowym `Lp.`, jednostkami w nawiasach kwadratowych w drugim wierszu nagłówka (`[szt.]`, `[l/s]`), wiersz sum pogrubiony.
- Na końcu rozdziału 5: ramka z trzema polami – imię, nazwisko i tytuł projektanta | numer uprawnień | miejsce na podpis.
- Dodaj numerację stron (w przykładach jej nie widać – to uzupełnienie), najlepiej w stopce.

## Dostosowanie do obiektu

Przykłady to domy jednorodzinne (4 osoby, jedna kotłownia, jeden zasobnik). Przy innym obiekcie przemyśl, co dochodzi, i dopisz to jako osobne podrozdziały lub wymagania, zamiast naciągać wzorzec:

- **Budynek użyteczności publicznej / usługowy** (np. świetlica): liczba użytkowników liczona z funkcji i kubatury, a nie „4 osoby”; zestawienie przyborów dla toalet ogólnodostępnych, w tym dla osób z niepełnosprawnością; wentylacja wynikająca z funkcji pomieszczeń (sala, zaplecze kuchenne, WC), nie tylko rekuperacja domowa; zabezpieczenia przeciwpożarowe przejść instalacyjnych; instalacja wod.-kan. i c.o. dobierane do nierównomiernego użytkowania.
- **Inne źródło ciepła** (kocioł gazowy/LPG, pompa ciepła, pellet, sieć): moduł „Technologia kotłowni” dostosuj do źródła, łącznie z zabezpieczeniem (naczynie przeponowe lub otwarte), odprowadzeniem spalin i wentylacją pomieszczenia – przykłady pokazują dwa warianty (pompa ciepła powietrze–woda i kocioł na pellet).
- **Brak sieci** → studnia, zbiornik szczelny, ewentualnie oczyszczalnia. **Jest sieć** → przyłącze według warunków gestora; cytuj numer i datę warunków (patrz przykład 3: warunki przyłączenia wody z parametrami przyłącza, a kanalizacji – odmowa z wymogiem zaprojektowania odcinka sieci).

## Czego nie kopiować z przykładów

Przykłady są wzorcem układu, nie źródłem treści technicznych ani prawnych. Z analizy wynika, że:

- **Podstawy prawne i normy są w nich przestarzałe lub cytowane w wersjach z lat 1997–2008** (rozporządzenie w sprawie warunków technicznych z 2002 r. „wraz z późniejszymi zmianami”, PN-92/B-01706, PN-91/B-02413, PN-81/B-10700/01 i in.). Przed wpisaniem jakiejkolwiek podstawy prawnej lub normy sprawdź jej aktualny stan (np. narzędziami Repertorium dla aktów prawnych) i podaj źródło; w razie niepewności napisz to wprost i zostaw pole do weryfikacji. Normy PN-EN są objęte prawem autorskim i wymagają sprawdzenia aktualnego wydania.
- **Błędy redakcyjne**, które trzeba omijać: numeracja rozjeżdżająca się z nagłówkiem (w przykładzie 2 nagłówek „4.2.” prowadzi do „4.1.1”), literówki w nagłówkach („DANE OGÓLE”), niespójność określeń („projekt techniczny” vs „projekt budowlany”), opis „system otwarty” obok instalacji z naczyniem przeponowym w innym przykładzie, wzmianka o odrębnym opracowaniu przyłącza bez powołania się na dokument.
- **Zdania-wypełniacze** typu „Alternatywnie według uznania inwestora dopuszcza się wykonanie instalacji z rur tworzyw sztucznych…” – zostaw tylko, jeśli projektant faktycznie dopuszcza zamienniki i wskazuje warunek równoważności.
- **Wartości liczbowe z przykładów** (średnice, moce, pojemności, ilości) nie są wartościami domyślnymi. Każdą liczbę w nowym projekcie wyprowadź z danych lub z pokazanych obliczeń; jeśli jej nie masz, oznacz jako założenie do potwierdzenia przez projektanta.

## Wyniki i odpowiedzialność

Dokument jest roboczym projektem do sprawdzenia przez uprawnionego projektanta – nie zastępuje jego podpisu, uprawnień ani obliczeń wykonanych w programach branżowych. Pisząc, oddzielaj to, co wynika z danych projektu, od własnych założeń i sugestii; niespójności w dokumentacji zgłaszaj jako pytania do projektanta. Domyślny format pliku: dokument edytowalny (Word .docx lub dokument online), chyba że użytkownik wskaże inaczej; rysunki dostarcza projektant (CAD) – skill opisuje ich zawartość i tabelkę, nie generuje rzutów.