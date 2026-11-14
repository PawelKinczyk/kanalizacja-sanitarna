#!/usr/bin/env python3
"""Wymiarowanie kanalizacji sanitarnej wewnetrznej wg PN-EN 12056-2:2002.

Podkomendy:
  du         przeplyw Qww = K * sqrt(sum DU) z listy przyborow
  podejscie  dobor DN podejscia (tab. 4/5 niewentylowane, 7/8 wentylowane; sys. I, II, IV)
  odplyw     hydraulika przewodu zbiorczego/podposadzkowego (Colebrook-White, napelnienie h/d)

Dane liczbowe tabel pochodza ze strony instsani.pl (PN-EN 12056-2:2002), odczytane
z obrazow. Wartosci Qww liczone ze wzoru (nie z tabeli strony, ktora ma blad dla DU=200, K=0,5).
Srednice wewnetrzne i chropowatosc w 'odplyw' to ZALOZENIA - podmien danymi producenta (--di, --k).
"""
import argparse
import json
import math
import sys

# ---- Tab. 3: DU [l/s] wg systemu (I, II, III, IV). None = nie stosowane / brak danych.
# Dla systemu III przy ustepach podano zakres - przyjeto gorna wartosc (bezpiecznie).
DU = {
    "umywalka":            (0.5, 0.3, 0.3, 0.3),   # umywalka, bidet
    "natrysk_bez_korka":   (0.6, 0.4, 0.4, 0.4),
    "natrysk_z_korkiem":   (0.8, 0.5, 1.3, 0.5),
    "pisuar_zbiornik":     (0.8, 0.5, 0.4, 0.5),   # pojedynczy pisuar ze zbiornikiem
    "pisuar_zawor":        (0.5, 0.3, None, 0.3),  # pisuar z zaworem spluczkowym
    "pisuar_plytowy_os":   (0.2, 0.2, 0.2, 0.2),   # na osobe
    "wanna":               (0.8, 0.6, 1.3, 0.5),
    "zlew":                (0.8, 0.6, 1.3, 0.5),
    "zmywarka":            (0.8, 0.6, 0.2, 0.5),
    "pralka_5kg":          (0.8, 0.6, 0.6, 0.5),
    "pralka_12kg":         (1.5, 1.2, 1.2, 1.0),
    "wc_4l":               (None, 1.8, None, None),  # nie zaleca sie w I, III, IV
    "wc_6l":               (2.0, 1.8, 1.7, 2.0),     # sys. III: 1,2-1,7 (przyjeto 1,7)
    "wc_7_5l":             (2.0, 1.8, 1.8, 2.0),     # sys. III: 1,4-1,8
    "wc_9l":               (2.5, 2.0, 2.0, 2.5),     # sys. III: 1,6-2,0
    "wpust_dn50":          (0.8, 0.9, None, 0.6),
    "wpust_dn70":          (1.5, 0.9, None, 1.0),
    "wpust_dn100":         (2.0, 1.2, None, 1.3),
}

# ---- Tab. 4 (Qmax -> DN, niewentylowane), wiersze: (Qmax, {sys: (DN|None, uwaga)})
T4 = [
    (0.40, {1: (None, "nie zaleca sie"), 2: (30, ""), 4: (30, "")}),
    (0.50, {1: (40, ""), 2: (40, ""), 4: (40, "")}),
    (0.80, {1: (50, ""), 2: (None, "nie zaleca sie"), 4: (None, "nie zaleca sie")}),
    (1.00, {1: (60, ""), 2: (50, ""), 4: (50, "")}),
    (1.50, {1: (70, ""), 2: (60, ""), 4: (60, "")}),
    (2.00, {1: (80, "bez ustepow splukiwanych"), 2: (70, "bez ustepow splukiwanych"),
            4: (70, "bez ustepow splukiwanych")}),
    (2.25, {1: (90, "max 2 ustepy splukiwane, zmiana kierunku <= 90 st."),
            2: (80, "max 1 ustep splukiwany"), 4: (80, "max 1 ustep splukiwany")}),
    (2.50, {1: (100, ""), 2: (90, ""), 4: (100, "")}),
]
# ---- Tab. 5: ograniczenia niewentylowane: L max [m], luki 90 max, H max [m], spadek min [%]
T5 = {1: (4.0, 3, 1.0, 1.00), 2: (10.0, 1, None, 1.50), 4: (10.0, 3, 1.0, 1.00)}
# sys. II: H max 6,0 m dla DN>70, 3,0 m dla DN=70

