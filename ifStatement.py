#if <condição>:
#   statement
#else:
#   statement
#Em python, podemos usar elif(else if) depois do if
#elif <condição>:
#   statement

value = int(input('Digite um número: '))

if value%2 == 0:
    print(value, 'é par')
elif value%5 == 0:
    print(value, 'é divisível por 5')
else:
    print(value, 'é ímpar')