'''
Para correr é preciso fazer pip install python-constraint
Input:
Vários pares do tipo:
(Nome,Sec,Ano,Ovr)

'''
from Elemento import Elemento
from Equipa import Equipa
from constraint import Problem
from collections import defaultdict

def criaOvDic(lista):
    over = defaultdict(dict)
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

def fazEquipas(elementos, n_equipas=3, max_solucoes=200000):
    problem = Problem()
    for i, el in enumerate(elementos):
        problem.addVariable(i, range(n_equipas))

    def max_2_secao(*args):
        for equipa in range(n_equipas):
            sec_count = {"II":0, "III":0, "IV":0}
            for idx, equipa_atr in enumerate(args):
                if equipa_atr == equipa:
                    sec_count[elementos[idx].seccao] += 1
            if any(v > 2 for v in sec_count.values()):
                return False
        return True

    def todos_compatíveis(*args):
        for equipa in range(n_equipas):
            membros = [elementos[idx] for idx, equipa_atr in enumerate(args) if equipa_atr == equipa]
            for i in range(len(membros)):
                for j in range(i+1, len(membros)):
                    if membros[j].seccao == membros[i].seccao and membros[j].ano == membros[i].ano:
                        return False
        return True

    def min_4(*args):
        for equipa in range(n_equipas):
            if sum(1 for e in args if e == equipa) < 4:
                return False
        return True

    def pelo_menos_um_de_cada_secao(*args):
        for equipa in range(n_equipas):
            secoes_presentes = set()
            for idx, equipa_atr in enumerate(args):
                if equipa_atr == equipa:
                    secoes_presentes.add(elementos[idx].seccao)
            if not all(sec in secoes_presentes for sec in ["II", "III", "IV"]):
                return False
        return True

    problem.addConstraint(max_2_secao, tuple(range(len(elementos))))
    problem.addConstraint(todos_compatíveis, tuple(range(len(elementos))))
    problem.addConstraint(min_4, tuple(range(len(elementos))))
    problem.addConstraint(pelo_menos_um_de_cada_secao, tuple(range(len(elementos))))

    solucoes = []
    for sol in problem.getSolutionIter():
        solucoes.append(sol)
        if len(solucoes) >= max_solucoes:
            break
    return solucoes

def escreveSolucoesOrdenadas(elementos, solucoes, n_equipas=3, filename="solucoes_equipas_ordenadas.txt"):
    # Calcula a diferença de médias para cada solução
    solucoes_com_dif = []
    for solucao in solucoes:
        medias = []
        for equipa in range(n_equipas):
            membros = [elementos[idx] for idx, equipa_atr in enumerate(solucao.values()) if equipa_atr == equipa]
            if membros:
                media = sum(e.overall for e in membros) / len(membros)
            else:
                media = 0
            medias.append(media)
        diff = max(medias) - min(medias)
        solucoes_com_dif.append((diff, solucao, medias))

    # Ordena as soluções pela diferença de médias (menor para maior)
    solucoes_com_dif.sort(key=lambda x: x[0])

    # Escreve para ficheiro as soluções ordenadas
    with open(filename, "w", encoding="utf-8") as f:
        for idx_sol, (diff, solucao, medias) in enumerate(solucoes_com_dif, 1):
            f.write(f"Solução {idx_sol} (Diferença de médias: {diff:.8f}):\n")
            for equipa in range(n_equipas):
                f.write(f"  Equipa {equipa+1} (Média: {medias[equipa]:.8f}):\n")
                for idx, equipa_atr in enumerate(solucao.values()):
                    if equipa_atr == equipa:
                        f.write(f"    {elementos[idx].toStringSimples()} (OVR: {elementos[idx].overall})\n")
            f.write("\n")
    return

# elementos=[
#     Elemento('Marta','IV',4,97),
#     Elemento('Abelamio','IV',3,95),
#     Elemento('Simao','IV',1,92),
#     Elemento('Jessica','IV',1,85),
#     Elemento('Chico','III',4,92),
#     Elemento('Bea','III',4,85),
#     Elemento('Nuno','III',2,85),
#     Elemento('Subtil','III',2,72),
#     Elemento('Ivo','III',1,70),
#     Elemento('JP','II',4,72),
#     Elemento('Caetano','II',3,72),
#     Elemento('NunoJose','II',3,60),
#     Elemento('Miguel','II',2,55)
# ]

