Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> a
10
>>> b = - 1.2
>>> b
-1.2
>>> c = "ola mundo"
>>> c
'ola mundo'
>>> 
>>> nome =input("Entre com o seu nome:")
Entre com o seu nome:Miele Silva
>>> nome
'Miele Silva'
>>> 
>>> 
>>> num = int(input("Entre com um numero?:"))
Entre com um numero?:100
>>> num
100
>>> num + 10
110
>>> num /5
20.0
>>> num %7
2
>>> altura = float(input("entre com sua altura"))
entre com sua altura1.80
>>> altura
1.8
>>> x= input("digite um numero")
digite um numero4
>>>  y = input("Digite outro valor:")
 
SyntaxError: unexpected indent
>>> 3
3
>>> y = input("Digite outro valor: ")
Digite outro valor: 4
>>> x + y
'44'
>>> 
>>> x = int(input("Digite um numero "))
Digite um numero 7
>>> y = int(input("Digite outro numero "))
Digite outro numero 8
>>> x + y
15
>>> print("Ola mundo")
Ola mundo
>>> 
>>> print("Ola" + "mundo")
Olamundo
>>> print('8+9=', 8 + 9)
8+9= 17
>>> a="aba"
>>> b= "cate"
>>>  c = a + b
 
SyntaxError: unexpected indent
>>> c = a + b
>>> print(c)
abacate
>>>  w = "abc" * 5
 
SyntaxError: unexpected indent
>>> w = "abc"  * 5
>>> print(w)
abcabcabcabcabc
>>> len(w)
15
>>> capitalize(w)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    capitalize(w)
NameError: name 'capitalize' is not defined
>>> x ="ola"
>>> capitalize(x)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    capitalize(x)
NameError: name 'capitalize' is not defined
>>> a.capitalize()
'Aba'
>>> 
w.capitalize()
'Abcabcabcabcabc'
>>> w.count("a")
5
>>> w.startswith("ab")
True
>>> s = "Python"
>>> s
'Python'
>>> s[1:4]
'yth'
>>> s[2:]
'thon'
>>> s[:4]
'Pyth'
>>> q = "paralelepipedo"
>>> len(q)
14
>>> q[3:8]
'alele'
>>> q[:12]
'paralelepipe'
>>> q[5:]
'elepipedo'
>>> q[:-4]
'paralelepi'
>>> q[5:-2]
'elepipe'
>>> 
>>> a = "Um elefante incomoda muita gente"
>>> a[3:20]
'elefante incomoda'
>>> 
>>> frase = input("Digete uma frase: ")
Digete uma frase: ola tudo bem
>>> frase.upper()
'OLA TUDO BEM'
>>> frase.upper(strip())
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    frase.upper(strip())
NameError: name 'strip' is not defined
>>> frase.upper().strip()
'OLA TUDO BEM'
>>> frase.upper() frase.strip()
SyntaxError: invalid syntax
>>> frase.upper()
'OLA TUDO BEM'
>>> frase.strip()
'ola tudo bem'
>>>  a = "um elefante incomoda muita gente"
 
SyntaxError: unexpected indent
>>> a = "um elefante incaomoda muita gente"
>>> a.upper()
'UM ELEFANTE INCAOMODA MUITA GENTE'
>>> a.strip()
'um elefante incaomoda muita gente'
>>> p ="o o"
>>> p.strip()
'o o'
>>> p=" o "
>>> p.strip()
'o'
>>> 

>>> teste ="Apostila de Pyton"
>>> len(teste)
17
>>> a = "python"
>>> a.capitalize()
'Python'
>>> b="linguagem Python"
>>> b.count(n)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    b.count(n)
NameError: name 'n' is not defined
>>> b = "Linguagem Python"
>>> b.count("n")
2
>>> 
>>> c= "Python"
>>> c.startswith
<built-in method startswith of str object at 0x01862580>
>>> c.startswith(Py)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    c.startswith(Py)
NameError: name 'Py' is not defined
>>>  e = "!@#$%"
 
