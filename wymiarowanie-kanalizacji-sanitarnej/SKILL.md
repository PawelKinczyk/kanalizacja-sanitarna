---
name: "wymiarowanie-kanalizacji-sanitarnej"
description: "Wymiarowanie wewnętrznej kanalizacji sanitarnej grawitacyjnej wg PN-EN 12056-2 – odpływy jednostkowe DU, współczynnik częstości K, natężenie Qww/Qtot, średnice i ograniczenia podejść (wentylowanych i niewentylowanych, systemy I–IV), kontrola odpływów i przewodów zbiorczych. Użyj zawsze, gdy użytkownik prosi o dobór średnic kanalizacji, obliczenie przepływu ścieków, sprawdzenie podejść do przyborów, spadków, długości, łuków, wentylacji podejść, o część obliczeniową opisu technicznego kanalizacji lub o ocenę, czy DN100/DN50 wystarczy – nawet gdy nie pada nazwa normy."
---

# Wymiarowanie kanalizacji sanitarnej wewnętrznej (PN-EN 12056-2)

Skill prowadzi przez dobór średnic i sprawdzenie ograniczeń instalacji kanalizacji grawitacyjnej wewnątrz budynku. Opiera się na materiale dydaktycznym instsani.pl („Wymiarowanie przewodów kanalizacyjnych wg PN-EN 12056-2:2002” i „Wyznaczanie przepływu obliczeniowego ścieków sanitarnych”), zapisanym tu własnymi słowami i tabelami liczbowymi.

## Krok 0 – zanim zaczniesz jakąkolwiek pracę: zapytaj o system kanalizacji

Zawsze, jako pierwszą czynność, zapytaj użytkownika, w jakim systemie kanalizacyjnym (I, II, III czy IV wg PN-EN 12056-2) realizowany jest projekt. Zrób to nawet wtedy, gdy wydaje Ci się, że system wynika z dokumentacji albo z wcześniejszej rozmowy. Powód: system decyduje o wartościach DU, o tabelach doboru podejść i o ograniczeniach (tab. 4–9), więc błędne założenie unieważnia cały wynik, a różnica jest niewidoczna na pierwszy rzut oka. Pytanie kosztuje użytkownika kilka sekund, a poprawka po fakcie – całe obliczenia.

- Użyj AskUserQuestion z opcjami: system I, system II, system III, system IV (użytkownik może wpisać własną odpowiedź). Jeżeli dokumentacja projektu wskazuje system, wymień go jako pierwszą opcję z dopiskiem „(wg dokumentacji)” i podaj, skąd to wiesz – ale i tak zapytaj o potwierdzenie.
- Nie zaczynaj liczenia, nie uruchamiaj skryptu i nie twórz plików, dopóki nie dostaniesz odpowiedzi.
- Przy okazji możesz zadać (w tym samym pytaniu) pozostałe brakujące dane z sekcji „Dane wejściowe”, np. współczynnik K, ale pytanie o system jest obowiązkowe.
- Jeśli nie ma kogo zapytać (uruchomienie bez udziału użytkownika, zadanie zaplanowane), przyjmij roboczo system I, napisz to na samym początku wyniku jako założenie do potwierdzenia i oznacz je w pliku Excel.
- Wybrany system zapisz w obliczeniach i w pliku Excel (arkusz Założenia); wszystkie DU i tabele bierz z kolumny/tabeli tego systemu.

## Co jest w źródle, a czego nie ma (ważne dla uczciwości obliczeń)

