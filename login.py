#Criando um login de usuário simples
print('Criar uma conta')
username = input('Digite um nome de usuário:')
password = input('Digite uma senha: ')

print('Sua conta foi criada com sucesso.')
print('Entre!')

username2 = input('Digite seu usuário: ')
password2 = input('Digite a sua senha: ')

if username == username2 and password == password2:
    print('Bem vind@')
else:
    print('Credenciais incorretas')