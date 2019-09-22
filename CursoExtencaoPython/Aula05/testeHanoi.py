def hanoi(n, ini, dest, temp) :
    #print(n," ",inicial," ",destino," ",temporario)
    if n == 1 :
        print('Mova um anel', ini, 'para o pino', dest)
    else :
        #print(n,"  ",ini," ",dest," ",temp)
        n1 = int(n)- int(1)
        hanoi(n1, ini, temp, dest)
        
        hanoi('Mova um anel do pino', ini, 'para o pino', dest)
        
        hanoi(n1, temp, dest, ini)

n = 3
hanoi(n, int(1), 2, 3)
