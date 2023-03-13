#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def Makepair(a,b):
    return a, b
def first(x):
    return x[0]
def second(x):
    return x[1]
def ispair(x):
    return len(x) == 2

#uso il concetto di coppia per implementare le pairlist

#def emptylist():
#    return None
def emptylist():
    return None
def makelist(x,ls=emptylist()):
    return Makepair(x,ls)
def head(ls):
    return first(ls)
def tail(ls):
    return second(ls)
def isempty(ls):
    return ls == emptylist()
    
def printlist(ls):
    def rec(As):
        if not isempty(As):
            print(head(As),end='')
            if not isempty(tail(As)):
                print(',',end='')
            rec(tail(As))
    print('[',end='')
    rec(ls)
    print(']')


def makeintrange(a,b):
    if a>b:
        return emptylist()
    return makelist(a,makeintrange(a+1,b))

cs= makeintrange(1,12)

def arelistequal(ls,bs):
    if isempty(ls) and isempty(bs):
        return True
    elif head(ls)!=head(bs):
        return False
    elif head(ls)==head(bs):
        return arelistequal(tail(ls),tail(bs))
    
def arelistequal2(ls,bs):
    res = False
    if isempty(ls) and isempty(bs):
        res = True
    elif head(ls)==head(bs):
        return  arelistequal2(tail(ls),tail(bs))
    
    
    return res

def leng(ls):
    def iter(As,c):
        if isempty(As):
            return c
        return iter(tail(As),c+1)
    return iter(ls,0)

print(leng(cs))

cs= makeintrange(1,12)
c2s= makeintrange(1,12)
c3s= makeintrange(1,11)

print(arelistequal2(cs,c2s))



def leng2(bs):
    i=0
    while not isempty(bs):
        i=i+1
        bs=tail(bs)

    return i     

def lengricor(ls):
    if isempty(ls):
        return 0
    else:
        i= 1+lengricor(tail(ls))
        return i

def next(ls,n): #successivo dell'elemento n-esimo
    if isempty(ls):
        return emptylist()
    for i in range (0, n, 1):
        ls=tail(ls)
    return head(ls)

def nelement(ls,n): #il primo elemento è quello all'indice zero
    if isempty(ls):
        return emptylist()
    for i in range (0, n-1, 1):
        ls=tail(ls)
    return head(ls)


print(leng2(cs),lengricor(cs),next(cs,4))

def append(As,Bs):
    if isempty(As):
        return Bs
    else:
        return makelist(head(As),append(tail(As), Bs))

print(append(cs,c3s))

    
def contains(ls, value):
    if isempty(ls):
        res = False
    elif head(ls) == value:
        res = True
    else:
        res = contains(tail(ls), value)
    return res 

print(contains(cs, 10), contains(cs, 14))

def removefirst(ls, value):
    if contains(ls, value):
        if head(ls) != value:
            return makelist(head(ls), removefirst(tail(ls), value))
        elif head(ls) == value:
            return tail(ls)
    else:
        return print('value not found') 

bl= append(cs,c3s)
print(removefirst(bl,9))   

def removeall(ls, value):
    if isempty(ls):
        return emptylist()
    else:
        if head(ls) != value:
            return makelist(head(ls), removeall(tail(ls), value))
        elif head(ls) == value:
            return removeall(tail(ls), value)

print(removeall(bl, 10))


def count(ls, value):
    if isempty(ls):
        return 0
    elif head(ls) != value:
        return count(tail(ls), value)
    elif head(ls) == value:
        i = 1 + count(tail(ls), value)
    return i 

print(count(bl, 9))

def reverse(ls):
    def f(ls,rs):
        if isempty(ls):
            return rs
        else:
            return f(tail(ls),makelist(head(ls),rs))
    return f(ls, emptylist())


print(reverse(cs))

def minmax(ls):
    def f(ls,M,m):
        if isempty(ls):
            return Makepair(m , M)
        elif head(ls) > M: 
            M = head(ls)
            return f(tail(ls) , M , m)
        else:
            m = head(ls)
            return f(tail(ls) , M , m)
    return f(ls , head(ls) , head(ls))


print(minmax(removefirst(cs,12)))

def summ(ls):
    if isempty(ls):
        return 0
    else:
        return head(ls) + summ(tail(ls))
            
print(summ(cs))

def product(ls):
    if isempty(ls):
        return 1
    else:
        return head(ls) * product(tail(ls))

print(product(makeintrange(1,5)))

