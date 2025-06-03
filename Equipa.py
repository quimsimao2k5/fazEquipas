from Elemento import Elemento

class Equipa:
    def __init__(self, nome):
        self.nome = nome
        self.elementos = []

    def adiciona_elemento(self, elemento: Elemento):
        self.elementos.append(elemento)

    def remove_elemento(self, elemento: Elemento):
        self.elementos.remove(elemento)

    def getEquipa(self):
        return self.elementos

    def media_ovr(self):
        equipa = self.getEquipa()
        if not equipa:
            return 0.0
        return sum(e.overall for e in equipa) / len(equipa)

    def __str__(self):
        elementos_str = "\n".join(str(e) for e in self.elementos)
        return f"Equipa: {self.nome}\nElementos:\n{elementos_str}"

    def __repr__(self):
        return self.__str__()