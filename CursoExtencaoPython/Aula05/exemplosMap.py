#Exemplos com map 1
funcao =  lambda x : x**2-3*x+4
sequencia = range(2,30,4)
s= map(funcao,sequencia)
print(list(s))


#Exemplo 2

D= {5:'a',11:'b', 7:'c'}
mod = map(funcao, D)
print(list(D))
