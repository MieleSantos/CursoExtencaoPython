estoque={}

estoque["lapis hb"]=(300,1.20)
estoque["caneta azul"]=(500,1.80)
estoque["borrcha"]=(150,0.90)
estoque["agenda"]=(80,12.80)
estoque["caderno"]=(100,22.80)
estoque["apondador"]=(30,6.40)

print('-12s'%'produto','%10s'%'quantidade','%8s'%'valor')

for produto in estoque:
    quantidade, valor=estoque[produto]
    print('-12s'%produto,'%10d'%quantidade,'%8.2f'%valor)




