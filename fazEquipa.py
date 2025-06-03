'''
Input:
Vários pares do tipo:
(Nome,Sec,Ano,Ovr)

'''
from typing import List, Dict, Set
from Elemento import Elemento
from Equipa import Equipa
import copy


elementos=[
    Elemento('Marta','IV',4,97),
    Elemento('Abelamio','IV',3,95),
    Elemento('Simao','IV',1,92),
    Elemento('Jessica','IV',1,85),
    Elemento('Chico','III',4,92),
    Elemento('Bea','III',4,85),
    Elemento('Nuno','III',2,85),
    Elemento('Subtil','III',2,72),
    Elemento('Ivo','III',1,70),
    Elemento('JP','II',4,72),
    Elemento('Caetano','II',3,72),
    Elemento('NunoJose','II',3,60),
    Elemento('Miguel','II',2,55)
]

def construtor(lElem: List[Elemento]):
    grafo={}
    for pessoa in lElem:
        for pessoa2 in lElem:
            if pessoa != pessoa2:
                if pessoa.seccao!=pessoa2.seccao or pessoa.ano!=pessoa2.ano:
                    if pessoa not in grafo:
                        grafo[pessoa] = set()
                    grafo[pessoa].add(pessoa2)
    return grafo

def printaGrafo(dic: Dict[Elemento,Set[Elemento]]):
    for pessoa, amigos in dic.items():
        print(pessoa.toString())
        for amigo in amigos:
            print(amigo.toStringSimples())
        print()

#printaGrafo(construtor(elementos))


def completeEquipa(elementos:Dict[Elemento,Set[Elemento]],equipas:Dict[int,Equipa]):
    l=0
    for equipa in equipas:
        if not complete(equipas[equipa].getEquipa()):
            return False
        l+=len(equipas[equipa].getEquipa())
    if l!=len(elementos):
        return False
    return True


def complete(c:List[Elemento]):
    '''
    Função que apenas verifica se o candidato é válido, ou seja, se a equipa está completa
    '''
    if len(c)<4:
        return False
    regra={
        "II":2,
        "III":2,
        "IV":2
    }
    for el in c:
        regra[el.seccao]-=1
    for sec in regra:
        if regra[sec]==2 or regra[sec]<0:
            return False
    return True

def extensions(c:List[Elemento],d:Dict[Elemento,Set[Elemento]],n:int):
    poss=list(d)
    for cand in c:
        for e in list(poss):
            if e not in d[cand]:
                poss.remove(e)
    return [(n, j) for j in poss]

#possivel problema de ter a mesma pessoa em várias equipas
def extensionsEquipa(elementos, equipas):
    """
    Gera uma lista de possíveis extensões (i, cand) onde cand é um elemento ainda não usado
    e pode ser adicionado à equipa i sem violar as restrições de no máximo 2 elementos por secção.
    Não modifica nada, apenas devolve as possibilidades.
    """
    usados = set()
    for equipa in equipas.values():
        usados.update(equipa.getEquipa())
    l = []
    for i, equipa in equipas.items():
        equipa_atual = equipa.getEquipa()
        # Conta elementos por secção na equipa atual
        sec_count = {"II": 0, "III": 0, "IV": 0}
        for el in equipa_atual:
            sec_count[el.seccao] += 1
        for cand in elementos:
            if cand not in usados and cand not in equipa_atual:
                # Só permite se não exceder 2 por secção
                if sec_count[cand.seccao] < 2:
                    nova_equipa = equipa_atual + [cand]
                    if len(nova_equipa) <= 6 and (len(nova_equipa) < 6 or complete(nova_equipa)):
                        l.append((i, cand))
    return l


def aux(elementos:Dict[Elemento,Set[Elemento]],equipas:Dict[int,Equipa],lista):
    if completeEquipa(elementos,equipas):
        lista.append(copy.deepcopy(equipas))
        return
    for i,x in extensionsEquipa(elementos,equipas):
        equipas[i].adiciona_elemento(x)
        if aux(elementos,equipas,lista):
            return
        equipas[i].remove_elemento(x)
    return
        

def fazEquipas(n:int,elem:List[Elemento]):
    '''
    n - número de equipas
    elem - lista de elementos
    '''
    lista=[]
    elementos=construtor(elem)
    equipas={}
    for i in range(n):
        equipas[i]=Equipa(str(i))
    lista=aux(elementos,equipas,lista)
    return lista


#está a fazer mal o extensions ver
print(fazEquipas(3,elementos))