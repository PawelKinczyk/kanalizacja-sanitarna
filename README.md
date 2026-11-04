# Kanalizacja sanitarna w CAD – przykładowy skill dla Claude

Repozytorium do filmu **„Model AI widzi Twój rysunek w CAD dopiero wtedy, gdy podłączysz go przez serwer MCP”**. W filmie pokazuję drogę od architektury przez osie i kropki wody do instalacji sanitarnej w GstarCAD, a na końcu skill creator tworzy z zebranych uwag skill do rysowania kanalizacji sanitarnej. Ten skill znajdziesz tutaj.

To skill przykładowy. Pokazuje, jak zamienić korekty wydawane modelowi w trakcie pracy w powtarzalne zasady. Dopasuj go do swoich standardów, warstw i bloków, zanim użyjesz go w projekcie.

## Co jest w repozytorium

```
kanalizacja-sanitarna/
├── SKILL.md               # zasady rysowania kanalizacji sanitarnej na rzutach CAD
└── references/
    └── cad-com.md         # obsługa GstarCAD / AutoCAD przez COM, pułapki, oglądanie wyniku
```

**`SKILL.md`** opisuje przebieg pracy i ustalenia z filmu:

- piony jako bloki z atrybutem `NUMER`, w narożniku lub przy ścianie za urządzeniem, przez wszystkie kondygnacje,
- wyprowadzenie pionów ponad dach z wywiewką (blok `WYWIEWKA`),
- podejścia prowadzone równolegle do ściany, zmywarka podłączona do podejścia zlewu,
- łączenia i zmiany kierunku pod kątem 45 stopni, odgałęzienia zgodne z kierunkiem przepływu,
- omijanie elementów konstrukcyjnych (słupów) z kontrolą kolizji skryptem przed rysowaniem,
- sprawdzanie wyniku na zrzucie widoku, a nie tylko na komunikacie „polecenie wykonane”,
- lista spraw do uzgodnienia z projektantem: średnice, spadki, czyszczaki, zawory napowietrzające, legenda.

**`references/cad-com.md`** to wiedza techniczna: połączenie z CAD przez COM, rysowanie polilinii, kropek i bloków z atrybutami, pułapki PowerShell i dekodowanie zrzutu widoku z serwera MCP.

## Instalacja skilla

**Claude Code** – skopiuj folder `kanalizacja-sanitarna` do katalogu skilli:

- dla wszystkich projektów: `~/.claude/skills/kanalizacja-sanitarna/`
- dla jednego projektu: `.claude/skills/kanalizacja-sanitarna/` w folderze projektu

```bash
git clone https://github.com/PawelKinczyk/kanalizacja-sanitarna.git
```

```bash
cp -r kanalizacja-sanitarna/kanalizacja-sanitarna ~/.claude/skills/
```

**Claude (aplikacja / claude.ai)** – spakuj folder `kanalizacja-sanitarna` do pliku ZIP i dodaj go w ustawieniach jako własny skill.

Skill uruchamia się sam, gdy poprosisz o rozrysowanie lub poprawienie kanalizacji, pionów, podejść albo wywiewek. Nie musisz podawać jego nazwy.

## Wymagania

