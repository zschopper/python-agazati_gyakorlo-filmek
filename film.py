class Film:

    def __init__(self, cim, rendezo, foszereplo, ev, jatekido):
        # Cím;Rendező;Főszereplő;Év;Perc
        self.cim = cim
        self.rendezo = rendezo
        self.foszereplo = foszereplo
        self.ev = int(ev)
        self.jatekido = int(jatekido)

    def __str__(self):
        return f"c: {self.cim}, {self.ev} játékidő: {self.jatekido}p r: {self.rendezo} f: {self.foszereplo}"