# ---- Tab. 7 (Qmax -> DN podejscia / DN przewodu went.), wentylowane
T7 = [
    (0.60, {1: (None, None, "nie zaleca sie"), 2: (30, 30, ""), 4: (30, 30, "")}),
    (0.75, {1: (50, 40, ""), 2: (40, 30, ""), 4: (40, 30, "")}),
    (1.50, {1: (60, 40, ""), 2: (50, 30, ""), 4: (50, 30, "")}),
    (2.25, {1: (70, 50, ""), 2: (60, 30, ""), 4: (60, 30, "")}),
    (3.00, {1: (80, 50, "bez ustepu splukiwanego"), 2: (70, 40, "bez ustepu splukiwanego"),
            4: (70, 40, "bez ustepu splukiwanego")}),
    (3.40, {1: (90, 60, "max 2 ustepy splukiwane, zmiana kierunku <= 90 st."),
            2: (80, 40, "max 1 ustep splukiwany"), 4: (80, 40, "max 1 ustep splukiwany")}),
    (3.75, {1: (100, 60, ""), 2: (90, 50, ""), 4: (90, 50, "")}),
]
# ---- Tab. 8: wentylowane: L max, luki, H max, spadek min [%]  (None = bez ograniczen)
T8 = {1: (10.0, None, 3.0, 0.50), 2: (None, None, 3.0, 1.50), 4: (10.0, None, 3.0, 0.50)}

K_USE = {"nieciagle": 0.5, "okresowe": 0.7, "zbiorowe": 1.0, "specjalne": 1.2}

# ---- ZALOZENIE: typowe srednice wewnetrzne rur kanalizacyjnych PVC-U [mm] - zastap danymi producenta
DI_DEFAULT = {40: 36.4, 50: 46.4, 75: 70.4, 90: 85.6, 110: 103.6, 125: 118.6, 160: 152.0, 200: 190.2, 250: 237.6, 315: 299.6}


def sysidx(s):
    return int(s) - 1


def cmd_du(a):
    items = json.loads(a.items)
    k = K_USE.get(a.uzytkowanie)
    if k is None:
        k = float(a.uzytkowanie)
    total, biggest, rows, warns = 0.0, 0.0, [], []
    for name, n in items.items():
        if name not in DU:
            sys.exit(f"Nieznany przybor '{name}'. Dostepne: {', '.join(DU)}")
        v = DU[name][sysidx(a.system)]
        if v is None:
            sys.exit(f"'{name}': brak DU w systemie {a.system} (nie stosowane / nie zaleca sie).")
        rows.append((name, n, v, n * v))
        total += n * v
        biggest = max(biggest, v)
    qww = k * math.sqrt(total)
    q = max(qww, biggest)
    if q > qww:
        warns.append("Przyjeto najwiekszy odplyw jednostkowy (Qww mniejsze od DU najwiekszego przyboru).")
    qtot = q + a.qc + a.qp
    for r in rows:
        print(f"{r[0]:22s} {r[1]:4g} x {r[2]:.1f} = {r[3]:.2f} l/s")
    print(f"sum DU = {total:.2f} l/s ; K = {k} ; Qww = K*sqrt(sumDU) = {qww:.2f} l/s")
    print(f"Q przyjete = max(Qww, DU max) = {q:.2f} l/s ; Qc = {a.qc} ; Qp = {a.qp} ; Qtot = {qtot:.2f} l/s")
    for w in warns:
        print("UWAGA:", w)


def lookup(table, sysno, q, vented):
    for row in table:
        qmax, d = row
        if q <= qmax + 1e-9:
            e = d.get(sysno)
            if e is None:
                sys.exit(f"Brak danych dla systemu {sysno}.")
            dn = e[0]
            if dn is None:
                continue  # 'nie zaleca sie' - przejdz do kolejnego wiersza
            return qmax, e
    return None, None


def cmd_podejscie(a):
    if a.system == 3:
        sys.exit("System III: uzyj tabel 6 (niewentylowane) i 9 (wentylowane) z pliku referencji skilla - wymagaja doboru wg rodzaju przyboru.")
    q = a.q
    table = T7 if a.wentylowane else T4
    lim = (T8 if a.wentylowane else T5)[a.system]
    qmax, e = lookup(table, a.system, q, a.wentylowane)
    if e is None:
        print(f"Q = {q} l/s przekracza zakres tabeli ({'7' if a.wentylowane else '4'}). Zwieksz srednice, przejdz na podejscie wentylowane / inna konfiguracje albo licz inaczej.")
        return
    if a.wentylowane:
        print(f"Tab. 7: Qmax = {qmax} l/s -> podejscie DN{e[0]} / przewod wentylacyjny DN{e[1]}  {('['+e[2]+']') if e[2] else ''}")
    else:
        print(f"Tab. 4: Qmax = {qmax} l/s -> podejscie DN{e[0]}  {('['+e[1]+']') if e[1] else ''}")
    dn = e[0]
    lmax, luki, hmax, smin = lim
    if a.system == 2 and not a.wentylowane:
        hmax = 6.0 if dn > 70 else 3.0
    bad = []
    if a.l is not None and lmax is not None and a.l > lmax:
        bad.append(f"L = {a.l} m > {lmax} m")
    if a.luki is not None and luki is not None and a.luki > luki:
        bad.append(f"luki 90 st. = {a.luki} > {luki}")
    if a.h is not None and hmax is not None and a.h > hmax:
        bad.append(f"H = {a.h} m > {hmax} m")
    if a.spadek is not None and a.spadek < smin:
        bad.append(f"spadek {a.spadek}% < min {smin}%")
    print(f"Ograniczenia (tab. {'8' if a.wentylowane else '5'}): L max {lmax or 'bez ogr.'} m; luki max {luki if luki is not None else 'bez ogr.'}; H max {hmax} m; spadek min {smin}%")
    if bad:
        print("PRZEKROCZONE:", "; ".join(bad), "-> zastosuj podejscie wentylowane, wieksza srednice lub zawor napowietrzajacy.")
    else:
        print("Podane parametry geometrii miesci sie w ograniczeniach (sprawdz tez uwagi do tabel).")


