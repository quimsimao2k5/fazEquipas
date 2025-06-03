from Elemento import Elemento

class Equipa:
    def __init__(self, nome):
        self.nome=nome
        self.elementos=[]

    def adiciona_elemento(self, elemento:Elemento):
        self.elementos.append(elemento)

    def remove_elemento(self, elemento:Elemento):
        self.elementos.remove(elemento)

    def getEquipa(self):
        return self.elementos