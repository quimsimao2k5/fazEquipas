from Elemento import Elemento
from Equipa import Equipa
from collections import defaultdict
from fazEquipa import *
#CÁLCULO DE OVERALL
# 1. Habilidades Técnicas(60%)
#{Construções,Nós,Froissartage, Cartografia}
# 2. Habilidades Interpessoais()
# Trabalho em equipa (capacidade de colaborar, ouvir e ajudar colegas)
# Comunicação (clareza ao explicar ideias, ouvir feedback)
# Liderança (capacidade de organizar, motivar e tomar iniciativa)
# Gestão de conflitos (saber lidar com opiniões diferentes)
# 3. Atitude e Motivação
# Compromisso (assiduidade, pontualidade, dedicação)
# Motivação (vontade de participar e dar o melhor)
# Resiliência (capacidade de lidar com pressão, ter calma e lidar ccom falhas)
# 4. Outros Aspetos
# Criatividade (capacidade de propor soluções inovadoras)
# Gestão de tempo (cumprir prazos, organizar tarefas)
# Experiência em papéis diferentes (ex: já foi líder, já foi membro, já jogou em várias posições)

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

def criaOvDic(lista):
    over = defaultdict(dict)
    lista = [item for sublist in lista for item in sublist]
    stats = [
        ("Tec", "Amar"),
        ("Tec", "Nos"),
        ("Tec", "Frois"),
        ("Tec", "Cart"),
        ("Tec", "Cod"),
        ("Tec", "Fogo"),
        ("Tec", "Soc"),
        ("Interp", "TrabEq"),
        ("Interp", "GestConf"),
        ("Interp", "Lider"),
        ("Interp", "Anim"),
        ("Fis", "DestFis"),
        ("Fis", "DestMan"),
        ("Atit", "Comp"),
        ("Atit", "Mot"),
        ("Atit", "Resil"),
        ("Atit", "Criat"),
        ("Ment", "Intel"),
        ("Ment", "Mem"),
        ("Ment", "Aten"),
        ("VC", "Arrum"),
        ("VC", "Mont"),
        ("VC", "Coop")
    ]
    for (t, s), o in zip(stats, lista):
        over[t][s] = o
    return over

oMarta=criaOvDic([[900,950,750,600,875,700,1000],[950,950,900,750],[850,975],[850,900,900,900],[1000,1000,950],[999,800,999]])
oAbelamio=criaOvDic([[950,999,900,800,950,800,600],[950,700,700,850],[950,900],[900,850,800,800],[975,850,900],[800,999,999]])
oSimao=criaOvDic([[975,999,900,800,950,820,600],[750,750,700,600],[850,920],[999,900,850,900],[900,800,900],[800,999,999]])
oJessica=criaOvDic([[900,900,850,400,750,800,700],[850,700,700,400],[700,950],[900,750,900,750],[900,900,900],[950,900,999]])
oChico=criaOvDic([[965,999,900,820,960,800,600],[750,750,650,400],[960,800],[900,900,820,700],[950,750,900],[800,999,999]])
oBea=criaOvDic([[920,920,700,400,700,650,700],[850,500,600,800],[700,900],[900,800,700,800],[800,850,900],[900,900,999]])
oNuno=criaOvDic([[925,850,850,750,750,750,600],[800,800,850,800],[800,800],[900,900,850,700],[800,750,900],[900,999,999]])
oSub=criaOvDic([[700,700,550,600,550,450,500],[600,800,550,800],[800,600],[900,800,800,700],[700,750,800],[700,700,900]])
oIvo=criaOvDic([[850,800,550,750,750,650,800],[600,500,550,800],[800,800],[300,500,300,700],[700,750,700],[700,800,500]])
oJP=criaOvDic([[800,750,550,700,750,550,500],[800,800,550,600],[650,600],[900,800,700,700],[700,750,850],[800,800,900]])
oCaetano=criaOvDic([[850,750,550,700,750,550,500],[800,800,750,800],[800,700],[800,800,700,700],[760,750,850],[800,800,900]])
oNunoJ=criaOvDic([[650,700,450,500,650,450,600],[550,600,450,800],[500,600],[999,600,600,800],[600,950,700],[800,700,999]])
oMiguel=criaOvDic([[550,600,450,500,650,450,400],[550,600,650,900],[300,500],[900,600,600,700],[500,650,600],[600,600,800]])

Marta = Elemento('Marta', 'IV', 4, oMarta)
Abelamio = Elemento('Abelamio', 'IV', 3, oAbelamio)
Simao = Elemento('Simao', 'IV', 1, oSimao)
Jessica = Elemento('Jessica', 'IV', 1, oJessica)
Chico = Elemento('Chico', 'III', 4, oChico)
Bea = Elemento('Bea', 'III', 4, oBea)
Nuno = Elemento('Nuno', 'III', 2, oNuno)
Subtil = Elemento('Subtil', 'III', 2, oSub)
Ivo = Elemento('Ivo', 'III', 1, oIvo)
JP = Elemento('JP', 'II', 4, oJP)
Caetano = Elemento('Caetano', 'II', 3, oCaetano)
NunoJose = Elemento('NunoJose', 'II', 3, oNunoJ)
Miguel = Elemento('Miguel', 'II', 2, oMiguel)

elementos = [
    Marta,
    Abelamio,
    Simao,
    Jessica,
    Chico,
    Bea,
    Nuno,
    Subtil,
    Ivo,
    JP,
    Caetano,
    NunoJose,
    Miguel
]

solucoes = fazEquipas(elementos, 3, 200000)
if solucoes:
    print(f"Foram encontradas {len(solucoes)} soluções!\n")
    escreveSolucoesOrdenadas(elementos, solucoes, 3)
else:
    print("Não foi encontrada solução.")

