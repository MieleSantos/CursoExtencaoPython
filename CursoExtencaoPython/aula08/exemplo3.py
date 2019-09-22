class Funcionario:

    def __init__(self,nome,salario):
        self.__nome=nome
        self.__salario=salario
        self.__bonificacao =0
        
    def imprimir(self):
        print('Nome:',self.getNome(),'Salario:',self.getSalario(),'bonificacao:',self.getBonificacao())
        
    def getNome(self):
        return self.__nome
    
    def getSalario(self):
        return self.__salario
    
    def getBonificacao(self):
        return self.__bonificacao
    
    def setSalario(self,novo_salario):
        self.__salario = novo_salario

    def getBonificacao(self):
        return self.__bonificacao
    
    def setBonificacao(self,bonus):
        self.__bonificacao = bonus

    def calcularSalario(self):
        return print('Salario final:',self.__salario + self.__bonificacao)
    
##classe Administrado
class Administrador(Funcionario):
    #construtor da classe administrador
    def __init__(self,nome,salario,auxilio):
        super().__init__(nome,salario)
        self._ajuda_de_custo = auxilio
    def getAjuda(self):
        return self._ajuda_de_custo
    def imprimir(self):
        print('Nome:',self.getNome(),'Salario:',self.getSalario(),'bonificacao:',self.getBonificacao(),'ajuda de custo:',self.getAjuda())
    def calcularSalario(self):
        return  print('Salario final: ',super().getSalario() + super().getBonificacao() + self._ajuda_de_custo)
    
def main():
    
    fun = Funcionario('Joao',1.25)
    fun.imprimir()
    fun.setSalario(500)
    fun.setBonificacao(50)
    fun.imprimir()
    fun.calcularSalario()

    adm = Administrador('jorge',5000,500)
    adm.setBonificacao(250)
    adm.imprimir()
    adm.calcularSalario()
    
    
main()
