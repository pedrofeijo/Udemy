def ge_dia_semana(dia):
    dias = {
        1:'Segunda',
        2:'Terça',
        3:'Quarta',
        4:'Quinta',
        5:'Sexta',
        6:'Sabado',  
        7:'Domingo',

    }
    return dias.get(dia,'invalido') #caso não seja passado um valor 
    #existente no dicionario usa-se a informação apos a virgula "invalido"

if __name__== "__main__":
    for dia in range(0,15):
        print(f'{dia}: {ge_dia_semana(dia)}')
        if dia in range(1,6):
            print(f'{dia}: {ge_dia_semana(dia)} - Dia da Semana ')
        elif dia in range(6,8):                 
            print(f'{dia}: {ge_dia_semana(dia)} - Final de Semana ')

