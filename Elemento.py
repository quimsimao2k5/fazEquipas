class Elemento:
    def __init__(self,nome,seccao,ano,overral):
        self.nome=nome
        self.seccao=seccao
        self.ano=ano
        self.overall=overral
    
    def __str__(self):
        return "("+self.nome + ' | ' + self.seccao+") "

    def __repr__(self):
        return self.__str__()

    def toStringSimples(self):
        return self.nome
    
    def toString(self):
        return f"{self.nome} | {self.seccao} Secção | {self.ano} na Secção | Overall: {self.overall} "

    def __eq__(self, value):
        if self.nome == value.nome and self.seccao == value.seccao and self.ano == value.ano and self.overall == value.overall:
            return True
        return False
    
    def __hash__(self):
        return hash((self.nome, self.seccao, self.ano, self.overall))