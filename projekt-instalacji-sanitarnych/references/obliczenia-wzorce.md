# Wzorce bloków obliczeniowych

Obliczenia w przykładach mają zawsze ten sam układ. Używaj go, a **wartości z przykładów traktuj wyłącznie jako ilustrację formatu** – w nowym projekcie liczby muszą wynikać z danych i z obliczeń. Jeśli czegoś nie da się policzyć (brak danych), zapisz „założenie do potwierdzenia” zamiast liczby.

## Układ bloku

```
DÓBÓR <ELEMENTU>                      <- pogrubiony, kursywa, podkreślony
  Założenia:
    symbol – opis                                   wartość + jednostka
    ...
  Obliczenia:
    opis wielkości obliczanej                       symbol = **wynik jednostka**
    ...
  **Dobrano <typ, producent, parametry>.**          <- pogrubione
  (opcjonalnie) Sprawdzenie: warunek spełniony / dobór jest poprawny
```

Zasady: symbol z indeksami (Q<sub>śr d</sub>), opis po myślniku, wartość wyrównana do prawej kolumny (ok. 60% szerokości), jednostki zawsze podane, przecinek dziesiętny, spójna liczba miejsc po przecinku w obrębie bloku. Wynik i zdanie „Dobrano…” pogrubione. Podaj normę lub metodę, z której wynika obliczenie – po sprawdzeniu aktualnego wydania.

## Katalog obliczeń (z przykładów)

| Obliczenie | Założenia | Wyniki | Dobór / wniosek |
|---|---|---|---|
| **Zapotrzebowanie na wodę** | współczynniki nierównomierności dobowej Nd i godzinowej Nh, liczba osób, jednostkowe zużycie wody, godziny użytkowania | Qśr d, Qmax d, Qmax h (dm³/d, m³/d, m³/h) | – |
| **Przepływ obliczeniowy wody** (tabela) | wykaz punktów czerpalnych: Lp., nazwa, ilość [szt.], normatywny wypływ [l/s], suma [l/s] | suma wypływów, przepływ obliczeniowy wody zimnej i ciepłej [l/s], wymagane ciśnienie dyspozycyjne [kPa] | warunek dla gestora/pompy |
| **Dobór zasobnika c.w.u.** | liczba odbiorców, jednostkowe dobowe zużycie c.w.u., godziny użytkowania, Nh, gęstość, ciepło właściwe wody, temperatury c.w.u. i wody zimnej, współczynnik akumulacji | średnie dobowe i godzinowe zużycie, maks. godzinowe, objętość zasobnika, moc minimalna i średnia | zasobnik o pojemności …, rzeczywisty współczynnik akumulacji |
| **Naczynie wzbiorcze c.w.u.** | pojemność wodna zasobnika, ciśnienie robocze, ciśnienie otwarcia zaworu bezp., Tmax, ciśnienie wstępne, współczynnik rozszerzalności | minimalna pojemność naczynia | naczynie … o pojemności … |
| **Zawór bezpieczeństwa c.w.u.** | pojemność wodna podgrzewacza, przepustowość zaworu | średnica obliczeniowa zaworu | warunek d_obl < d_dobrana → „dobór jest poprawny” |
| **Przepływ ścieków (DU)** (tabela) | przybory: Lp., nazwa, ilość, odpływ jednostkowy DU, suma | suma DU, współczynnik częstości, Qww [l/s], średnica kolektora, wypełnienie [%], prędkość [m/s] | średnica zbiorczego kanału odpływowego |
| **Naczynie przeponowe c.o.** | Tmax, Tmin, pojemność zładu, wysokość statyczna, PSV, ubytki eksploatacyjne | objętość rozszerzalności Ve, rezerwa Vwr, ciśnienie wstępne i końcowe, współczynnik ciśnieniowy, wymagana objętość | naczynie … o pojemności … |
| **Zawór bezpieczeństwa c.o.** | maks. moc cieplna źródła, ciśnienie nastawy, ciepło parowania, współczynniki poprawkowe, współczynnik wypływu, maks. ciśnienie przed zaworem | wymagana przepustowość, powierzchnia i średnica kanału dolotowego | zawór … o nastawie …, porównanie z powierzchnią kanału |
| **Naczynie wzbiorcze otwarte** | pojemność całkowita instalacji i źródła, gęstość wody, przyrost objętości właściwej, moc źródła | minimalna pojemność naczynia, średnice rur: bezpieczeństwa, wzbiorczej, sygnalizacyjnej, przelewowej | naczynie typu … i rury o średnicach … |
| **Bilans powietrza wentylacji** (tabela) | pomieszczenia: nr, nazwa, powierzchnia, kubatura, krotność, nawiew, wywiew | sumy nawiewu i wywiewu, sumaryczna krotność | centrala o wydajności … (dobór wg bilansu) |
| **Wody opadowe – zbiornik** | natężenia deszczu (miarodajne i nawalne), powierzchnie spływu (dach, utwardzenia), współczynnik spływu, czas deszczu | Q (deszcz miarodajny), Qn (nawalny), wymagana pojemność zbiornika | zbiornik o pojemności całkowitej … |

## Kontrola spójności obliczeń

- Wyniki w obliczeniach, w opisie (np. „moc całkowita instalacji c.o. wynosi …”) i na rysunkach (moce pomieszczeń, pętli, legenda) są **identyczne**.
- Dobrany element ma parametr nie gorszy niż obliczony (pojemność naczynia ≥ wymagana, średnica zaworu ≥ obliczona).
- Suma wypływów, suma DU i suma bilansu powietrza zgadzają się z sumami częściowymi w tabeli (sprawdź rachunkiem).
- Nawiew i wywiew bilansują się (lub różnica jest zamierzona i opisana).
- Pole powierzchni i kubatura w bilansie powietrza są zgodne z danymi architektury.

Przy uwzględnieniu zmian przepisów (np. nowych norm projektowania instalacji wodociągowych i kanalizacyjnych) zaktualizuj metodę obliczeń i powołanie, nie kopiuj starych norm z przykładów.
