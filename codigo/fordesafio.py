# receber numeros de 1 a 6 
from random import randint
valor_sorteado = randint(1,7)
for i in range(1,7):
    resto = i%2
    if resto ==0 and valor_sorteado==i:
        print('Acertou')
        break
    else:
        print('Não acertou o número')


        