- program CAD z dostępem przez COM: GstarCAD (w filmie) lub AutoCAD,
- serwer MCP podłączony do CAD, w filmie [multiCAD MCP](https://github.com/AnCode666/multiCAD-mcp),
- plik `CLAUDE.md` (albo `AGENTS.md` przy ChatGPT) w folderze projektu z założeniami tego konkretnego projektu: położenie rzutów, warstwy, nazwy bloków, lista słupów.

## O filmie

Serwer MCP działa jak stół warsztatowy: na nim leżą narzędzia, każde opisane, a model wybiera te, które są potrzebne do zadania. Gdy gotowego narzędzia brakuje, wysyła z siebie własny skrypt do CAD, trochę jak własny LISP, więc możesz zrobić więcej niż w predefiniowanych funkcjach, oczywiście w granicach tego, co daje sam program. Najważniejsze w codziennej pracy jest jednak coś innego: plik `CLAUDE.md` (albo `AGENTS.md` przy ChatGPT) jako pamięć projektu, który model aktualizuje w trakcie pracy. Bez niego to samo polecenie daje inny wynik przy każdym uruchomieniu i model idzie po linii najmniejszego oporu, jeśli go nie naprowadzasz.

W filmie pokazuję:

- co to serwer MCP i metafora stołu warsztatowego: narzędzia opisane, model wybiera potrzebne
- własne skrypty wysyłane z modelu do CAD, działają jak LISP, więc można zrobić więcej niż w gotowych narzędziach
- `CLAUDE.md` i `AGENTS.md` jako pamięć projektu, aktualizowane w trakcie pracy
- dyktowanie poleceń w Handy zamiast pisania
- podpięcie architektury jako Xref na osobnej warstwie i rysowanie osi
- lokalizacja urządzeń sanitarnych i oznaczanie punktów wody i kanalizacji kropkami
- blok łazienki z kreskowaniem, piony jako bloki z atrybutem numeru, piony do dachu z wywiewką
- trasowanie kanalizacji i wody oraz korekty: łączenia 45 stopni, omijanie elementów konstrukcyjnych, podejścia przy ścianie
- dwutorowe zapisywanie uwag: `CLAUDE.md` dla projektu i skill dla powtarzalnych zasad, na końcu skill creator tworzy skill do kanalizacji

### Do zapamiętania

1. **Model idzie po linii najmniejszego oporu.** To bardzo inteligentny asystent, ale wynik zawsze trzeba naprowadzić, a nie przyjąć domyślny.
2. **Uwagi pisz dwutorowo.** `CLAUDE.md` trzyma założenia tylko tego projektu, skill zbiera powtarzalne zasady dla kolejnych.
3. **Jedna seria poleceń głosowych.** Cały film to polecenia dyktowane głosem, od podpięcia architektury do gotowego skilla do kanalizacji sanitarnej.

### Rozdziały

| Czas  | Temat |
|-------|-------|
| 00:00 | Co daje serwer MCP w CAD |
| 01:06 | Własne skrypty zamiast LISP |
| 03:00 | CLAUDE.md jako pamięć projektu |
| 05:33 | Dyktowanie polecenia i podpięcie Xref |
| 07:04 | Rysowanie osi na podkładzie |
| 10:14 | Punkty wody i kanalizacji kropkami |
| 13:38 | Blok łazienki z kreskowaniem |
| 15:31 | Piony jako bloki z atrybutem numeru |
| 20:35 | Ciepła i zimna woda na osobnych warstwach |
| 22:33 | Piony wyciągnięte do dachu z wywiewką |
| 24:10 | Trasowanie kanalizacji i wody |
| 27:11 | Elementy konstrukcyjne i łączenia 45 stopni |
| 31:37 | Uwagi dwutorowo: CLAUDE.md i skill |
| 34:21 | Skill creator tworzy skill do kanalizacji |

## Serwery MCP użyte i polecane

- **multiCAD MCP** – serwer użyty w filmie: https://github.com/AnCode666/multiCAD-mcp
- **AutoCAD MCP Pro**: https://github.com/U-C4N/Autocad-MCP
- **CAD-MCP**: https://github.com/daobataotie/CAD-MCP
- **best-cad-mcp**: https://github.com/LokmenoWer/best-cad-mcp

Na każdym z tych repozytoriów jest instrukcja instalacji. Konfigurację łatwiej zrobić z modelem, który przejdzie przez pliki konfiguracyjne krok po kroku.

## Powiązane filmy

- Dyktowanie poleceń w Handy zamiast pisania: https://www.youtube.com/watch?v=y_ZnVwFdKeY
- Skille w Claude, bez tego filmu skill creator nie będzie jasny: https://youtu.be/fWUHA1TJOS4

## Autor

Paweł Kińczyk

- Blog: https://produktywnyprojektant.com
- LinkedIn: https://www.linkedin.com/in/paweł-kińczyk
- Facebook: https://www.facebook.com/profile.php?id=100077381224044
- GitHub: https://github.com/PawelKinczyk

## Licencja

MIT, zob. [LICENSE](LICENSE). Skill jest przykładem do nauki i adaptacji. Odpowiedzialność za projekt i jego zgodność z przepisami pozostaje po stronie projektanta.

`#MCP #CAD #GstarCAD #Claude #ProjektowanieInstalacji #Produktywność`
