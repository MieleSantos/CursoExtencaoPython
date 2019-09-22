estoque=[( "lapis HB",300,1.20),("Caneta Azul",500,1.80),("Borracha",150,0.90),
("Agenda", 80, 12.50),("Caderno", 100, 22.80),("Apontador", 30, 6.40)]#tupla dentro de uma lista

for item in estoque:   
    produto,quantidade,valor = item
    print(produto,'',quantidade,'',valor)


for produto, quantidade, valor in estoque:
    print(produto,'',quantidade,'',valor)
