def soma(*elemento):
    s =0
    for elem in elemento:
        s += elem
    return s


print(soma(6,3,5,8))




def Soma(x,*y):
    if x==y():
        return x
    else:
        return x + soma(*y)



print(Soma(2,3,5,6))
