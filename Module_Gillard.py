#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def listdiv(n):        # Rend la liste des diviseurs de n
    l = []
    for i in range(1,n-1):
        if n%i == 0 : 
            l.append(i)
        else :
            continue
    return l


def somdiv(n):        # Rend la somme des diviseurs de n
    s = 0
    for d in range(1,n//2 + 1): # "//" est la division euclidienne
        if n%d == 0:            # On divise par 2 car aucun diviseur ne sera plus grand que n/2
            s = s + d
    return s


def parfait(n):             # Rend vrai si n est parfait
    return somdiv(n) == n


def listparf(n):            # Rend la liste des nombres parfaits inférieurs à n
    l = []
    for i in range(n):        # range(n) est la "liste" des nombres entre 0 et n
        if parfait(i):
            l.append(i)
    return l
            

def amicaux(n):        # Rend la liste des nombres amicaux inférieurs à n
    l = []
    for i in range(n):
        s = somdiv(i)
        for j in range(i+1,n):
            if s == j and somdiv(j) == i :
                l.append([(i,j)])
    return l


def amicaux2(n):        # Rend la liste des nombres amicaux inférieurs à n
    l = []              # Optimisé
    for i in range(n):
        s = somdiv(i)
        if somdiv(s) == i and i<s<n:
            l.append([(i,s)])
    return l


# Exercice 2


def estpremier(n):        # Dit si un nombre est premier ou non
    if n <= 1:
        return False
    for i in range(2,int(sqrt(n)+1)):
        if n%i == 0:
            return False
    return True


def chanceux(p):      # Dit si un nombre est chanceux (au sens d'Euler) ou non     
    if p in [0,1]:
        return False
    for k in range(p-1):
        n = p + k**2 + k
        if not estpremier(n):
            return False
    return True
    
        
def listchanc(n):         # Affiche la liste des nombres chanceux (au sens d'Euler)
    l = []
    for i in range(2,n):
        if chanceux(i):
            l.append(i)
    return l
    

# Exercice 3


def taxicab(N):          # Rend la liste des nombres inférieurs à N qui s'écrivent de deux manières différentes comme somme de deux cubes
    n = int(N**(1/3))   # Met la racine cubique de n sous forme entière
    liste = []          # Liste que l'on rend à la fin
    for i in range(1,n+1):
        icube = i**3     # Pour calculer i une seule fois et optimiser
        for j in range(i+1,n+1): # Pour ne pas avoir 2 fois le même nombre, on prend les nombres plus grand que i
            s = icube + j**3     # Pour optimiser
            if s <= N:      # Pour ne pas avoir de nombre plus grand que N
                for k in range(i+1,n+1): # Même chose
                    kcube = k**3     # Pour calculer k une seule fois et optimiser
                    for l in range(k+1,n+1): # On prend les nombres plus grands que k
                        if s == kcube + l**3: # On regarde si les sommes des deux cubes sont égales
                            print(f"Le nombre {s} s'écrit {i}^3 + {j}^3 et {k}^3 + {l}^3") # Affiche le nombre s et ses sommes de cube
                            liste.append([s,[i,j],[k,l]]) # liste qui contient le nombre et les deux façons de l'écrire
    return liste 


def f(n):
    s = 0
    for k in range(1,n+1):
        s = s + k
    return s

def g(n):
    s = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            s = s + 1/(i+j)
            print(f"i = {i} , j = {j}")
    return s

def h(x):
    return x

def eval2(f):
    return f(2)



def rectangle(f,a,b,n):
    s = 0
    t = (b-a)/n
    for k in range(0,n):
        s = s + f(a+k*t)
    return t*s

def carree(x):
    return x**2

# lambda x: x**3
    
def euler(eps):
    s = 0
    k = 1
    while 1/k**2 > eps:
        s = s + 1/k**2
        k = k + 1
    print(f"{k} iterations")
    return s

def pair(n):
    if n%2 == 0:
        return True
    else:
        return False
