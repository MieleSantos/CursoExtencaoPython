Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
from random import
SyntaxError: invalid syntax
>>> from random import*
>>> random()
0.583758525565696
>>> uniform(4,12)
11.300012060390246
>>> randint(4,12)
12
>>> choice('python web')
' '
>>> L = [2,4,6,8,10,12]
>>> shuffle(L)
>>> L
[4, 6, 8, 10, 2, 12]
>>> choice(L)
10
>>> randint(0,500)
356
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "F:/ADS/Curso de extensao Python/aula4/exercicioSoteio.py", line 2, in <module>
    sorteio = radint(0,501)
NameError: name 'radint' is not defined
>>> ================================ RESTART ================================
>>> 
Digite um numero entre 0 e 500!54
Traceback (most recent call last):
  File "F:/ADS/Curso de extensao Python/aula4/exercicioSoteio.py", line 6, in <module>
    while palpite != sorteado :
NameError: name 'sorteado' is not defined
>>> ================================ RESTART ================================
>>> 
Digite um numero entre 0 e 500!54
Digite um numero entre 0 e 500!47
Digite um numero entre 0 e 500!44
Digite um numero entre 0 e 500!7
Digite um numero entre 0 e 500!4
Digite um numero entre 0 e 500!5
Digite um numero entre 0 e 500!5
Digite um numero entre 0 e 500!7
Digite um numero entre 0 e 500!
>>> ================================ RESTART ================================
>>> 
Digite um numero entre 0 e 500!4
Digite um numero entre 0 e 500!78
Digite um numero entre 0 e 500!50
Digite um numero entre 0 e 500!114
Digite um numero entre 0 e 500!
