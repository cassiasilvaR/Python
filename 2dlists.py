#Listas dimensionais comportam várias listas dentro de outras
novalista = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

print(novalista[1][0])
#Nested loop: Um loop dentro de outro
for lista in novalista: #Pra printar os elementos da 2dlist individualmente 
    for l in lista:     
        print(l)