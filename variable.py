#.lower() Minúsculas
#.upper() Maiúsculas
#islower() Verdadeiro se é tudo minúsculo, falso se há 1 maiúsculo
#isupper() Verdadeiro se é tudo maiúsculo, falso se há 1 minúsculo
#.lower().islower(), .lower().isupper(), .upper().islower(), .upper().isupper()
#len(string) Tamanho
#name.index('caractere') Devolve a posição desse caractere na string
#name.replace('c1', 'c2') Troca o caracter da esquerda pelo da direita na string 
#str(number) Transforma em uma string
#int(string) transforma uma string em int
#abs(-9) Módulo de um número
#max(1,2) Escolhe o número máximo
#min(1,2) Escolhe o número mínimo
#round(2.5) Arredonda um número double
#bin(21) Transforma um número em uma string binária
#math biblioteca python
#input() Entrada
from math import * #importar tudo da biblioteca math de python
#sqrt(25) Retorna a raíz de um número

name = 'Cássia'
age = 19
number = 23.12
print(22 + 213.21) # é diferente de print(age + number)
print(name + ' has ' + str(age) + ' y') 
print(name.replace('Cá', 'ta'))
print(abs(-9))
print(max(min(4,1,3), 0))
print(round(3.6))
print(sqrt(4))
eu = input('Olá, qual o sue nome? ')
idade = int(input('Qual a sua idade? '))
print('Olá ' + eu + ' você tem ', idade, ' anos') #a vírgula consegue concatenar uma string com int