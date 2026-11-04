---
name: kanalizacja-sanitarna
description: Rysowanie instalacji kanalizacji sanitarnej na rzutach CAD (AutoCAD/GstarCAD, XREF z architekturą) - piony, podejścia do urządzeń, kolektory, przyłącze, wywiewki. Używaj zawsze, gdy użytkownik prosi o rozrysowanie, wytrasowanie, poprawienie lub sprawdzenie kanalizacji, pionów kanalizacyjnych, podejść do WC, umywalki, wanny, zlewu, zmywarki, prysznica, o połączeniach 45 stopni, przyłączu kanalizacji albo o wywiewce na dachu, także gdy nie pada słowo "skill" ani "kanalizacja sanitarna". Draw sanitary sewer risers, branches and collectors on CAD floor plans.
---

# Kanalizacja sanitarna na rzutach CAD

Skill opisuje, jak rysować kanalizację sanitarną na rzutach kondygnacji, tak jak ustalił użytkownik w projekcie z podkładem architektonicznym w XREF. Reguły wynikają z korekt użytkownika, więc traktuj je jako ustalone, a nie jako propozycje. Szczegóły techniczne obsługi CAD przez COM są w `references/cad-com.md`.

## Przebieg pracy

1. **Poznaj rysunek.** Odczytaj z `CLAUDE.md` projektu: położenie rzutów, przesunięcia między kondygnacjami, warstwy, nazwy bloków urządzeń, listę słupów. Jeśli czegoś brakuje, odczytaj z XREF (bloki urządzeń, słupy), nie zgaduj. Przy każdej pracy sprawdź, co użytkownik zmienił od ostatniego razu (przesunięte piony, nowe linie), i traktuj to jako wzorzec.
2. **Znajdź urządzenia i punkty odpływu** na każdym rzucie (WC, umywalka, wanna, prysznic, zlew, zmywarka). Rozpoznawaj po nazwie bloku, a gdy nazwa jest nieczytelna, po wyglądzie symbolu na zrzucie widoku. Zapisz punkt odpływu (kropka brązowa) i ścianę, przy której urządzenie stoi.
3. **Ustaw piony.** Zob. "Piony".
4. **Zaplanuj kolektor i przyłącze.** Przyłącze wychodzi z pomieszczenia wskazanego przez użytkownika. Jeśli go nie wskazał, zapytaj. Kolektor na parterze leży pod posadzką.
5. **Poprowadź podejścia** od urządzeń do pionów lub kolektora. Zob. "Podejścia".
6. **Sprawdź kolizje ze słupami** skryptem, zanim cokolwiek narysujesz.
7. **Narysuj, potem obejrzyj wynik na zrzucie** (zoom na obszar, `export_view`, dekoduj PNG). Samo "polecenie wykonane" nie dowodzi, że rysunek wygląda dobrze.
8. **Podsumuj użytkownikowi**: co narysowane, jakie przyjęto założenia, co wymaga potwierdzenia. Zapisz nowe ustalenia w `CLAUDE.md` projektu.

## Piony

- Pion rysuj jako blok z atrybutem `NUMER` (np. `Pk1`), a nie jako luźne koło i tekst. Numer pozwala identyfikować i zestawiać piony. Ten sam numer oznacza ten sam pion.
- Stawiaj pion w narożniku dwóch stykających się ścian albo przy ścianie za urządzeniem, nigdy na środku blatu lub ściany. Użytkownik przeniósł Pk3 ze środka blatu w narożnik i nazwał to wyraźnie lepszym miejscem.
- **Pion przechodzi przez całą kondygnację i wszystkie kondygnacje**, chyba że instrukcja użytkownika mówi inaczej. Dlatego pion z parteru rysuj też na piętrze, a pion z piętra rysuj też na parterze, w tym samym miejscu w planie (przesunięcie rzutu w osi x, y bez zmian). Na każdej kondygnacji ten sam `NUMER`. Powód: pion to jeden element pionowy, a plan pokazuje go na każdej kondygnacji, którą przecina. Pominięcie go na kondygnacji bez urządzeń jest błędem, bo tam też zajmuje miejsce i bywa w kolizji.
- **Pion kończy się na dachu wywiewką** (blok `WYWIEWKA`, podwójne koło z krzyżykiem, atrybut `NUMER`, warstwa pionów kanalizacyjnych). Wentylacja pionu wyprowadzona ponad dach jest warunkiem poprawnego działania instalacji.
- Gdy użytkownik wprost wyłącza pion z reguły (np. wodociąg nie idzie na dach), zastosuj jego wyjątek.

