'''
Patrik Bressan
09/08/2023
'''

menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
'''

saldo = 0
LIMITE = 500
extrato = f'\n---Extrato Bancário---\nSaldo inicial: {saldo:.2f}'
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    valor = 0

    if opcao == 'd':
        valor += float(input('Digite o valor do depósito: '))
        if valor > 0:
            saldo += valor
            extrato += f'\nDepósito : R$ {valor:.2f}'
            extrato += f' |   Saldo : R$ {saldo:.2f}'
        else:
            print('Opção inválida! Não é possível o depósito de valores negativos.')
    elif opcao == 's':
        if numero_saques >= LIMITE_SAQUES:
            print(f'Limite de saques: {numero_saques} atingido!')
        else:
            valor = float(input('Digite o valor do saque: '))
            if valor <= LIMITE and valor <= saldo and valor > 0:
                saldo -= valor
                numero_saques += 1
                extrato += f'\nSaque    : R$ {valor:.2f}'
                extrato += f' | Saldo   : R$ {saldo:.2f}'
            else:
                print('\nO limite de saque é de R$ 500,00 por saque ou você não tem saldo o suficiente ou não é permitido sacar valores negativos!')
    elif opcao == 'e':
        print(extrato)
    elif opcao == 'q':
        break
    else:
        print('Opção inválida! Por favor, selecione novamente a operação desejada.')