- **Jest:** wzory na Qww i Qtot, tabela DU (systemy I–IV), współczynniki K, średnice i ograniczenia **podejść** (systemy I, II, IV – tab. 4, 5, 7, 8; system III – tab. 6 i 9).
- **Nie ma wartości liczbowych dla pionów i odpływów** (strona zawiera tylko nagłówki tych zakładek). Dla pionów wartości Qmax bierz z normy PN-EN 12056-2 albo z danych producenta rur; **nie zgaduj** (zasada projektu: liczby tylko z dokumentacji lub z pokazanych obliczeń). Odpływy/przewody zbiorcze policz hydraulicznie (sekcja 4) z jawnie podanymi założeniami.
- Norma PN-EN 12056-2:2002 i wskazane w niej tablice mogły zostać zmienione; przed wpisaniem do projektu sprawdź aktualną wersję normy i krajowe wymagania (WT). Strona jest pomocą naukową dla uczniów – nie zastępuje normy.
- W źródle znalazł się błąd: w tabeli Qww dla ΣDU = 200 i K = 0,5 stoi 7,6, a ze wzoru wychodzi 7,07 dm³/s. Dlatego **Qww zawsze licz ze wzoru**, nie odczytuj z tabeli.

## Dane wejściowe – zbierz przed liczeniem

Jeśli czegoś brakuje w dokumentacji, zapytaj albo oznacz jako założenie do potwierdzenia:

1. **System kanalizacji (I, II, III lub IV)** – ustalony w kroku 0.
2. **Przeznaczenie i sposób korzystania** → K (tab. 2).
3. **Wykaz pomieszczeń i przyborów (emiterów ścieków)** – dla każdego pomieszczenia liczba i typ przyborów (WC wg pojemności spłuczki, umywalki, pisuary, wpusty DN, zlewy, zmywarki, pralki…). To jest podstawa pliku Excel opisanego niżej.
4. **Geometria każdego podejścia**: długość L, liczba łuków 90°, różnica wysokości H, planowany spadek.
5. **Przepływy dodatkowe**: ciągłe Qc (np. skropliny, odpływ z urządzeń), pompowane Qp (pompownie, przepompownie ścieków).
6. **Materiał rur** i średnice wewnętrzne (dane producenta) do kontroli hydraulicznej.

## Algorytm

### 1. Natężenie przepływu

Qww = K · √ΣDU [dm³/s]  
Qtot = Qww + Qc + Qp [dm³/s]

Przyjmowana do doboru średnicy przepustowość nie może być mniejsza niż (a) obliczone Qww lub Qtot, ani (b) największy odpływ jednostkowy DU spośród przyborów na danym odcinku. Czyli licz Q = max(Qww; DU_max). Dla pojedynczego przyboru Q = DU tego przyboru (np. WC 6 l w systemie I → 2,0 dm³/s).

**Tab. 2 – współczynnik częstości K**

| Sposób korzystania | K |
|---|---|
| nieciągłe (mieszkanie, pensjonat, biuro) | 0,5 |
| okresowe (szpital, szkoła, restauracja, hotel) | 0,7 |
| zbiorowe (publiczne toalety i natryski) | 1,0 |
| specjalne (laboratoria) | 1,2 |

Świetlica wiejska/obiekt użyteczności publicznej: dobór K (0,7 czy 1,0) wymaga decyzji projektanta na podstawie użytkowania – wskaż to jako założenie i podaj wynik dla obu, jeśli to istotne.

**Tab. 1 – odpływy jednostkowe DU [dm³/s] wg systemu**

| Przybór | I | II | III | IV |
|---|---|---|---|---|
| Umywalka, bidet | 0,5 | 0,3 | 0,3 | 0,3 |
| Natrysk bez korka | 0,6 | 0,4 | 0,4 | 0,4 |
| Natrysk z korkiem | 0,8 | 0,5 | 1,3 | 0,5 |
| Pojedynczy pisuar ze zbiornikiem | 0,8 | 0,5 | 0,4 | 0,5 |
| Pisuar z zaworem spłukującym | 0,5 | 0,3 | – | 0,3 |
| Pisuar płytowy (na osobę) | 0,2 | 0,2 | 0,2 | 0,2 |
| Wanna | 0,8 | 0,6 | 1,3 | 0,5 |
| Zlew kuchenny | 0,8 | 0,6 | 1,3 | 0,5 |
| Zmywarka domowa | 0,8 | 0,6 | 0,2 | 0,5 |
| Pralka automatyczna do 5 kg | 0,8 | 0,6 | 0,6 | 0,5 |
| Pralka automatyczna do 12 kg | 1,5 | 1,2 | 1,2 | 1,0 |
| Ustęp, zbiornik 4,0 l | nie zal. | 1,8 | nie zal. | nie zal. |
| Ustęp, zbiornik 6,0 l | 2,0 | 1,8 | 1,2–1,7 | 2,0 |
| Ustęp, zbiornik 7,5 l | 2,0 | 1,8 | 1,4–1,8 | 2,0 |
| Ustęp, zbiornik 9,0 l | 2,5 | 2,0 | 1,6–2,0 | 2,5 |
| Wpust podłogowy DN 50 | 0,8 | 0,9 | – | 0,6 |
| Wpust podłogowy DN 70 | 1,5 | 0,9 | – | 1,0 |
| Wpust podłogowy DN 100 | 2,0 | 1,2 | – | 1,3 |

