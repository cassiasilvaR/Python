#Ao executar um objeto de uma classe, ele retorna a posição dele na memória
#Em python, o construtor de uma classe é a função __init__, o seu primeiro parâmetro é o 'self', mesmo que o 'this'
#Os atributos da classe não precisam ser instanciados antes 
#O nome dos atributos são os mesmo dentro e fora da classe e não dá erro porque são segmentações de código diferentes 
#class <nome>()->Opcional:
#A herança em python é quando colocamos uma outra classe como "atributo" de uma nova
#Para fazer isso, é preciso criar um novo arquivo e colocar na mesma pasta, do contrário, não funciona
#Para pegar ou colocar atributos na classe pai, chamamos super()
from clss import Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, idade, serie):
        self.serie = serie
        super().__init__(nome, idade)
    
    #pass Possibilita deixar a classe vazia?

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
serie = input('Em que semestre você está? ')

p1 = Aluno(nome, idade, serie)

print(p1.nome + ' tem ' + p1.idade+ ' anos e está no ' + p1.serie + ' semestre.')

del p1 #Deleta o objeto ou um elemento desse objeto