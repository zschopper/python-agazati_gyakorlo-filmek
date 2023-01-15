from film import Film

class Filmek:
    def __init__(self, fajlnev):
        self.__fajlnev = fajlnev
        self.__lista = []
        self.betolt()

    def betolt(self):
        f = open(self.__fajlnev, "r", encoding="utf-8")
        sor = f.readline()
        while sor:
            sor = f.readline()
            if sor:
                elemek = sor.rstrip().split(";")
                self.__lista.append(Film(elemek[0], elemek[1], elemek[2], elemek[3], elemek[4]))
        f.close()

    def filmek_szama(self):
        return len(self.__lista)

    def legrovidebb(self):
        i = 0
        idx = 0
        while i < len(self.__lista):
            f = self.__lista[i]
            if f.jatekido < self.__lista[idx].jatekido:
                idx = i
            i += 1
        return self.__lista[idx].cim

    def hosszabbak(self, jatekido):
        i = 0
        db = 0
        while i < len(self.__lista):
            f = self.__lista[i]
            if f.jatekido > jatekido:
                db += 1
            i += 1
        return db

    def szinesz_filmjei(self, szinesz):
        lista = []
        i = 0
        while i < len(self.__lista):
            f = self.__lista[i]
            if f.foszereplo == szinesz:
                lista.append(f.cim)
            i += 1
        return lista

    def szinesz_filmjei_fajlba(self, szinesz, fajlnev):
        szinesz_filmjei = self.szinesz_filmjei(szinesz)

        if szinesz_filmjei:
            szoveg = f"4. feladat\n\t{szinesz} filmjei: {', '.join(szinesz_filmjei)}"
        else:
            szoveg = f"4. feladat\n\t Nincs a listában {szinesz} főszereplésével film."

        fh = open(fajlnev, "w", encoding="utf-8")
        meret = fh.write(szoveg)
        fh.close()
        return meret

    def rendezok(self):
        i = 0
        ret = {}
        while i < len(self.__lista):
            f = self.__lista[i]
            rendezok = f.rendezo.split(',')
            j = 0
            while j < len(rendezok):
                rendezo = rendezok[j].strip()
                if rendezo in ret:
                    ret[rendezo].append(f)
                else:
                    ret[rendezo] = [f]
                j += 1
            i += 1
        return ret