„–” = nie stosowane lub brak danych. Zakresy ustępów w systemie III zależą od typu spłuczki (tylko ustęp ze zbiornikiem z syfonem): dla bezpieczeństwa przyjmij górną wartość i zaznacz to w obliczeniach.

### 2. Podejścia (przewód od przyboru do pionu)

Zasady ogólne:
- Średnica podejścia **nie może być mniejsza niż średnica wylotu z przyboru** (np. WC o wylocie 100 → min. DN100, niezależnie od tabeli).
- Podejście **niewentylowane** = brak osobnego przewodu wentylacyjnego lub zaworu napowietrzającego na końcu podejścia. Gdy ograniczeń nie da się dotrzymać: zastosuj podejście wentylowane, większą średnicę albo zawór napowietrzający.

#### Systemy I, II, IV – niewentylowane (tab. 4 i 5)

Wybierz pierwszy wiersz, w którym Qmax ≥ Q. „n.z.” = nie zaleca się (przejdź do następnego wiersza).

| Qmax [dm³/s] | DN sys. I | DN sys. II | DN sys. IV |
|---|---|---|---|
| 0,40 | n.z. | 30 | 30 |
| 0,50 | 40 | 40 | 40 |
| 0,80 | 50 | n.z. | n.z. |
| 1,00 | 60 | 50 | 50 |
| 1,50 | 70 | 60 | 60 |
| 2,00 | 80 ᵃ | 70 ᵃ | 70 ᵃ |
| 2,25 | 90 ᵇ | 80 ᶜ | 80 ᶜ |
| 2,50 | 100 | 90 | 100 |

ᵃ bez ustępów spłukiwanych; ᵇ max 2 ustępy spłukiwane i całkowita zmiana kierunku ≤ 90°; ᶜ max 1 ustęp spłukiwany.

| Ograniczenie (niewentylowane) | I | II | IV |
|---|---|---|---|
| L max | 4,0 m | 10,0 m | 10,0 m |
| Liczba łuków 90° max (bez łuku łącznikowego) | 3 | 1 | 3 |
| H max (odchylenie ≥ 45°) | 1,0 m | 6,0 m dla DN > 70; 3,0 m dla DN 70 | 1,0 m |
| Spadek min | 1,00 % | 1,50 % | 1,00 % |

Dodatkowo: jeśli DN < 100 i do podejścia włączono ustęp spłukiwany, to powyżej 1 m nad włączeniem do systemu wentylującego nie wolno podłączać żadnych innych urządzeń.

#### Systemy I, II, IV – wentylowane (tab. 7 i 8)

Wartości: DN podejścia / DN przewodu wentylacyjnego.

| Qmax [dm³/s] | sys. I | sys. II | sys. IV |
|---|---|---|---|
| 0,60 | n.z. | 30/30 | 30/30 |
| 0,75 | 50/40 | 40/30 | 40/30 |
| 1,50 | 60/40 | 50/30 | 50/30 |
| 2,25 | 70/50 | 60/30 | 60/30 |
| 3,00 | 80/50 ᵃ | 70/40 ᵃ | 70/40 ᵃ |
| 3,40 | 90/60 ᵇ | 80/40 ᶜ | 80/40 ᶜ |
| 3,75 | 100/60 | 90/50 | 90/50 |

