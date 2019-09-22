estoque =[["lapis HB",300,1.20],["Caneta Azul",500,1.80],["Borracha",150,0.90],["Agenda", 80, 12.50],["Caderno", 100, 22.80],["Apontador", 30, 6.40]]

#for item in estoque: #item vai recebendo os indices dos elementos da lista
                      #estoque e vai e o print imprime linha por linha
 #print(item)

#for item in estoque:
   # print(item[0],' ',item[1],' ',item[2])

#for item in estoque:
   # for elemento in item:
     #   print(elemento,end="\t")
   # print("")

print('%-12s'%'Produto','%10s'%'Quantidade','%8s'%'Valor')
for item in estoque:
    print('%-12s'%item[0],'%10s'%item[1],'%8s'%item[2])


print('%-12s'%'Produto','%10s'%'Quantidade','%8s'%'Valor','Total')
for item in estoque:   
    print('%-12s'%item[0],'%10d'%item[1],'%8.2f'%item[2],'%8.2f'%(item[1]*item[2])) #multipicando a quantidade pelo valor


for item in estoque:
    total=item[1] *item[2]
    item.append(total)
print(estoque)
