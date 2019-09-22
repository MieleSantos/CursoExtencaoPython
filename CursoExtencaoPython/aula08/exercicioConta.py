class Conta():

    def __init__(self,numero,saldo):
        self.__numero=numero
        self.__saldo=saldo

    def getNumero(self):
        return self.__numero
    
    def setNumero(self):
        self.__numero = numero
        
    def getSaldo(self):
        return self.__saldo
    
    def setSaldo(self):
        self.__saldo= saldo
        
    def __str__(self):
        return "Conta: " + self.getNumero() + " " + self.getSaldo()
    
    def imprimir(self):
        return print('Conta:',self.getNumero(), 'Saldo:', self.getSaldo())
    
    def saldoDisponivel(self):
        return print('Saldo disponivel:',self.getSaldo())

    def deposito(self,valor):
        return print('deposito de:',valor,'Novo saldo:', self.getSaldo() + valor)

    def saque(self,valor):
         return print('saque de:',valor,'Novo saldo:', self.getSaldo()  - valor)

def main():

    num = Conta(12,1000)
    num.imprimir()
    num.saldoDisponivel()
    num.deposito(200)
    num.saque(50)
    

main()