# def construtor(lElem: List[Elemento]):
#     grafo={}
#     for pessoa in lElem:
#         for pessoa2 in lElem:
#             if pessoa != pessoa2:
#                 if pessoa.seccao!=pessoa2.seccao or pessoa.ano!=pessoa2.ano:
#                     if pessoa not in grafo:
#                         grafo[pessoa] = set()
#                     grafo[pessoa].add(pessoa2)
#     return grafo

# def printaGrafo(dic: Dict[Elemento,Set[Elemento]]):
#     for pessoa, amigos in dic.items():
#         print(pessoa.toString())
#         for amigo in amigos:
#             print(amigo.toStringSimples())
#         print()

# #printaGrafo(construtor(elementos))


# def completeEquipa(elementos:Dict[Elemento,Set[Elemento]],equipas:Dict[int,Equipa]):
#     l=0
#     for equipa in equipas:
#         if not complete(equipas[equipa].getEquipa()):
#             return False
#         l+=len(equipas[equipa].getEquipa())
#     if l!=len(elementos):
#         return False
#     return True


# def complete(c:List[Elemento]):
#     '''
#     Função que apenas verifica se o candidato é válido, ou seja, se a equipa está completa
#     '''
#     if len(c)<4:
#         return False
#     regra={
#         "II":2,
#         "III":2,
#         "IV":2
#     }
#     for el in c:
#         regra[el.seccao]-=1
#     for sec in regra:
#         if regra[sec]==2 or regra[sec]<0:
#             return False
#     return True

# def extensions(c:List[Elemento],d:Dict[Elemento,Set[Elemento]],n:int):
#     poss=list(d)
#     for cand in c:
#         for e in list(poss):
#             if e not in d[cand]:
#                 poss.remove(e)
#     return [(n, j) for j in poss]

# #possivel problema de ter a mesma pessoa em várias equipas
# def extensionsEquipa(elementos, equipas):
#     """
#     Gera uma lista de possíveis extensões (i, cand) onde cand é um elemento ainda não usado,
#     pode ser adicionado à equipa i sem violar as restrições de no máximo 2 elementos por secção,
#     e é compatível com todos os membros atuais da equipa segundo o dicionário 'elementos'.
#     """
#     usados = set()
#     for equipa in equipas.values():
#         usados.update(equipa.getEquipa())
#     l = []
#     for i, equipa in equipas.items():
#         equipa_atual = equipa.getEquipa()
#         # Conta elementos por secção na equipa atual
#         sec_count = {"II": 0, "III": 0, "IV": 0}
#         for el in equipa_atual:
#             sec_count[el.seccao] += 1
#         for cand in elementos:
#             if cand not in usados and cand not in equipa_atual:
#                 # Só permite se não exceder 2 por secção
#                 if sec_count[cand.seccao] < 2:
#                     # Verifica compatibilidade com todos os membros da equipa
#                     if all(cand in elementos[el] for el in equipa_atual):
#                         nova_equipa = equipa_atual + [cand]
#                         if len(nova_equipa) <= 6 and (len(nova_equipa) < 6 or complete(nova_equipa)):
#                             l.append((i, cand))
#     return l


# def aux(elementos:Dict[Elemento,Set[Elemento]],equipas:Dict[int,Equipa],lista):
#     if completeEquipa(elementos,equipas):
#         lista.append(copy.deepcopy(equipas))
#         return True  # Para parar à primeira solução
#     # Pruning: se já não há elementos suficientes para completar equipas, termina
#     usados = set()
#     for equipa in equipas.values():
#         usados.update(equipa.getEquipa())
#     if len(usados) > len(elementos):
#         return False
#     for i, x in extensionsEquipa(elementos, equipas):
#         equipas[i].adiciona_elemento(x)
#         if aux(elementos, equipas, lista):
#             return True
#         equipas[i].remove_elemento(x)
#     return False
        

# def fazEquipas(n:int,elem:List[Elemento]):
#     '''
#     n - número de equipas
#     elem - lista de elementos
#     '''
#     lista=[]
#     elementos=construtor(elem)
#     equipas={}
#     for i in range(n):
#         equipas[i]=Equipa(str(i))
#     lista=aux(elementos,equipas,lista)
#     return lista


# #está a fazer mal o extensions ver
# print(fazEquipas(3,elementos))