#Funciona igual a todas as outras linguagens
#while <condição>:
#   statement
#do-while não existe em python
#Em python, o for não aceita atribuição 
#for a in range(b):
#   statement
#for a in lista:
#   statement
#O laço for aceita várias condições
#No final do for podemos colocar else 
number = 0
while number <= 10: 
    print(number, 'não é maior que 10')
    number = int(input())
print(number, ' é maior que 10')

frutas = ['banana', 'maçã', 'abacate', 'goiaba']

for a in frutas:
    print(a)

for b in range(1,11): #Começa em 0!
    print(b)
else:
    print('Final do laço')
#for i=0; i<10; i++ Não é aceito