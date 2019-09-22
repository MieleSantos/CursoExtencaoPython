#lista os alunos aprovados com notas acima de 6  usando o filter

def aprovado(T):
    nome, nota=T
    return nota>=6




classe = [("joao",3),("asdrubal",7),("mane",9),("jorge",5),("ester",8)]


seq=filter(aprovado,classe)
print(list(seq))