def hyd(di_mm, slope, fill, k_mm, nu=1.31e-6):
    d = di_mm / 1000.0
    th = 2 * math.acos(1 - 2 * fill)           # kat srodkowy zwilzony
    A = d * d / 8 * (th - math.sin(th))
    P = d * th / 2
    R = A / P
    Dh = 4 * R
    k = k_mm / 1000.0
    v = 1.0
    for _ in range(100):
        re = max(v * Dh / nu, 1.0)
        lam = 0.02
        for _ in range(50):
            lam = (-2 * math.log10(k / (3.71 * Dh) + 2.51 / (re * math.sqrt(lam)))) ** -2
        vn = math.sqrt(8 * 9.81 * R * slope / lam)
        if abs(vn - v) < 1e-6:
            break
        v = vn
    return v, v * A * 1000.0  # m/s, l/s


def cmd_odplyw(a):
    s = a.spadek / 100.0
    print(f"Q = {a.q} l/s ; spadek = {a.spadek}% ; h/d = {a.wypelnienie} ; k = {a.k} mm")
    res = None
    for dn in sorted(DI_DEFAULT):
        if dn < a.dn_min:
            continue
        di = a.di if a.di else DI_DEFAULT[dn]
        v, qc = hyd(di, s, a.wypelnienie, a.k)
        ok = qc >= a.q
        print(f"DN{dn:<4d} di={di:6.1f} mm  v={v:4.2f} m/s  Q_przep={qc:6.2f} l/s  {'OK' if ok else 'za male'}")
        if ok and res is None:
            res = (dn, di, v, qc)
        if a.di:
            break
    if res:
        dn, di, v, qc = res
        # rzeczywiste napelnienie dla Q
        lo, hi = 0.01, a.wypelnienie
        for _ in range(60):
            mid = (lo + hi) / 2
            if hyd(di, s, mid, a.k)[1] < a.q:
                lo = mid
            else:
                hi = mid
        vr = hyd(di, s, hi, a.k)[0]
        print(f"WYNIK: DN{dn}; rzeczywiste h/d ~ {hi:.2f}, v ~ {vr:.2f} m/s przy Q = {a.q} l/s")
        if vr < a.v_min:
            print(f"UWAGA: v = {vr:.2f} m/s < {a.v_min} m/s (samoczyszczenie) - zwieksz spadek.")
        print("Pamietaj: DN odplywu nie mniejsza niz DN najwiekszego podlaczonego przewodu/pionu; nie zmniejszaj w kierunku przeplywu.")
    else:
        print("Zadna srednica nie spelnia warunku - zwieksz spadek lub DN.")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    d = sp.add_parser("du")
    d.add_argument("--system", type=int, choices=[1, 2, 3, 4], required=True)
    d.add_argument("--uzytkowanie", required=True, help="nieciagle|okresowe|zbiorowe|specjalne lub liczba K")
    d.add_argument("--items", required=True, help='JSON, np. {"wc_6l":3,"umywalka":4}')
    d.add_argument("--qc", type=float, default=0.0)
    d.add_argument("--qp", type=float, default=0.0)
    d.set_defaults(f=cmd_du)
    q = sp.add_parser("podejscie")
    q.add_argument("--system", type=int, choices=[1, 2, 3, 4], required=True)
    q.add_argument("--wentylowane", action="store_true")
    q.add_argument("--q", type=float, required=True)
    q.add_argument("--l", type=float)
    q.add_argument("--luki", type=int)
    q.add_argument("--h", type=float)
    q.add_argument("--spadek", type=float)
    q.set_defaults(f=cmd_podejscie)
    o = sp.add_parser("odplyw")
    o.add_argument("--q", type=float, required=True)
    o.add_argument("--spadek", type=float, required=True, help="[%]")
    o.add_argument("--wypelnienie", type=float, default=0.5)
    o.add_argument("--k", type=float, default=1.0, help="chropowatosc [mm] - zalozenie")
    o.add_argument("--di", type=float, help="srednica wewnetrzna [mm] jednej rury (zamiast tabeli typowych)")
    o.add_argument("--dn-min", type=int, default=50)
    o.add_argument("--v-min", type=float, default=0.7)
    o.set_defaults(f=cmd_odplyw)
    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
