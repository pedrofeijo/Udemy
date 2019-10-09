# while True:
#     print("vai demorar")

from random import randint
num_informado = -1 # é um número diferente do randint, 
#se nao pode ser o numero sorteado
numero_secreto = randint(0, 9)

while num_informado != numero_secreto:
    num_informado = int(input("Infome o número: "))

print("Numero secreto {} foi encontrado!".format(numero_secreto))
