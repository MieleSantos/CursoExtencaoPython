def hanoi(n, ini, dest, temp) :
    #print(n," ",inicial," ",destino," ",temporario)
    if n == 1 :
        print('Mova um anel', ini, 'para o pino', dest)
    else :
        print(n,"  ",ini," ",dest," ",temp)
        n = n-1
        hanoi(n, ini, temp, dest)
        
        hanoi('Mova um anel do pino', ini, 'para o pino', dest)
        
        hanoi(n, temp, dest, ini)

n = 3
hanoi(n, 1, 2, 3)