| Ograniczenie (wentylowane) | I | II | IV |
|---|---|---|---|
| L max | 10,0 m | bez ograniczeń | 10,0 m |
| Liczba łuków 90° max | bez ograniczeń | bez ograniczeń | bez ograniczeń |
| H max | 3,0 m | 3,0 m | 3,0 m |
| Spadek min (bez łuku przyłączeniowego) | 0,50 % | 1,50 % | 0,50 % |

#### System III – dobór wg rodzaju przybora (tab. 6 niewentylowane, tab. 9 wentylowane)

Kolumny: DN | min. zamknięcie wodne [mm] | L max od wylotu syfonu do pionu [m] | spadek [%] | max liczba łuków | H max [m]. „b.o.” = bez ograniczeń.

Niewentylowane (tab. 6):

| Przybór | DN | Zamkn. wodne | L max | Spadek | Łuki | H |
|---|---|---|---|---|---|---|
| Umywalka, bidet (syfon 30 mm) | 30 | 75 | 1,7 | 2,2 ¹ | 0 | 0 |
| tamże | 30 | 75 | 1,1 | 4,4 ¹ | 0 | 0 |
| tamże | 30 | 75 | 0,7 | 8,7 ¹ | 0 | 0 |
| Umywalka, bidet | 40 | 75 | 3 | 1,8–4,4 | 2 | 0 |
| Natrysk, wanna | 40 | 50 | b.o. ² | 1,8–9,0 | b.o. | 1,5 |
| Pisuar muszlowy | 40 | 75 | 3,0 ³ | 1,8–9,0 | b.o. ⁴ | 1,5 |
| Pisuar korytowy | 50 | 75 | 3,0 ³ | 1,8–9,0 | b.o. ⁴ | 1,5 |
| Pisuar płytowy ⁵ | 60 | 50 | 3,0 ³ | 1,8–9,0 | b.o. ⁴ | 1,5 |
| Zlew kuchenny (syfon 40 mm) | 40 | 75 | b.o. ² | 1,8–9,0 | b.o. | 1,5 |
| Zmywarka, pralka | 40 | 75 | 3 | 1,8–4,4 | b.o. | 1,5 |
| Ustęp spłukiwany, wylot ≤ 80 mm ⁶ | 75 | 50 | b.o. | min 1,8 | b.o. ⁴ | 1,5 |
| Ustęp spłukiwany, wylot > 80 mm ⁶ | 100 | 50 | b.o. | min 1,8 | b.o. ⁴ | 1,5 |
| Urządzenie do odpadków żywnościowych ⁷ | min 40 | 75 ⁸ | 3 ³ | min 13,5 | b.o. ⁴ | 1,5 |
| Urządzenie do usuwania podpasek | min 40 | 75 ⁸ | 3,0 ³ | min 5,4 | b.o. ⁴ | 1,5 |
| Wpust podłogowy | 50 / 70 / 100 | 50 | b.o. ³ | min 1,8 | b.o. | 1,5 |
| 4 miski | 50 | 75 | 4 | 1,8–4,4 | 0 | 0 |
| Pisuary muszlowe ⁸ | 50 | 75 | b.o. ³ | 1,8–9,0 | b.o. ⁴ | 1,5 |
| Maks. 8 ustępów spłukiwanych ⁶ | 100 | 50 | 15 | 0,9–9,0 | 2 | 1,5 |
| Do 5 misek z zaworem natryskowym | maks. 30 | 50 | 4,5 ³ | 1,8–4,4 | b.o. ⁴ | 0 |

