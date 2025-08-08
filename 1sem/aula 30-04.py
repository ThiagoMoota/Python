Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

3 in [1,2,3]
True
5 in [1,2,3]
False

'i' in 'FIAP'
False
'I' in 'FIAP'
True

for i in range(5):
    print(i)

    
0
1
2
3
4

for letra in 'FIAP':
    print(letra)

    
F
I
A
P

#Crie uma estrutura de repetição para percorrer e exibir as letras do alfabeto

for letra in 'abcdefghijklmnopqrstuvwxyz':
    print(letra)

    
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z
>>> 
>>> lista = [1,2,3,4,5,6,7,8,9,10]
>>> for i in lista:
...     print(i)
... 
...     
1
2
3
4
5
6
7
8
9
10
>>> 
>>> #escreva um programa que imprima os numeros pares entre 1-10
>>> 
>>> for i in range(1,11):
...     if i%2==0:
...         print(f'{i} é PAR')
... 
...         
2 é PAR
4 é PAR
6 é PAR
8 é PAR
10 é PAR
>>> dias = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado')
>>> dias
('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado')
>>> for dia in dias:
...     print(dia)
... 
...     
Domingo
Segunda
Terça
Quarta
Quinta
Sexta
Sábado
>>> 
>>> #escreva um programa que leia 5 nomes e exiba a quantidade que iniciam com vogal
>>> 
