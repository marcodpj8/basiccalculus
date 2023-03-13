
def insertionsort(Ls):
    Rs = [i for i in Ls]
    for t in range(1,len(Rs)):
        key = Rs[t]
        i = t-1
        while i >= 0 and Rs[i] > key:
            Rs[i+1] = Rs[i]
            i -= 1
            Rs[i+1] = key
    return Rs
Lista = [19,4,33,72,6,8,1,0,13]

#defining insertion sort in another way

def insertionsort1(Ls):
    Rs = [i for i in Ls]
    for t in range(1,len(Rs)):
        i = t-1
        while i >= 0 and Rs[i] > Rs[t]:
            Rs[i],Rs[t] = Rs[t],Rs[i]
            i -= 1
            t -= 1
    return Rs

print(Lista, insertionsort1(Lista))


def selectionsort(Ls):
    Rs = [i for i in Ls]
    res = []
    while len(Rs) > 0:
        res.append(min(Rs))
        Rs.remove(min(Rs))
    return res

print(selectionsort(Lista))

def selectionsortnativa(Ls):
    Rs = [c for c in Ls]
    for i in range(len(Rs)):
        for j in range(i+1,len(Rs)):
            if Rs[i] > Rs[j]:
                Rs[i],Rs[j]=Rs[j],Rs[i]
    return Rs

print(selectionsortnativa(Lista))


def mergesort(Ls):
    def merge(As, Bs):
        if As == []:
            return Bs
        if Bs == []:
            return As
        if As[0] < Bs[0]:
            return [As[0]]+merge(As[1:],Bs)
        elif  As[0] > Bs[0]:
            return [Bs[0]]+merge(As,Bs[1:])
    mid = len(Ls) // 2
    As, Bs = Ls[:mid], Ls[mid:]
    if len(Ls) <= 1:
        return Ls
    else:
        return merge(mergesort(As),mergesort(Bs))

print(mergesort(Lista))




    
    
    