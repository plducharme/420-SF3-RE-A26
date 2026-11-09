

class CaisseOranges:

    def __init__(self, id: int, quantite: int, code: str):
        self.id = id
        self.quantite = quantite
        self.code = code

    def __repr__(self):
        return f"[id: {self.id}, qte: {self.quantite}, code: {self.code}]"

    def __add__(self, other):
        return CaisseOranges(self.id + other.id, self.quantite + other.quantite, self.code + other.code)


class CaissePommes:

    def __init__(self, id: int, quantite: int, code: str):
        self.id = id
        self.quantite = quantite
        self.code = code


caisse_p1 = CaissePommes(1, 50, "HC101")
caisse_p2 = CaissePommes(2, 67, "E23")

# Sans redéfinir les méthodes incluses d'object (magic methods), certaines opérations ne sont pas possibles
print(caisse_p1)
print(caisse_p2)
try:
    caisse3 = caisse_p1 + caisse_p2
except TypeError as te:
    print(te)

co1 = CaisseOranges(1, 43, "Navel1")
co2 = CaisseOranges(2, 64, "STD56")

print(co1)
print(co2)

co3 = co1 + co2
print(co3)





