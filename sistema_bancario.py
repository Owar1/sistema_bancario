menu = '''
    OPCOES DO MINI-BANCO

    [d] = depositar
    [s] = sacar
    [e] = extrato
    [q] = sair

'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor_deposito = int(input('digite o valor do deposito: '))
        if valor_deposito > 500:
            print('limite de deposito e de R$500')
        
        extrato += f'deposito: R${valor_deposito:.2f}\n'
        saldo += valor_deposito

    elif opcao == 's':
        if numero_saques == LIMITE_SAQUES:
            print('limite de saques execidos')

        valor_saque = int(input('digite o valor do saque: '))
        if valor_saque > saldo:
            print('saldo insulficiente')

        saldo -= valor_saque
        extrato += f'saque: R${valor_saque:.2f}\n'
        numero_saques += 1
            
    elif opcao == 'e':
        print('EXTRATO'.center(50, '#'))
        print('nao foram realizadas movimentacoes' if not extrato else extrato)
        print(f'saldo: R${saldo:.2f}')
        print('#'.center(50, '#'))

    elif opcao == 'q':
        break

    else:
        print('selecione uma opcao valida pfv')
