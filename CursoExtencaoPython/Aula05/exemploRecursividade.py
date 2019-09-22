def ImprimeSequencia(a,b) :
    for x in range(a,b+1) :
        print(x,end=" ")




ImprimeSequencia(14,22)

def imprimeSequencia(a,b) :
    if a==b: print(b)
    else:
        print(a,end=" ")
        imprimeSequencia(a+1,b)

imprimeSequencia(14,22)
