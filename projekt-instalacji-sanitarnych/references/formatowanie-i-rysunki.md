# Formatowanie dokumentu i część graficzna

Spis treści:
1. Strona i typografia
2. Nagłówki i numeracja
3. Listy, tabele, bloki obliczeń
4. Spis zawartości i lista rysunków
5. Rysunki – format, zawartość, oznaczenia
6. Tabelka rysunkowa (blok tytułowy)
7. Profile podłużne sieci
8. Dokumenty dołączane (warunki przyłączenia)

Opis pochodzi z oględzin przykładów 1–3 z folderu `Przykł`; wartości wymiarowe są przybliżone.

## 1. Strona i typografia

- Część opisowa: A4 pionowo, marginesy lewy i prawy ok. 25 mm.
- Krój bezszeryfowy wąski (w przykładach Arial Narrow), wielkość ok. 10–11 pt, tekst wyjustowany, interlinia pojedyncza z odstępem między akapitami.
- Wyróżnienia: pogrubienie dla wyników, dobranych elementów i kluczowych zaleceń (np. zdanie o możliwości zamiany materiałów, słowo „RÓWNOWAŻNE”). Nie nadużywaj – wyróżniona ma być rzecz, której wykonawca nie może przeoczyć.
- Przykłady nie mają widocznej numeracji stron; dodaj numerację „strona x z y” i krótką stopkę z nazwą obiektu i branży (uzupełnienie).

## 2. Nagłówki i numeracja

| Poziom | Wygląd | Przykład |
|---|---|---|
| Część | pogrubiony, wersaliki | `A. CZĘŚĆ OPISOWA`, `B. CZĘŚĆ GRAFICZNA` |
| Rozdział | pogrubiony, wersaliki | `1. PRZEDMIOT OPRACOWANIA`, `4. ROZWIĄZANIA TECHNICZNE` |
| Moduł 4.x | pogrubiony, wersaliki, podkreślony | `4.1. INSTALACJA WODY ZIMNEJ, CIEPŁEJ WODY UŻYTKOWEJ, CYRKULACYJNEJ.` |
| Podpunkt 4.x.y | pogrubiony, wersaliki | `4.1.1 DANE OGÓLNE`, `4.1.4 OBLICZENIA` |
| Obliczenie | pogrubiony, kursywa, podkreślony, wersaliki | `DÓBÓR ZASOBNIKA CWU` |
| Podtytuł w treści | pogrubiona kursywa bez numeru | `Organizacja wymiany powietrza w pomieszczeniach.` |

Numeracja musi być **ciągła i zgodna ze spisem** (w przykładzie 2 nagłówek 4.2 prowadzi do podpunktów 4.1.1–4.1.3 – to błąd). Najlepiej użyć automatycznej numeracji wielopoziomowej w edytorze. Po numerze rozdziału kropka, po numerze podpunktu zwykle bez kropki – wybierz jeden wariant i trzymaj go w całym dokumencie.

## 3. Listy, tabele, bloki obliczeń

- **Lista:** myślnik „–”, wcięcie, każdy punkt kończy się przecinkiem, ostatni kropką/średnikiem zgodnie z konwencją dokumentu.
- **Tabela przyborów / bilansu / izolacji:** pierwsza kolumna `Lp.`; nagłówek w dwóch wierszach – nazwa, a pod nią jednostka w nawiasie kwadratowym (`[-]`, `[szt.]`, `[l/s]`); ramka cienka, wiersze podsumowujące (suma, przepływ obliczeniowy) pogrubione i wyrównane do prawej; bilans powietrza ma wiersze nagłówkowe pięter (PARTER / PODDASZE).
- **Tabela izolacji cieplnej:** `Lp. | Rodzaj przewodu lub komponentu | Minimalna grubość izolacji cieplnej (materiał λ = 0,035 W/m·K)` – wartości z aktualnych warunków technicznych.
- **Tabela mocowań kanalizacji:** wiersze „rury w poziomie” i „rury w pionie” dla DN 40–160.
- **Bloki „Założenia / Obliczenia”:** patrz `obliczenia-wzorce.md`.

## 4. Spis zawartości i lista rysunków

Pierwsza strona (po stronie tytułowej, jeśli ją dodajesz): tytuł „S P I S  Z A W A R T O Ś C I” rozstrzelony. Poniżej:

```
A. CZĘŚĆ OPISOWA
 1. Przedmiot opracowania
 2. Podstawa opracowania
 3. Zakres opracowania
 4. Rozwiązania techniczne
 5. Uwagi końcowe

B. CZĘŚĆ GRAFICZNA
 1. Rzut parteru – instalacja c.o.                     S1
 2. Rzut poddasza – instalacja c.o.                    S2
 ...
```

Symbol rysunku (S1, S2…) w tym samym brzmieniu co w tabelce rysunkowej. Rozdziały opisu w spisie zapisuj zwykłą wielkością liter, w opisie wersalikami.

Wykaz rysunków w przykładach (układ do skopiowania, nie lista obowiązkowa):
- rzuty parteru i poddasza osobno dla c.o., wod.-kan., wentylacji (rzut „poziom sufitu” i „poziom posadzki”),
- schemat technologiczny kotłowni (pompa ciepła lub pellet),
- profile podłużne: instalacja deszczowa, kanalizacja sanitarna, wodociąg,
- schemat studni głębinowej, schematy zbiorników (ścieki sanitarne, wody opadowe).

