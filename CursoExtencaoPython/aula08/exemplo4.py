class Gato:
    #construtor
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor
        self.valor=10
        
        #funcao str
    def __str__(self):
        return "gato:" + self.nome + "" + self.cor
    
    def __repr__(self):
        return "gato:" + self.nome + "" + self.cor + "" + self.valor

    def  __call__(self):
        print(self.nome + ':Miau')

    def __int__(self):
        return self.valor

    def __gt__(self,outro):
        return self.valor > outro.valor
#main
def main():
    gato1= Gato('Gafield: ','amarelo')
    gato2 = Gato('Felix','preto')
    # S= str(gato1)
    #print(S)
    #print(gato1.__repr__())
    #gato1.__call__()
    gato1.valor = 15
    gato1 > gato2
   
#main principal
main()
