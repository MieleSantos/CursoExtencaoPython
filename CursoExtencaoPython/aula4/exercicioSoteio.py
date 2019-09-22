from random import*
sorteio = randint(0,4)
num = int(input("Digite um numero entre 0 e 500!"))
palpite = -1
cont = 0
while palpite != sorteio :
   palpite= int(input("Digite um numero entre 0 e 500!"))
   cont =cont + 1   
if sorteio > palpite :
        print("Seu numero e menor que o sorteado")
       
elif sorteio < palpite :
        print("Seu  numero e maior que o sorteado")
        


print("Voce acertou em "+str(cont) + " tentativas")
