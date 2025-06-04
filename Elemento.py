class Elemento:
    def __init__(self,nome,seccao,ano,overall):
        self.nome=nome
        self.seccao=seccao
        self.ano=ano
        self.overall=self.calculaOverall(overall)
    
    # Overall={
#     "Técnica 27,5%":{
#         "Amarrações 32,5%": float,
#         "Nós 15%": float,
#         "Froissartage 7,5%":float,
#         "Cartografia, Orientação 10%": float,
#         "Códigos 20%": float,
#         "Fogo 7,5%": float,
#         "Socorrismo 7,5%": float
#     }
#     ,
#     "Interpessoais 17,5%":{
#         "Trabalho em Equipa 55%": float,
#         "Gestão de Conflitos 15%": float,
#         "Liderança 10%": float,
#         "Animação 20%": float
#     }
#     ,
#     "Físicas 12,5%":{
#         "Destreza Física 60%": float,
#         "Destreza Manual 40%": float
#     }
#     ,
#     "Atitude 20%":{
#         "Compromisso 30%": float,
#         "Motivação 30%": float,
#         "Resiliência 15%": float,
#         "Criatividade 15%": float
#     }
#     ,
#     "Mental 15%":{
#         "Inteligência": float,
#         "Memória": float,
#         "Atenção": float
#     }
#     ,
#     "Vida em Campo 7,5%":{
#         "Arrumação": float,
#         "Montagens": float,
#         "Cooperação": float
#     }
# }

    # stats = [
    #     ("Tec", "Amar"),
    #     ("Tec", "Nos"),
    #     ("Tec", "Frois"),
    #     ("Tec", "Cart"),
    #     ("Tec", "Cod"),
    #     ("Tec", "Fogo"),
    #     ("Tec", "Soc"),
    #     ("Interp", "TrabEq"),
    #     ("Interp", "GestConf"),
    #     ("Interp", "Lider"),
    #     ("Interp", "Anim"),
    #     ("Fis", "DestFis"),
    #     ("Fis", "DestMan"),
    #     ("Atit", "Comp"),
    #     ("Atit", "Mot"),
    #     ("Atit", "Resil"),
    #     ("Atit", "Criat"),
    #     ("Ment", "Intel"),
    #     ("Ment", "Mem"),
    #     ("Ment", "Aten"),
    #     ("VC", "Arrum"),
    #     ("VC", "Mont"),
    #     ("VC", "Coop")
    # ]

    def calculaOverall(self, overall):
        # Calcula os valores ponderados para cada categoria principal
        # Ordem: Técnica, Interpessoais, Físicas, Atitude, Mental, Vida em Campo
        over = [0, 0, 0, 0, 0, 0]

        # Técnica 27,5%
        tecnica = (
            overall["Tec"]["Amar"] * 0.325 +
            overall["Tec"]["Nos"] * 0.15 +
            overall["Tec"]["Frois"] * 0.075 +
            overall["Tec"]["Cart"] * 0.10 +
            overall["Tec"]["Cod"] * 0.20 +
            overall["Tec"]["Fogo"] * 0.075 +
            overall["Tec"]["Soc"] * 0.075
        )
        over[0] = tecnica * 0.275

        # Interpessoais 17,5%
        interp = (
            overall["Interp"]["TrabEq"] * 0.55 +
            overall["Interp"]["GestConf"] * 0.15 +
            overall["Interp"]["Lider"] * 0.10 +
            overall["Interp"]["Anim"] * 0.20
        )
        over[1] = interp * 0.175

        # Físicas 12,5%
        fisicas = (
            overall["Fis"]["DestFis"] * 0.60 +
            overall["Fis"]["DestMan"] * 0.40
        )
        over[2] = fisicas * 0.125

        # Atitude 20%
        atitude = (
            overall["Atit"]["Comp"] * 0.30 +
            overall["Atit"]["Mot"] * 0.30 +
            overall["Atit"]["Resil"] * 0.15 +
            overall["Atit"]["Criat"] * 0.15
        )
        over[3] = atitude * 0.20

        # Mental 15%
        mental = (
            overall["Ment"]["Intel"] * 0.50 +
            overall["Ment"]["Mem"] * 0.15 +
            overall["Ment"]["Aten"] * 0.35
        )
        over[4] = mental * 0.15

        # Vida em Campo 7,5%
        vc = (
            overall["VC"]["Arrum"] * 0.4 +
            overall["VC"]["Mont"] * 0.2 +
            overall["VC"]["Coop"] *0.4
        )
        over[5] = vc * 0.075

        # Soma total do overall
        total = sum(over)
        return round(total, 5)

    def __str__(self):
        return "("+self.nome + ' | ' + self.seccao+'|' + str(round((self.overall/10),2))+") "

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