SyntaxError: unexpected indent
>>> e="!@#$%"
>>> e.isalnum()
False
>>> e = "!@#$%f"
>>> e.isalnum()
False
>>> c.startswith("Py")
True
>>> c.lowwer()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    c.lowwer()
AttributeError: 'str' object has no attribute 'lowwer'
>>> c.lower()
'python'
>>> c.upper()
'PYTHON'
>>> c.swapcase()
'pYTHON'
>>> c.title()
'Python'
>>> titulo = "ola de novo"
>>> titulo.title()
'Ola De Novo'
>>> titulo.split()
['ola', 'de', 'novo']
>>> titulo.replace("novo","Python")
'ola de Python'
>>> titulo.find("o")
0
>>> 0
0
>>> equacao ="1+2+3+4"
>>> equacao.split()
['1+2+3+4']
>>> equacao.split("+")
['1', '2', '3', '4']
>>> 
>>> 
>>> a = input("Digite uma frase")
Digite uma fraseOla de novo
>>> b= a.rep
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    b= a.rep
AttributeError: 'str' object has no attribute 'rep'
>>> b= a.replace(" ","_")
>>> b
'Ola_de_novo'
>>> b.upper()
'OLA_DE_NOVO'
>>> 
==== RESTART: F:\ADS\Curso de extensao Python\aula01\exercicio2pagina8.py ====
Digete uma fraseoi de novo
oi de novo
Traceback (most recent call last):
  File "F:\ADS\Curso de extensao Python\aula01\exercicio2pagina8.py", line 3, in <module>
    b = a.replace(" ", "_")
AttributeError: 'NoneType' object has no attribute 'replace'
>>> 
==== RESTART: F:\ADS\Curso de extensao Python\aula01\exercicio2pagina8.py ====
Digete uma frase: oi de novo
oi de novo
Traceback (most recent call last):
  File "F:\ADS\Curso de extensao Python\aula01\exercicio2pagina8.py", line 3, in <module>
    b = a.replace(" ","_")
AttributeError: 'NoneType' object has no attribute 'replace'
>>> 
==== RESTART: F:\ADS\Curso de extensao Python\aula01\exercicio2pagina8.py ====
Digete uma frase: oi de novo
oi de novo
Traceback (most recent call last):
  File "F:\ADS\Curso de extensao Python\aula01\exercicio2pagina8.py", line 2, in <module>
    a.replace(" ","_")
AttributeError: 'NoneType' object has no attribute 'replace'
>>> 
>>> 
>>> 
>>> 

>>> 

>>> 

>>> 

>>> 
>>> 
>>> 
>>> 
>>> frase = input("Digite uma frase")
Digite uma fraseoi de novo
>>> b = frase.lstrip()
>>> b
'oi de novo'
>>> b.rstrip()
'oi de novo'
>>> b = frase.replase(" ","_")
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    b = frase.replase(" ","_")
AttributeError: 'str' object has no attribute 'replase'
>>> 
>>> 
>>> 


>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 
>>> frase = input("Digite uma frase: ")
Digite uma frase: oi de novo
>>> frase1 = frase.replace(" ","_")
>>> frase1.upper()
'OI_DE_NOVO'
>>> frase.split()
['oi', 'de', 'novo']
>>> 
==== RESTART: F:\ADS\Curso de extensao Python\aula01\exercicio2pagina8.py ====
Digete uma frase: oi de novo
['OI', 'DE', 'NOVO']
>>>  x= 3 - 5j
 
SyntaxError: unexpected indent
>>> x = 3 -5j
>>> 3j
3j
>>> 
>>> 



>>> 
>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 


>>> 
>>> 


>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 
>>> 
>>> 
>>> x = 3 - 5j
>>> x = 3j
>>> x **2
(-9+0j)
>>> -9 **0.5
-3.0
>>> 
>>> 
>>> x = input(Digite o primeiro numero: )
SyntaxError: invalid syntax
>>> 
>>> x = input("Digite o primeiro numero: ")
Digite o primeiro numero: 4
>>> y = input("Digite o segundo numero: ")
Digite o segundo numero: 8
>>> 
>>> z = (x**2 + y**2)/(x-y)**2
Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    z = (x**2 + y**2)/(x-y)**2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> 
>>> 
>>> 

>>> 
>>> 
>>> 
>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> x = int(input("Digite o primeiro numero: "))
Digite o primeiro numero: 2
>>> y = int(input("Digite o segundo numero: "))
Digite o segundo numero: 4
>>> z = (x**2 + y**2)/(x-y)**2
>>> z
5.0
>>> x = 5
>>> y = 3
>>> z = (x**2 + y**2)/(x-y)**2
>>> z
8.5
>>> 
>>> x = 5
>>> y = 10
>>> z = (x**2 + y**2)/(x-y)**2
>>> z
5.0
>>> 
>>> 
>>> salario = 100
>>> 
>>> salario * 0,35
(0, 35)
>>> salario = salario  * 0,35
>>> salario
(0, 35)
>>> 
>>> 
>>> sa = 100
>>> sa = sa * 0,35
>>> sa
(0, 35)
>>> sa = 100
>>> salario = sa +0,35
>>> sa + salario
Traceback (most recent call last):
  File "<pyshell#234>", line 1, in <module>
    sa + salario
TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
>>> 
>>> 
>>> 
