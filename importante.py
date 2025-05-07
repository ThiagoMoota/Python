Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'Linguagem Python'
'Linguagem Python'
"Linguagem Python"
'Linguagem Python'
ling = 'Linguagem Python'
ling
'Linguagem Python'
texto = ''
texto
''
type(texto)
<class 'str'>
texto = 'Linguagem Python'
texto
'Linguagem Python'
len(texto)
16
texto[0]
'L'
texto[1]
'i'

texto[15]
'n'

texto[16]
Traceback (most recent call last):
  File "<pyshell#13>", line 2, in <module>
    texto[16]
IndexError: string index out of range
texto[0] = 'X'
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    texto[0] = 'X'
TypeError: 'str' object does not support item assignment

# String -> homogênea e imutável

#Listas

#construtor list()

# mutável e heterogênea

lista = list()

lista
[]
type(lista)
<class 'list'>
lista = []
lista
[]
lista = [3, True, 3.14, 'Python']
lista
[3, True, 3.14, 'Python']
len(lista)
4
lista[2] = 3.16
list
<class 'list'>
lista
[3, True, 3.16, 'Python']
lista[0] = 20
lista
[20, True, 3.16, 'Python']
lista[3] = 'Java'
lista
[20, True, 3.16, 'Java']
type(lista)
<class 'list'>
#Tuple
# Imutável
# Imutável
# Imutável e heterogênea
#construtor tuple()

tupla = tuple()
tupla
()
type(tupla)
<class 'tuple'>
tupla = ()
tupla
()
type(tupla)
<class 'tuple'>
tupla = (123,)
tupla
(123,)
type(tupla)
<class 'tuple'>
tupla = (123, True, 3.14, 'Python')
tupla
(123, True, 3.14, 'Python')
len(tupla)
4
tupla[1]
True
tupla[3]
'Python'
i = 0
while i<len(tupla):
    print(tupla[i])
    i+=1

    
123
True
3.14
Python

i = 0
while i<len(texto):
    print(texto[i])
    i+=1
    
SyntaxError: multiple statements found while compiling a single statement
tupla
(123, True, 3.14, 'Python')
tupla[1] = false
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    tupla[1] = false
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> 
>>> #intervalo -> range()
>>> #imutáveis e homogênea
>>> #contrutor -> range()
>>> 
>>> # três parâmetros - range(inicio, fim, passo)
>>> # dois parâmetos - range (inicio, fim)
>>> # um parâmetro - range(fim)
>>> 
>>> intervalo = range()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    intervalo = range()
TypeError: range expected at least 1 argument, got 0
>>> intervalo = range(0)
>>> intervalo
range(0, 0)
>>> intervalo = range(5, 10, 2)
>>> intervalo
range(5, 10, 2)
>>> lista = list(intervalo)
>>> lista
[5, 7, 9]
>>> tupla = tuple(intervalo)
>>> tupla
(5, 7, 9)
>>> intervalo[0]
5
>>> tupla[0]
5
>>> intervalo[0] = 70
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    intervalo[0] = 70
TypeError: 'range' object does not support item assignment
