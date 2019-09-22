class Pessoa:

    def __init__(self,nome,idade,cpf):
        self.nome=nome
        self.idade=idade
        self.cpf=cpf
        
    def imprimir(self):
        print('Nome:',self.nome,'idade:',self.idade,'cpf:',self.cpf)

    def fazerAniversario(self):
        self.idade = self.idade + 1
def main():
    brenda = Pessoa('Brenda star',33,'98765432101')
    brenda.imprimir()
    brenda.fazerAniversario()
    brenda.imprimir()

main()