## Podejścia do urządzeń

- Pierwszy odcinek podejścia biegnie **równolegle do ściany**, przy której stoi urządzenie, a nie w poprzek pomieszczenia ani blatu. Powód: przewody przy ścianie nie blokują posadzki i są tam, gdzie je prowadzi się w praktyce.
- Podejście zlewu biegnie wzdłuż ściany za zlewem do pionu. Zmywarka łączy się z podejściem zlewu (przy syfonie), a nie osobno z pionem. Użytkownik wymaga takiego połączenia. Jeśli geometria na to nie pozwala (kolizja ze słupem, narożnik), powiedz wprost, zamiast po cichu łączyć gdzie indziej.
- Podejście do WC: najpierw w stronę ściany, przy której stoi WC, potem zawraca do pionu.

## Połączenia pod kątem 45 stopni

- Wszystkie łączenia i zmiany kierunku robisz kątem 45 stopni: kolano 90 stopni zastępuj dwoma kolanami 45 (odcinek ukośny między dwoma prostymi), a boczne dopływy podłączaj trójnikami skośnymi (odgałęzienie 45 stopni).
- **Odgałęzienie musi wpływać zgodnie z kierunkiem przepływu**: wektor odgałęzienia ma mieć składową zgodną z przepływem w przewodzie głównym. Odgałęzienie "pod prąd" jest błędem hydraulicznym, nawet jeśli wygląda poprawnie. Wyjątki ustala użytkownik: na piętrze, gdy podejście do pionu biegnie przy ścianie, umywalki i wanna mogą wchodzić prostopadle zgodnie z poleceniem użytkownika. Wanna została potem poprawiona na 45 stopni.
- Typowa konstrukcja: odcinek prosty, ukos 45 stopni o równych rzutach dx i dy, odcinek prosty. Długość ukosu dobierz tak, by wejście w przewód główny nastąpiło w żądanym punkcie.
- Dwa dopływy z przeciwnych stron wprowadzaj w różnych punktach przewodu głównego, by nie zbiegały się w jednym punkcie.

## Kolizje i prowadzenie w budynku

- Elementy konstrukcyjne (słupy) są nieprzekraczalne. Gdy trasa koliduje, **przesuń cały odcinek**, a nie tylko kawałek. Słup ma 0,2 x 0,2 m, zapas minimum 0,03 m. Skrypt sprawdzający próbkuje odcinki co 0,5 procent długości względem listy słupów.
- Na parterze kanalizacja leży w posadzce. Na kondygnacjach wyższych w podłodze lub pod stropem, zależnie od polecenia.
- Rysuj trasy jako polilinie na osobnej warstwie (linia ukryta, grubość 0,03 dla kanalizacji), a piony jako bloki na warstwie pionów. Nie mieszaj warstw.

## Czego nie robić

- Nie zakładaj z góry miejsca przyłącza ani kotła, zapytaj lub użyj wskazania użytkownika.
- Nie nadpisuj obiektów użytkownika (jego kropek, bloków). Dopisuj własne, a zmiany jego obiektów zgłaszaj.
- Nie usuwaj obiektów poza własnymi. Przy usuwaniu po uchwycie sprawdź, czy uchwyt to na pewno Twój obiekt, bo uchwyty zmieniają się po zapisie i zmianie nazwy rysunku.

## Co jeszcze warto uzgodnić z użytkownikiem

To nie są ustalenia, tylko lista pytań do zadania, gdy mają znaczenie:

- średnice (zwykle DN110 dla WC i kolektora, DN50 dla umywalki, zlewu, wanny i prysznica) i opisy na rysunku,
- spadki przewodów leżących (zwykle ok. 2 procent dla DN110, ok. 3 procent dla DN50) i ich oznaczenie,
- czyszczaki (rewizje) przy podstawie pionu, przy zmianach kierunku i przed wyjściem z budynku,
- zawory napowietrzające zamiast wywiewki, gdy dach tego wymaga,
- brodzik lub wpust podłogowy w pomieszczeniu z prysznicem, jeśli go nie narysowano,
- legenda, skala, tabela pionów (numer, kondygnacje, miejsce).
