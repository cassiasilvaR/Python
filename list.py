#type() Retorna o tipo da variável passada como parâmetro. Pode ser type(paises[i]) p/ saber o tipo de um elemento
#Uma lista também suporta tipos de dados diferentes ['Brasil', 4, 'India']
#list(('elemento1', 3, True)) construtor da classe list
#.extend(lista) faz uma lista "juntar" com outra
#.append(elemento) adiciona um novo elemento na última posição da lista
#.insert(i, elemento) insere um novo elemento na posição i da lista
#.remove(elemento) remove o elemento da lista
#.clear() remove todos os elementos da lista
#.index(elemento) retorna o indice do elemento na lista
#.count(elemento) conta quantas vezes um elemento aparece na lista 
#.sort() ordena uma lista em ordem crescente
#.reverse() devolve a lista em ordem inversa
#.copy() devolve a cópia de uma lista
#.pop() remove o último elemento da lista. Pode ter índice ou não como parâmetro
#del lista[] deleta a lista toda ou um elemento dela 
#.clear() limpa a lista
paises = ['Brasil', 'Canadá', 'Venezuela', 'Peru', 'Congo'] #Definindo uma lista
cidades = ['Belém', 'Chicago', 'Cape Town', 'Paris']
numeros = [23, 4, 6, 9, 8]
print(paises[:1]) #Antes de 1
print(paises[1:]) #De 1 em diante
print(paises[0:3]) #De 0 até antes de 3
print(paises[1][5]) #Na posição x, pegar o caractere de índice y
paises.extend(cidades)
print(paises)
cidades.append('Veneza')
print(cidades)
numeros.insert(2, 5)
print(numeros)
paises.remove('Canadá')
numeros.sort()
print(numeros)
paises.reverse()
paises2 = paises.copy()
print(paises)
numeros.clear()