Wentylowane (tab. 9) – inne niż powyżej: brak wiersza umywalki DN40 i trzeciego wiersza umywalki DN30 (0,7 m / 8,7 %); wpust wannowy i podłogowy DN50 łącznie; 5 misek (DN50, 75 mm, L 4 m, 1,8–4,4 %, 0 łuków, H 0) oraz 10 misek (każda miska wentylowana indywidualnie ⁹ ᐧ ¹⁰); pisuary muszlowe w dowolnej liczbie ⁹ ᐧ ¹¹; „więcej niż 8 ustępów spłukiwanych” (DN100, 50 mm, L 15 m, 0,9–9,0 %, 2 łuki, H 1,5); ustępy z uwagą ¹⁴ (DN50 przewodu wentylacyjnego do 50 mm powyżej poziomu przelewu, gdy podłączenia wentylacyjne są podatne na zablokowanie przez powtarzane spłukiwanie lub podtopienie); przewody wentylujące podejścia do urządzeń mogą mieć DN25, lecz przy długości > 15 m lub > 5 łuków – DN30 ¹³. Pozostałe wiersze jak w tab. 6.

Uwagi do tab. 6 i 9: ¹ dotyczy maks. odległości między syfonem a przewodem wentylacyjnym; ² przy długości > 3 m głośny odpływ może zassać wodę z syfonu i grozi zablokowaniem; ³ długość możliwie najkrótsza (osady); ⁴ unikać ostrych, zwężonych łuków; ⁵ pisuar korytowy do 7 osób, dłuższe koryta – więcej niż jeden wylot; ⁶ podejścia z łagodnymi odgałęzieniami obsługujące ustępy; ⁷ uwzględnia małe urządzenia do obierania ziemniaków; ⁸ syfony rurowe (nie butelkowe ani ponownie napełniane); miski z zaworem natryskowym powinny mieć możliwość stopniowego spłukiwania ścieków bez korków.

Jeśli parametry przekraczają limity z tabel (np. L = 6 m dla podejścia niewentylowanego sys. I), **nie „naciągaj”** – zaproponuj: podejście wentylowane, zawór napowietrzający, większe DN lub zmianę trasy.

### 3. Piony

- Wartości Qmax pionów (dla danego DN, rodzaju wentylacji i systemu) weź z PN-EN 12056-2 lub od producenta rur. Podaj źródło i tablicę; jeżeli ich nie masz, napisz to wprost i wstaw pole „UZUPEŁNIĆ” zamiast liczby.
- Zasady ogólne do potwierdzenia w normie: pion nie może mieć średnicy mniejszej niż największe podłączone podejście/odpływ; nie zmniejszaj średnicy w kierunku przepływu; przy przesunięciu (odsadzce) uwzględnij wymagania normy.
- Wentylacja pionu: pion wyprowadzony ponad dach (rura wywiewna) lub wentylacja uzupełniająca – zgodnie z projektem i przepisami (sprawdź aktualne WT).

### 4. Odpływy (poziomy podposadzkowe i zbiorcze)

Źródło nie podaje wartości liczbowych. Policz hydraulicznie lub użyj tablic normy/producenta:

