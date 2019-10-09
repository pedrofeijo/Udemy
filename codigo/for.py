# indicado para um intervalo determinado
for i in range(1, 11):  # o 11 não entra na contage
    print('imprimir {}'.format(i))
# TABUADA
for x in range(1, 11):
    for y in range(1, 11):
        print(f'{x} * {y} = {x*y}'
# pecorre palavra

palavra = "paralelepipedo"
for letra in palavra:
    print(letra, end=',')

# pecorrer lista
aprovados=['Pedro', 'Roger', 'Navar', 'Elias']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print('posição', nome)
