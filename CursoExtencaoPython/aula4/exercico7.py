t = [1,2,3,4,5,6]

def media(s):
    soma=0
    for i in s:
        soma = soma + i
    
    st = soma/len(s)
    return st

print(media(t))
