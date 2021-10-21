#Uma exception para o programa
#try:
#   statement
#exception <erro>(opcional): 
#   statement
#else:(opcional) aqui também pode ser finally:
#   statement                            statement       
try:
    x = int(input())
except ValueError: 
    print('ERROR')