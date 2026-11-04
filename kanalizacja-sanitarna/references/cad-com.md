# Obsługa CAD przez COM (GstarCAD / AutoCAD)

Sprawdzone w pracy z GstarCAD. Używaj, gdy rysujesz lub oglądasz wynik.

## Połączenie

- `[Runtime.InteropServices.Marshal]::GetActiveObject("Gcad.Application")`, potem `$app.ActiveDocument` i `$d.ModelSpace`. Dla AutoCAD zamiast tego `AutoCAD.Application`.
- Narzędzie MCP `multiCAD` (`manage_session connect`, `manage_layers`, `manage_blocks`) działa na tym samym rysunku, ale nie ma akcji XREF ani rysowania polilinii z szerokością. Te rzeczy rób przez COM.
- Nazwa aktywnego rysunku się zmienia (`Rysunek1.dwg`, potem `Projekt.dwg`). Nie zakładaj nazwy, odczytaj ją.

## Rysowanie

- Polilinia: `$ms.AddLightWeightPolyline([double[]](x1,y1,x2,y2,...))`, potem `.Layer`, `.Linetype`, `.LinetypeScale = 0.05`, `.ConstantWidth = 0.03`. Linetype trzeba najpierw załadować: `$d.Linetypes.Load("HIDDEN","gcadiso.lin")`.
- Zmiana wierzchołków istniejącej polilinii: `$e.Coordinates = [double[]](...)`.
- Kropka: polilinia z dwoma wierzchołkami i `SetBulge(0,1)`, `SetBulge(1,1)`, `Closed = $true`, `ConstantWidth` równe średnicy.
- Blok: `$d.Blocks.Add([double[]](0,0,0),"NAZWA")`, dodaj geometrię na warstwie `0` i atrybut `AddAttribute(wysokość,0,"prompt",punkt,"NUMER","domyślna")`. Wstawienie: `$ms.InsertBlock(pt,"NAZWA",1,1,1,0)`, potem `.Layer` i `GetAttributes()`, przez `TextString` i `InsertionPoint` ustaw wartość i położenie etykiety.
- Kolejność rysowania: `SendCommand` z `ssget` wiesza CAD. Anuluj Esc (`SendCommand([string][char]27 + [char]27)`). Jeśli to możliwe, unikaj.

## Pułapki PowerShell

- Nie nazywaj funkcji `R` (alias `Invoke-History`) ani zmiennych `$home`, `$args`, `$host` (zmienne zarezerwowane).
- Wyrażenia typu `$R/2` w jednej linii potrafią zablokować wywołanie, więc używaj `* 0.5`.
- Argument `-f` z `($X|measure -Min).Minimum` w liście argumentów psuje formatowanie: policz wartości wcześniej do zmiennych.
- Polskie znaki w stringach COM wstawiaj jako `[char]0x0142` i podobne, jeśli kodowanie skryptu zawodzi.

## Oglądanie wyniku

1. `$app.ZoomWindow([double[]](x1,y1,0),[double[]](x2,y2,0))` na interesujący obszar.
2. `manage_session` z `export_view`. Wynik jest ogromny (base64 PNG) i narzędzie zapisze go do pliku z komunikatem "exceeds maximum allowed tokens". Zdekoduj w Pythonie: wczytaj JSON z pliku, weź `result`, sparsuj, w `results[].data` jest PNG w base64. Uruchamiaj Pythona z `-I`.
3. Otwórz PNG narzędziem Read i oceń. Skala: z oddalenia widać układ, z bliska węzły i kolizje. Linie ukryte mogą na zrzucie wyglądać jak linie kreskowane o innej skali, ocena kątów i kolizji jest wiarygodna, wyglądu kreskowania nie.

## Kontrola kolizji ze słupami (wzór)

Dla każdego odcinka trasy i każdego słupa (środek cx, cy, bok 0,2) sprawdź w skrypcie, czy któryś z 200 punktów próbkowania leży w prostokącie powiększonym o zapas (0,1 + 0,03). Jeśli są kolizje, nie rysuj, popraw trasę (przesuń cały odcinek) i sprawdź ponownie.