- Zadany Q (max z Qww/Qtot i DU_max), spadek i napełnienie h/d (domyślnie 0,5 – założenie do potwierdzenia w normie).
- Prędkość i przepływ dla częściowo napełnionej rury kołowej: kąt środkowy θ = 2·arccos(1 − 2·h/d); A = d²/8·(θ − sin θ); P = d·θ/2; R = A/P; Dh = 4R; λ z Colebrooka-White’a: 1/√λ = −2·log10(k/(3,71·Dh) + 2,51/(Re·√λ)); v = √(8·g·R·I/λ); Q = v·A.
- Założenia, które musisz jawnie wypisać w wyniku: chropowatość k (domyślnie 1,0 mm), średnice wewnętrzne rur wg producenta (nie nominalne DN – różnica kilku % średnicy daje ok. 15–20 % przepustowości), temperatura ścieków (ν = 1,31·10⁻⁶ m²/s przy 10 °C).
- Kontrole: v ≥ ok. 0,7 m/s (samooczyszczanie, wartość orientacyjna do potwierdzenia), DN nie mniejsza niż DN dopływów, nie zmniejszać w kierunku przepływu, spadek zgodny z wymaganiami normy i WT.
- **Skrypt obliczeniowy jest częścią skilla** (`scripts/kanalizacja_wymiarowanie.py` w katalogu skilla – działa w każdym projekcie, nie wymaga plików projektu ani bibliotek). Uruchamiaj go z katalogu skilla podanego w nagłówku „Base directory”: `python3 -I <katalog skilla>/scripts/kanalizacja_wymiarowanie.py <podkomenda> ...`. Zamiast samodzielnie liczyć ręcznie, użyj go – wyniki są powtarzalne i bez pomyłek arytmetycznych.
  - `du --system 1..4 --uzytkowanie nieciagle|okresowe|zbiorowe|specjalne|<K> --items '{"wc_6l":3,"umywalka":4}' [--qc X --qp Y]` → ΣDU, Qww, Q przyjęte (max z Qww i DU_max), Qtot. Klucze przyborów: umywalka, natrysk_bez_korka, natrysk_z_korkiem, pisuar_zbiornik, pisuar_zawor, pisuar_plytowy_os, wanna, zlew, zmywarka, pralka_5kg, pralka_12kg, wc_4l, wc_6l, wc_7_5l, wc_9l, wpust_dn50, wpust_dn70, wpust_dn100.
  - `podejscie --system 1|2|4 [--wentylowane] --q Q [--l L --luki N --h H --spadek %]` → DN (i DN przewodu wentylacyjnego) z tab. 4/7 oraz kontrola ograniczeń tab. 5/8. System III: skrypt odsyła do tab. 6 i 9 z tego pliku (dobór wg rodzaju przyboru).
  - `odplyw --q Q --spadek % [--wypelnienie 0.5 --k 1.0 --di mm --dn-min 50 --v-min 0.7]` → najmniejsza średnica z typowej tabeli PVC (lub jedna `--di` z danych producenta), prędkość, rzeczywiste napełnienie. Średnice wewnętrzne i k to **założenia** – zawsze je wypisz w wyniku.
  - Skrypt nie zastępuje oceny: sprawdź uwagi do tabel, średnicę wylotu przyboru i wymagania normy/WT.

## Zestawienie w Excelu – domyślny produkt każdego obliczenia

Po ustaleniu systemu i zebraniu wykazu przyborów **zawsze twórz plik Excel** z zestawieniem pomieszczeń i urządzeń (emiterów ścieków) ze wskazaniem odpływu jednostkowego DU każdego przyboru. Robisz to domyślnie, bez czekania na prośbę: inżynier potrzebuje tej tabeli do opisu technicznego, do weryfikacji z projektantem i do szybkiego przeliczenia po zmianie wykazu przyborów, a tabela wklejona w odpowiedź tego nie zapewnia. Pominąć plik możesz tylko wtedy, gdy użytkownik wprost o to poprosi.

**Gdzie zapisać:** w folderze projektu przeznaczonym na obliczenia (jeśli projekt ma `Claude.md` lub podobny plik z opisem struktury folderów, trzymaj się go – zwykle `obliczenia/`). Jeśli takiego folderu nie ma, zapisz w katalogu roboczym. Zapisuj jako nowy plik obok istniejących; nie nadpisuj i nie zmieniaj oryginalnych dokumentów projektu. Nazwa: `Scieki_wg_pomieszczen_<obiekt>.xlsx` (bez polskich znaków i spacji w nazwie pliku). Gdy projekt ma listę plików (np. w `Claude.md`), zaproponuj dopisanie nowego pliku.

**Jak zbudować:** wczytaj skill `xlsx` (openpyxl, formuły, przeliczenie `recalc.py`, zero błędów formuł, czcionka Arial). Liczby mają wynikać z formuł, nie z wartości wklejonych z Pythona, żeby arkusz przeliczał się po zmianie danych. Niebieskie komórki = dane wejściowe (liczby przyborów, K, DU), czarne = formuły.

Układ arkuszy (trzymaj się go, żeby pliki z różnych projektów były porównywalne):

