value1 = int(input('Digite o primeiro número: '))
value2 = int(input('Digite o segundo número: '))
op = input('Digite a operação: ')

if op == '+':
    print(value1 + value2)
elif op == '-':
    print(value1 - value2)
elif op == '/':
    print(value1 / value2)
elif op == '*':
    print(value1 * value2)
else:
    print('Operação inválida')