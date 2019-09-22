def fatorial(n):
    F=1
    for x in range(1,n+1):
        F*=x
    return F

x= fatorial(5)
print(x)



def Fatorial(n):
    if n==0:
        return 1
    return n*Fatorial(n-1)

print(Fatorial(5))
