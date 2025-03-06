saldo = 0
limite_saque = 500
quantidade_saques= 0
SAQUES_DIARIOS = 3
extrato = ''

while True:
    opcao = int(input('\n[1] Depósito \n[2] Saque \n[3] Extrato \n[4] Sair \nDIGITE A OPÇÃO DESEJADA: '))

    if opcao == 1:
        valor = float(input('\nDigite o valor que deseja depositar: R$'))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito de R${valor:.2f}\n'
        else:
            print('\nValor inválido. Tente novamente')

    elif opcao == 2:
        valor = float(input('\nDigite o valor que deseja sacar: R$'))
        if valor > saldo:
            print('\nVocê não possui saldo suficiente. Tente novamente.')
        elif valor > limite_saque:
            print('\nVocê não pode sacar mais de R$500,00. Tente novamente.')
        elif quantidade_saques > SAQUES_DIARIOS:
            print('\nVocê não pode fazer mais de três saques diários. Tente novamente.')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque de R${valor:.2f}\n'
            quantidade_saques += 1
        else:
            print('\nValor inválido. Tente novamente.')

    elif opcao == 3:
        print('\n----------EXTRATO----------')
        if not extrato:
            print('Nenhuma movimentação realizada.')
        else:
            print(extrato)
        print(f'Saldo da conta: R${saldo:.2f}')
        print('---------------------------\n')

    elif opcao == 4:
        print('\nObrigado por usar nosso banco. Volte sempre.')
        break

    else:
        print('\nOperação digitada inválida. Tente novamente.')