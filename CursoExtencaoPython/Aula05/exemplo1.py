def soma(x,y):
    
    return x +y


def subtracao(x,y):
    return x-y

def imprime(a,b,func):
    resp= func(a,b)
    print(resp)

imprime(10,4,soma)

imprime(10,4,subtracao)
