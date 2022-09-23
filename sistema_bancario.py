import textwrap

def menu():
    menu = '''
    #################MENU##################

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNovo ususario
    [nc]\tNova conta
    [lc]\tListar contas
    [q]\tSair
    ==> '''

    r_usr = input(textwrap.dedent(menu))
    r_usr = str(r_usr)
    return r_usr

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Desposito"\tR$ {valor:.2f}\n'
        print('\n||||| Deposito realizado com sucesso! |||||')
    else:
        print('\n@@@ Operacao falhou!')

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print('\n@@@ Operacao falhou! Excedeu saldo')
    elif excedeu_limite:
        print('\n@@@ Operacao falhou! Excedeu limite')
    elif excedeu_saques:
        print('\n@@@ Operacao falhou! Excedeu limite de saques')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print('\n||||| Saque realizado com sucesso! |||||')
    else:
        print('\n@@@ Operacao falhou! valor informado invalido')

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('EXTRATO'.center(50, '#'))
    print('nao foram realizadas movimentacoes' if not extrato else extrato)
    print(f'saldo: R${saldo:.2f}')
    print('#'.center(50, '#'))

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (Somente numeros pfv): ')
    usuario = filtar_ususario(cpf, usuarios)

    if usuario:
        print('\n@@@ Ja existe um usuario com esse CPF! @@@')
        return

    nome = input('Digite seu nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aa): ')
    endereco = input('Informe o endereco (logradouro, nro - bairo, cidade/sigla-estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('||||| Usuario criado com sucesso! |||||')

def filtar_ususario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuario: ')
    usuario = filtar_ususario(cpf, usuarios)

    if usuario:
        print('\n||||| Conta criada com sucesso! |||||')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print('\n@@@ Usuario nao encontrado, Criacao de conta encerrada! @@@')

def listar_contas(contas):
    for conta in contas:
        linha = f'''\
                Agencia:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']}

        '''
        print('*' * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        
        if opcao.isnumeric():
            print('selecione uma das opcoes validas pfv!')
            continue

        if opcao == 'd':
            valor_deposito = float(input('digite o valor do deposito: '))
        
            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao == 's':
            valor_saque = float(input('digite o valor do saque: '))
           
            saldo, extrato = sacar(
                    saldo = saldo,
                    valor = valor_saque,
                    extrato = extrato,
                    limite = limite,
                    numero_saques = numero_saques,
                    limite_saques = LIMITE_SAQUES,

                    )

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break

        else:
            print('selecione uma opcao valida pfv')

main()