def reduce(ls , F, x0):  #f(a,b) -> c 
    if isempty(ls):
        return x0
    else:
        return F(head(ls), reduce(tail(ls), F , x0))

def sommatoria(Ls):
    return reduce(Ls,lambda x,y:x+y, 0)

def produttoria(Ls):
    return reduce(Ls,lambda x,y:x*y,1)

def fattoriale(n:int):
    def f(n):
        if n <= 1:
            return emptylist()
        return makelist(n,f(n-1))
    return reduce(f(n),lambda x,y:x*y,1)

print(reduce(cs , lambda x,y:x+y , 0))
print(reduce(makeintrange(1,5) , lambda x,y:x*y , 1))

def reduceleft(ls, F, x0):
    if isempty(ls):
        return x0
    else:
        return reduceleft(tail(ls), F, F(head(ls),x0))

print(reduceleft(cs , lambda x,y:x+y , 0))
print(reduceleft(makeintrange(1,5) , lambda x,y:x*y , 1))

def mapp(ls, F):
    if isempty(ls):
        return emptylist()
    else:
        return makelist(F(head(ls), mapp(tail(ls), F)))

def mapp1(ls, F):
    return reduce(ls, lambda x,y:makelist(F(x),y) ,emptylist())

print(mapp1(cs, lambda x:x**2))

def isodd(x):
    if x%2 == 0:
        return False
    else:
        return True

def filterr(ls, P):
    if isempty(ls):
        return emptylist()
    elif P(head(ls)):
        return makelist(head(ls), filterr(tail(ls), P))
    else:
        return filterr(tail(ls), P)

def filterr1(ls, P):
    def concatenate(x,y):
        if P(x):
            return makelist(x,y)
        else:
            return y
    return reduce(ls, concatenate, emptylist())


print(filterr(cs, isodd))
print(filterr1(cs, isodd))



def insertionsort(Ls,Cmp=lambda x,y: x <= y):
    if isempty(Ls):
        return emptylist()
    def insert(L1,value):
        if isempty(L1):
            return makelist(value)
        elif Cmp(head(L1), value):
            return makelist(head(L1),insert(tail(L1),value))
        return makelist(value,L1)
    As = emptylist()
    Bs = Ls
    while not isempty(Bs):
        As = insert(As,head(Bs))
        Bs = tail(Bs)
    return As 
    
    
T = append(mapp1(cs, lambda x:x**3),mapp1(cs, lambda x:x**2))
print(T, insertionsort(T))

def selectionsort(Ls,Cmp=lambda x,y:x <= y):
    if isempty(Ls):
        return emptylist()
    def min(As):
        C = head(As)
        def rec(ls,c):
            if isempty(ls):
                return c
            if Cmp(head(ls),c):
                c = head(ls)
                return rec(tail(ls),c)
            return rec(tail(ls),c)
        return rec(As,C)
    return makelist(min(Ls),selectionsort(removefirst(Ls,min(Ls))))

T = append(mapp1(cs, lambda x:x**3),mapp1(cs, lambda x:x**2))
print(T, selectionsort(T))

def mergesort(Ls,Cmp=lambda x,y:x <= y):
    def merge(As,Bs):
        if isempty(As):
            return Bs
        if isempty(Bs):
            return As
        if Cmp(head(As),head(Bs)):
            return makelist(head(As),merge(tail(As),Bs))
        return makelist(head(Bs),merge(As,tail(Bs)))
    def helve(Cs,Ds,n):
        if n <= 0:
            return Cs,Ds
        return helve(tail(Cs),makelist(head(Cs),Ds),n-1)
    def split(Zs):
        n = leng(Zs)
        if n <= 1:
            return Zs
        mid = n//2
        Ns,Ms = helve(Zs,emptylist(),mid)
        left = split(Ns)
        right = split(Ms)
        return merge(left,right)
    return split(Ls)        

T = append(mapp1(cs, lambda x:x**3),mapp1(cs, lambda x:x**2))
print(T, mergesort(T))

def quicksort(Ls,Cmp=lambda x,y:x <= y):
    if isempty(Ls):
        return emptylist()
    else:
        pivot = head(Ls)
        As = filterr(tail(Ls),lambda z:Cmp(z,pivot))
        Bs = filterr(tail(Ls),lambda z: not Cmp(z,pivot))
        return append(quicksort(As),append(makelist(pivot),quicksort(Bs)))

T = append(mapp1(cs, lambda x:x**3),mapp1(cs, lambda x:x**2))
print(T, quicksort(T))
