def fase2():

    while True:
        print('---------------  FASE 2 -------------------\n')
        print('Aloque 2 CÃES e 1 OSSO em seus respectivos quartos.\n')
        print('[ _ | * | * | * ]\n[ * | C | _ | _ ]')
        casa2 = [[2, 3, 4, 5, 6], [1,[7,8]]]


        posicao_c1 = int(input('Qual a posição que o CÃO deve ficar?: '))
        if posicao_c1 in casa2[0]:
            print('Ops! Esse quarto está ocupado! Tente novamente\n\n')
            continue
        elif posicao_c1 > 8 or posicao_c1 < 1:
            print('Número inválido! Tente novamente\n\n')
            continue
        casa2[0].append(posicao_c1)

        posicao_c2 = int(input('Qual a posição que o CÃO 2 deve ficar?: '))
        if posicao_c2 in casa2[0]:
            print('Ops! Esse quarto está ocupado! Tente novamente\n\n')
            continue
        elif posicao_c2 > 8 or posicao_c2 < 1:
            print('Número inválido! Tente novamente\n\n')
            continue

        casa2[0].append(posicao_c2)

        posicao_o = int(input('Qual a posição que o OSSO deve ficar?: '))
        if posicao_o in casa2[0]:
            print('Ops! Esse quarto está ocupado! Tente novamente\n\n')
            continue
        elif posicao_o > 8 or posicao_o < 1:
            print('Número inválido! Tente novamente\n\n')
            continue

        elif posicao_o == 1 and posicao_c1 in casa2[1][1] and posicao_c2 in casa2[1][1]:
            print('Muito bem! \n\n')
            return fase3()

        elif posicao_o in casa2[1][1]:
            print('Fim de jogo! Você perdeu!')
            go = int(input('Deseja jogar novamente? Não - 0    Sim - 1'))
            if (go == 0):
                return 0
            else:
                return 1

def fase3():

    while True:
        print('---------------  FASE 3 -------------------\n')
        print('Aloque 1 GATO, 1 RATO E 1 OSSO em seus respectivos quartos.\n')
        print('[ _ | * | * | * ]\n[ _ | G | _ | * ]')
        casa3 = [[2,3,4,6,8],[1,5,7]]

        posicao_r1 = int(input('Qual a posição que o RATO deve ficar?: '))
        if posicao_r1 in casa3[0]:
            print('Ops! Esse quarto está ocupado! Tente novamente\n\n')
            continue
        elif posicao_r1 > 8 or posicao_r1 < 1:
            print('Número inválido! Tente novamente\n\n')
            continue

        casa3[0].append(posicao_r1)

        posicao_g1 = int(input('Qual a posição que o GATO deve ficar?: '))
        if posicao_g1 in casa3[0]:
            print('Ops! Esse quarto está ocupado! Tente novamente\n\n')
            continue
        elif posicao_g1 > 8 or posicao_g1 < 1:
            print('Número inválido! Tente novamente\n\n')
            continue

        casa3[0].append(posicao_g1)

        posicao_o1 = int(input('Qual a posição que o OSSO deve ficar?: '))
        if posicao_o1 in casa3[0]:
            print('Ops! Esse quarto está ocupado! Tente novamente\n\n')
            continue
        elif posicao_o1 > 8 or posicao_o1 < 1:
            print('Número inválido! Tente novamente\n\n')
            continue

        elif posicao_r1 != 1 or posicao_o1 != 5 :
            print('Fim de jogo! você perdeu!')
            go = int(input('Deseja jogar novamente? Não - 0    Sim - 1'))
            if (go == 0):
                return 0
            else:
                return 1

        elif posicao_r1 == 1 and posicao_g1 == 7:
            print('Muito bem! \n\n')
            return fase4()

def fase4():

    while True:
        print('---------------  FASE 4 -------------------\n')
        print('Aloque 2 QUEIJOS E 1 OSSO em seus respectivos quartos.\n')
        print('[ _ | _ | _ | * ]\n[ * | R | * | * ]')
        casa4 = [[4,5,6,7,8],[1,3,2]]

        posicao_q1 = int(input('Qual a posição que o PRIMEIRO QUEIJO deve ficar?: '))
        if posicao_q1 in casa4[0]:
            print('Ops! Esse quarto está ocupado! Tente novamente\n\n')
            continue
        elif posicao_q1 > 8 or posicao_q1 < 1:
            print('Número inválido! Tente novamente\n\n')
            continue

        casa4[0].append(posicao_q1)

        posicao_q2 = int(input('Qual a posição que o SEGUNDO QUEIJO deve ficar?: '))
        if posicao_q2 in casa4[0]:
            print('Ops! Esse quarto está ocupado! Tente novamente\n\n')
            continue
        elif posicao_q2 > 8 or posicao_q2 < 1:
            print('Número inválido! Tente novamente\n\n')
            continue

        casa4[0].append(posicao_q2)

        posicao_o1 = int(input('Qual a posição que o OSSO deve ficar?: '))
        if posicao_o1 in casa4[0]:
            print('Ops! Esse quarto está ocupado! Tente novamente\n\n')
            continue
        elif posicao_o1 > 8 or posicao_o1 < 1:
            print('Número inválido! Tente novamente\n\n')
            continue

        elif posicao_q1 == 2 or posicao_q2 == 2:
            print('Fim de jogo! você perdeu!')
            go = int(input('Deseja jogar novamente? Não - 0    Sim - 1'))
            if (go == 0):
                return 0
            else:
                return 1

        elif posicao_q1 == 1 or posicao_q1 == 3  or posicao_q2 ==1 or posicao_q2 == 3:
            print('Parabéns! Você ganhou!')
            return 0




print('HOTEL DOS ANIMAIS E DOIS ALIMENTOS\n')
print('Posições no jogo:\n[1 | 2 | 3 | 4]\n[5 | 6 | 7 | 8]\n      Animais:\nG - Gato    C - Cão\nR - Rato    Q - Queijo\nO - Osso')


while True:
    print('---------------FASE 1-------------------')
    print('Aloque o GATO e o RATO em seus respectivos quartos.')
    print('[ * | * | _ | G ]\n[ R | _ | * | * ]\n')
    posicao_g = int(input('Qual a posição que o GATO deve ficar?: '))
    casa = [[1, 2, 4, 7, 8], [3, 6]]

    if posicao_g in casa[0]:
        print('Ops! Esse quarto está ocupado! Tente novamente\n\n')
        continue

    elif posicao_g > 8 or posicao_g < 1:
        print('Número inválido! Tente novamente\n\n')
        continue
    casa[0].append(posicao_g)

    posicao_r = int(input('Qual a posição que o RATO deve ficar?: '))

    if posicao_r in casa[0] :
        print('Ops! Esse quarto está ocupado! Tente novamente\n\n')
        continue

    elif posicao_r > 8 or posicao_r < 1:
        print('Número inválido! Tente novamente\n\n')
        continue

    elif posicao_g == 6 and posicao_r == 3:
        print('Fim de jogo! Você perdeu!')
        go = int(input('Deseja jogar novamente? Não - 0    Sim - 1'))
        if(go == 0):
             break
        else:
            continue
    elif posicao_g == 3 and posicao_r == 6:
        print('Muito bem! \n\n')
        fim = fase2()
        if fim == 0:
            break


