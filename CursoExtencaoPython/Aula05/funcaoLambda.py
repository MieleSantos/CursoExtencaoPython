dist = lambda x1,y1,x2,y2:((x2-x1)**2 +(y2-y1)**2)**0.5

print(dist)


fatorial = lambda n : n * fatorial(n-1) if n > 1 else 1

print(fatorial)
