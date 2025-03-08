import textwrap

def menu():
    menu = '''
    -------MENU-------
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Novo usuário
    [5] Nova conta
    [6] Listar conta
    [7] Sair
    Digite a opção desejada
    '''
    return input(textwrap.dedent(menu)).strip()


def deposito(saldo, valor, extrato, /): #o que vem antes da / é posicional (positional only)
    if valor > 0:
        saldo += valor
        extrato += f'Depósito de R${valor:.2f}\n'
        print('\nDepósito realizado com sucesso.')
    else:
        print('\nValor inválido. Tente novamente.')
    return saldo, extrato


def saque(*, saldo, valor, extrato, limite_valor, quantidade_saques, LIMITE_SAQUES): #o que vem depois do * é nomeado (keyword only)
    if valor > saldo:
        print('\nVocê não possui saldo suficiente. Tente novamente.')
    elif valor > limite_valor:
        print('\nVocê não pode sacar mais de R$500,00. Tente novamente.')
    elif quantidade_saques > LIMITE_SAQUES:
        print('\nVocê não pode fazer mais de três saques diários. Tente novamente.')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque de R${valor:.2f}\n'
        quantidade_saques += 1
        print('Saque realizado com sucesso.')
    else:
        print('\nValor inválido. Tente novamente.')
        return saldo, extrato


def extrato(saldo, /, *, extrato): #posicional é o saldo (antes do /) e nomeado é o extrato (depois do *)
    print('\n----------EXTRATO----------')
    if not extrato:
        print('Nenhuma movimentação realizada.')
    else:
        print(extrato)
    print(f'Saldo da conta: R${saldo:.2f}')
    print('---------------------------\n')


def novo_usuario(usuarios):
    cpf = input("Digite o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\nJá existe usuário com esse CPF.")
        return

    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o endereço (logradouro, nº - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso.")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = []
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuarios_filtrados.append(usuario)
    if usuarios_filtrados:
        return usuarios_filtrados[0]
    else:
        return None


def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\nConta criada com sucesso.")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nUsuário não encontrado, a criação da conta foi encerrada.")


def listar_conta(contas):
    for conta in contas:
        linha = f'''\
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        '''
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    saldo = 0
    limite_valor = 500
    quantidade_saques= 0
    extrato = ''
    usuarios = []
    contas = []
    
    while True:
        try:
            opcao = int(menu())

            if opcao == 1:
                valor = float(input('Valor do depósito: R$'))
                saldo, extrato = deposito(saldo, valor, extrato)

            elif opcao == 2:
                valor = float(input("Valor do saque: R$"))
                saldo, extrato = saque(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite_valor=limite_valor,
                    quantidade_saques=quantidade_saques,
                    LIMITE_SAQUES=LIMITE_SAQUES
                    )

            elif opcao == 3:
                extrato(saldo, extrato = extrato)

            elif opcao == 4:
                novo_usuario(usuarios)

            elif opcao == 5:
                numero_conta = len(contas) + 1
                conta = nova_conta(AGENCIA, numero_conta, usuarios)
                if conta:
                    contas.append(conta)

            elif opcao == 6:
                listar_conta(contas)

            elif opcao == 7:
                print('\nObrigado por usar nosso banco. Volte sempre.')
                break

        except ValueError:
            print('\nOperação digitada inválida. Tente novamente.')

main()