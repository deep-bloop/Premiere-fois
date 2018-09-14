# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
f = lambda x: (3*x+1)/(2*x+1)

def iteration(a,f,n):
    liste=[a]
    for i in range(n):
        liste.append(f(liste[-1]))
    return liste

def estpremier(n):
    if n<2:
        return False
    r=int(sqrt(n)+1)
    for k in range(2,r):
        if n%k == 0:
            return False
    return True
        
def listepremiers(n):
    liste=[]
    for k in range(2,n):
        if estpremier(k):
            liste.append(k)
    return liste

def grospremier(n):
    if n<2:
        return False
    r=int(sqrt(n)+1)
    L=listepremiers(r)
    for k in range(0,len(L)):
        if n%L[k] == 0:
            return False
    return True



def racine(liste):
    newliste=[]
    for k in liste :
        newliste.append(sqrt(k))
    return newliste

2274134858771



def hilb(n):
    L=[]
    for k in range(n):
        l=[]
        for i in range(n):
            l.append(1/(i+k+1))
        L.append(l)
    return np.array(L)
#on voit ici les matrices comme des listes de listes 

def hilb2(n):
    L=[[1/(i+j+1) for j in range(n)] for i in range(n)]
    return np.array(L)