1. **Podsumowanie** – ΣDU, DU_max, Qww i Q przyjęte dla każdego scenariusza i dla każdego rozważanego K (np. 0,7 i 1,0); kluczowy wynik wyróżniony; krótka uwaga, czego nie uwzględniono (Qc, Qp, przybory bez danych).
2. **Założenia** – wybrany system (I–IV) i skąd wiadomo, wartości K z uzasadnieniem, tabela DU **dla wybranego systemu** (przybory z kolumny tego systemu, z wartościami edytowalnymi), wzory, źródła (PN-EN 12056-2:2002 w brzmieniu do sprawdzenia, instsani.pl), zastrzeżenia.
3. **Emitery** – jedna linia na parę pomieszczenie × przybór: lp., pomieszczenie, strefa, przybór (lista rozwijana z arkusza Założenia), liczba, **DU jednostkowe pobierane z tabeli DU** (INDEX/MATCH), ΣDU = liczba × DU, DU maks. wiersza; wiersz sumy. Jeżeli wykaz przyborów jest niepewny, dodaj osobną kolumnę liczby dla scenariusza alternatywnego (np. z umywalkami), zamiast zgadywać.
4. **Pomieszczenia** – jedna linia na pomieszczenie: liczba ustępów, pisuarów, umywalek itd., ΣDU, DU maks., Qww i Q przyjęte (dla każdego K), udział w ΣDU budynku. Zaznacz w opisie, że przepływy pomieszczeń się nie sumują – sumuje się ΣDU.

Przed oddaniem przeliczaj plik (`recalc.py`), sprawdź kilka komórek względem wyniku skryptu `du` (powinny się zgadzać co do 0,01 dm³/s) i dopiero wtedy podaj wynik. Do odpowiedzi w rozmowie wystarczy krótki wynik kluczowy i wskazanie pliku – nie powtarzaj całej tabeli.

## Format odpowiedzi

Zawsze podaj w tej kolejności (najpierw wykonaj krok 0 – pytanie o system):

1. **Założenia** (system, K, przybory, materiał, wypełnienie, k) – oznacz, co pochodzi z dokumentacji projektu, a co jest założeniem własnym.
2. **Obliczenia**: wynik kluczowy (ΣDU, K, Qww, Q przyjęte, wzór i podstawienie) i wskazanie utworzonego pliku Excel z pełnym zestawieniem pomieszczeń i przyborów z DU (patrz sekcja „Zestawienie w Excelu”). Pełną tabelę przyborów trzymaj w pliku, nie w treści odpowiedzi.
3. **Dobór DN podejść / odcinków** z tabelą: odcinek, Q, DN, L, łuki, H, spadek, wynik kontroli ograniczeń (OK / przekroczone + co zrobić). Jeśli geometrii podejść nie podano, napisz to i pomiń ten punkt zamiast zgadywać.
4. **Uwagi i otwarte pytania do projektanta** (np. system kanalizacji, wartość K, brakujące tabele pionów).
5. **Źródła**: PN-EN 12056-2:2002 (w brzmieniu do sprawdzenia), strony instsani.pl; dla przepisów (Prawo budowlane, WT) – aktualny stan prawny sprawdzony w Repertorium lub innym źródle.

## Typowe pułapki

- Rozpoczęcie pracy bez zapytania o system kanalizacji (I–IV) – patrz krok 0.
- Odczyt Qww z tabeli zamiast ze wzoru (błąd w tabeli dla ΣDU = 200).
- Pominięcie warunku Q ≥ DU_max (np. 2 WC + 2 umywalki: Qww = 1,12 dm³/s przy K = 0,5, ale DU_max = 2,0 – przyjmij 2,0).
- Wybór DN z tabeli niższego niż wylot przyboru.
- Stosowanie tabel systemów I/II/IV dla systemu III (ma osobne tab. 6 i 9).
- Podawanie wartości dla pionów bez źródła.
- Mieszanie jednostek: DU i Q w dm³/s (l/s), spadek w %, L i H w m.
- Wpisanie w Excelu wartości DU z innego systemu niż wybrany albo wyników policzonych w Pythonie zamiast formuł.
- Sumowanie przepływów pomieszczeń zamiast ΣDU.