Dla budynku z piwnicą lub wielu kondygnacji dodaj rzuty tych kondygnacji; dla sieci zewnętrznych – plan zagospodarowania/sytuacyjny z trasami sieci (w przykładach go nie ma, a jest potrzebny, by wykonawca zlokalizował przyłącza i zbiorniki) – oznacz to jako uzupełnienie.

## 5. Rysunki – format, zawartość, oznaczenia

- Format: duży arkusz poziomo (w przykładzie ok. 504 × 420 mm); jeden rysunek na arkusz; w prawym dolnym rogu tabelka rysunkowa.
- Rzuty w skali 1:50 na podkładzie architektonicznym; instalacje w różnych kolorach (np. c.o. – czerwony/niebieski, woda – niebieski i inne, kanalizacja – brązowy, wentylacja – zielony), legenda na arkuszu.
- **Legenda** na każdym rzucie: symbol – opis (np. „PC.1 – proj. jednostka zewnętrzna powietrznej pompy ciepła o mocy …”, „P.CO – proj. pion instalacji c.o.”); dla rurociągów materiał i średnica.
- **Oznaczenia pomieszczeń** (c.o.): numer pomieszczenia i temperatura obliczeniowa (np. „1.3 +20 °C”), obliczeniowa moc grzewcza w watach; **pętle ogrzewania podłogowego**: oznaczenie pętli, powierzchnia, rozstaw.
- Rzuty wod.-kan.: przybory, piony, poziomy, średnice, rozdzielacze, zawory, czyszczaki, wpusty, przejścia przez przegrody, miejsce wejścia przyłącza.
- Rzuty wentylacji: centrala, kanały z średnicami, skrzynki rozdzielcze i rozprężne, anemostaty z przepływami, czerpnia i wyrzutnia.
- Schemat technologiczny źródła ciepła: wszystkie urządzenia, armatura, zabezpieczenia, parametry, legenda.
- Numer rysunku (S…) i jego tytuł muszą być identyczne na rysunku, w spisie i w tekście, który się do niego odwołuje.

## 6. Tabelka rysunkowa

Prostokątny blok w prawym dolnym rogu, od góry:

| Wiersz | Zawartość |
|---|---|
| Nagłówek (tło szare) | nazwa i logo biura projektowego, telefon, strona www |
| STADIUM | np. PROJEKT TECHNICZNY (lub: PROJEKT BUDOWLANY – zgodnie ze stadium dokumentacji) |
| TREŚĆ | nazwa rysunku, np. RZUT PARTERU / INSTALACJA C.O. |
| OBIEKT | nazwa obiektu |
| ADRES | miejscowość, nr działki, obręb, gmina |
| INWESTOR | nazwa/imię i nazwisko, adres |
| PROJEKTANT (br. sanitarna) | imię i nazwisko z tytułem, numer uprawnień, zakres uprawnień, pole PODPIS |
| (wiersz pusty) | w przykładzie niewykorzystany – można użyć na sprawdzającego |
| DATA / SKALA | data opracowania (miesiąc i rok), skala rysunku |
| Program / RYSUNEK | nazwa programu CAD i licencja; numer rysunku (S1 …) |

Wszystkie dane (obiekt, adres, inwestor, data) muszą być identyczne na wszystkich arkuszach i na stronie tytułowej.

## 7. Profile podłużne sieci

Profil podłużny to rysunek z rzędnymi, a pod nim tabela o stałych wierszach (z przykładów):

1. RZĘDNA TERENU
2. RZĘDNA DNA KANAŁU
3. ZAGŁĘBIENIE DNA KANAŁU
4. SPADKI, DŁUGOŚCI
5. ŚREDNICA, MATERIAŁ
6. ODLEGŁOŚCI
7. HEKTOMETRY (pikietaż; punkty oznaczone symbolami, np. ZD – zbiornik deszczowy, T – trójnik, K – kolano, R – rewizja/studzienka)

Na rysunku: oś pionowa z rzędnymi odniesienia, przecięcia z innymi sieciami (kolizje), studnie i zbiorniki, spadki w % i długości odcinków w m. Spadki i długości z tabeli muszą być zgodne z opisem (np. minimalny spadek kolektora).

## 8. Dokumenty dołączane (przykład 3)

Pisma gestora sieci (np. spółki komunalnej) dołącz w załącznikach i cytuj w „Podstawie opracowania” z numerem i datą. Z przykładu 3 wynika, co z nich wyciągnąć do projektu:

- **Warunki przyłączenia do sieci wodociągowej:** zapotrzebowanie wody (m³/d), z jakiej sieci i z której działki wykonać przyłącze, średnica i materiał przyłącza (np. PE 100 SDR 11 PN 16), kto montuje wodomierz, granica odpowiedzialności (zawór za wodomierzem głównym), tryb zgłoszenia (projekt przyłącza lub plan sytuacyjny – zależnie od trybu zgłoszenia), termin ważności warunków (w przykładzie dwa lata), wymóg zgłoszenia do odbioru i podpisania umowy.
- **Odmowa przyłączenia do kanalizacji:** powód (brak sieci), wymagane zaprojektowanie i wybudowanie odcinka sieci i przyłącza – to uzasadnia w projekcie zbiornik szczelny albo wymaga rozszerzenia zakresu.

Dane z tych pism muszą być spójne z częścią opisową (średnica przyłącza, materiał, zapotrzebowanie wody). Przykład: warunki dla działki z przykładu 1 wskazują zapotrzebowanie 0,5 m³/d, a obliczenia w opisie dają Qśr d = 0,40 m³/d i Qmax d = 0,52 m³/d – w nowym projekcie wyraźnie napisz, która wartość została zgłoszona gestorowi i jak się ma do obliczeń.
