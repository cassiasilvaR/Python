#.lower() Minúsculas
#.upper() Maiúsculas
#islower() Verdadeiro se é tudo minúsculo, falso se há 1 maiúsculo
#isupper() Verdadeiro se é tudo maiúsculo, falso se há 1 minúsculo
#.lower().islower(), .lower().isupper(), .upper().islower(), .upper().isupper()
#len(string) Tamanho
#name.index('caractere') Devolve a posição desse caractere na string
#name.replace('c1', 'c2') Troca o caracter da esquerda pelo da direita na string 
#str(number) Transforma em uma string
name = 'Cássia'
age = 19
number = 23.12
print(22 + 213.21) # é diferente de print(age + number)
print(name + ' has ' + str(age) + ' y') 
print(name.replace('Cá', 'ta'))