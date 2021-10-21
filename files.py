#Para abrir um arquivo usamos open 
#open('arq.txt', op<w, r+, a, r>) a é append
#.close() fecha o arquivo
#É preciso importar da biblioteca os
#.readable() verifica se o arquivo foi aberto
#Se a abertura somente com o nome do arquivo não funcionar, é preciso copiar o diretório inteiro
#.readline() retorna a primeira linha do arquivo 
#.readlines() retorna todas as linhas do arquivo
#Podemos criar arquivos de variadas extensões 
from os import close
file = open("C:/Users/cassia.rosa/OneDrive - Televisão Morena Ltda/Documentos/Python/paises.txt", "a") #Com w, vai sobrescrever o arquivo, com a, vai concatenar 
file.write('\nEstou aqui\0')
#print(file.readlines()[0]) #Retorna a linha especificada do arquivo
#for lines in file.readlines(): #Se usada com a linha acima dá errado  
#    print(lines)

file.close()
