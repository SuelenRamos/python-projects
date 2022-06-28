
print('##################### CALCULADORA ######################\n\n')
print('Selecione a operação desejada:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n\n')


while True:
    opcao = int(input('Digite sua opção  (1, 2, 3 ou 4): '))

    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))

    if opcao == 1:
        resposta = n1+n2
        print(n1, '+', n2, '=', resposta)
    elif opcao == 2:
        resposta = n1 - n2
        print(n1, '-', n2, '=', resposta)

    elif opcao == 3:
        resposta = n1*n2
        print(n1, 'x', n2, '=', resposta)

    elif opcao == 4:
        resposta = n1/n2
        print(n1, '/', n2, '=', resposta)

    else:
        print('Opção inválida!')
    saida = input('Deseja tentar novamente? S - Sim   N - Não ')

    if saida=='N' or saida=='n':
        print('Encerrando o programa!')
        break

    else:
        continue
