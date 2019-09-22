def func(x,*args):
     print(x)
     print(args)
     print(*args)

def soma(*elementos):
    s = 0
    for elem in elementos:
         s += elem
         return s

func(1,2,3,4,5)
soma(6,3,5,8)
