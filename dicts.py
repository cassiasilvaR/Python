#Um dicionário(dictionaries) é como um vetor que possui chaves para os seus elementos
#Diferente das tuplas, os elementos podem ser modificados, mas as chaves não podem ser duplicadas
#Os valores podem ser modificados
#Um dicionário pode ser entendido como uma struct 
#Cada chave e valor equivalem como UM elemento
#Os atributos/chaves precisam ser strings, mas os valores não 
#<nome do dicionario> = {
#   '<atributo>'  : 'valor',
#   '<atributo 2> : 'valor2'
#}
my_dict = {
    'name' : 'Tim',
    'age'  :  23,
    'nacionality' : 'Brazilian',
    'friends' : ['Ana', 'Beto', 'Miguel']
}

print(type(my_dict['age'])) #Podemos usar os atributos(chaves) para "buscar" no dicionário, como se fosse um índice 
print(my_dict['friends'][1]) #Para acessar um elemento de uma lista em um dicionário
#print(my_dict[1]) Índices inteiros não podem ser usados em dicionários
print(len(my_dict))