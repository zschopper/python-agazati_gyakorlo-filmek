from filmek import Filmek

f = Filmek("film.txt")
print(f"\n1. feladat\n\tFilmek száma: {f.filmek_szama()}")
print(f"\n2. feladat\n\tA legrövidebb film címe: {f.legrovidebb()}")
jatekido = 110
print(f"\n3. feladat\n\t{f.hosszabbak(jatekido)} db {jatekido} percnél hosszabb film van.")

print("\n4. feladat")
alap_szinesz = "Brad Pitt"
szinesz = input(f"\tAdj meg egy színészt [{alap_szinesz}]: ")
if not szinesz:
    szinesz = alap_szinesz
szinesz_filmjei = f.szinesz_filmjei(szinesz)
if szinesz_filmjei:
    print(f"\t{szinesz} filmjei: {', '.join(szinesz_filmjei)}")
else:
    print(f"\t Nincs a listában {szinesz} főszereplésével film.")

fajlnev = "szinesz_filmjei.txt"
m = f.szinesz_filmjei_fajlba(szinesz, fajlnev)

print(f"\n5. feladat\n\tA szinész filmjeinek listája mentve, a fájl neve {fajlnev}, mérete {m} byte.")

print("\n6. feladat")

rendezok = f.rendezok()
for nev in sorted(f.rendezok().keys()):
    fk = rendezok[nev]
    print(f"\t{nev}, {len(fk)} film:")
    # for f in fk:
    #     print(f"\t\t{f}")
