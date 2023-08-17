'''
Patrik Bressan
17/08/2023

Deixar com funções e criar duas novas funções:
- cadastrar usuário (cliente)
- cadastrar conta bancária
'''

# Receber argumentos apenas por nome (Keyword only)
# Tudo que vem após o * (asterisco) deve ser nomeado
def saque(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    ultrapassou_saques = numero_saques >= limite_saques
    ultrapassou_saldo = valor > saldo
    ultrapassou_limite = valor > limite

    if ultrapassou_saques:
        print(f'Limite de saques: {numero_saques} atingido!')
    elif ultrapassou_saldo:
        print(f'O seu saldo não é suficiente. Saldo atual: {saldo}.')
    elif ultrapassou_limite:
        print(f'O seu limite não é suficiente. Limite atual: {limite}.')
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f'\nSaque: R$ {valor:.2f}\nSaldo: R$ {saldo:.2f}'
        print('\nSaque realizado com sucesso.')
    else:
        print('\nO valor é inválido!')
    return(saldo, extrato)

# Receber argumentos apenas por posição (positional only)
# Tudo que está antes do barra, tem que ser passado por posição
def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'\nDepósito: R$ {valor:.2f}\nSaldo: R$ {saldo:.2f}'
        print('\nDepósito realizado com sucesso.')
    else:
        print('Opção inválida! Não é possível o depósito de valores negativos.')
    return(saldo, extrato)

# Receber argumentos por posição e nome
# saldo (posição), extrato = extrato (nomeado)
def extrato(saldo, /, *, extrato):
    print('\n$$$$ EXTRATO $$$$')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('\n$$$$ FIM EXTRATO $$$$')

'''
Armazenar tudo em uma lista
nome, data de nascimento, cpf(somente números), endereço(logradouro, nº, bairro, cidade/sigla estado)
Não permitir o cadastro de 2 usuários com o mesmo CPF

DICA:
- para vincular usuário e conta, filtre a lista de usuários por CPF.
- se não achar o CPF, não cria a conta.
- se achar o CPF, cria a conta e vincula nesse mesmo CPF.
'''
def criarUsuario(usuarios):
    cpf = input('Digite o seu CPF (somente os números): ')
    usuario = filtrar_usuario(cpf,usuarios)

    if(usuario):
        print('\nUsuário já existente. Operação inválida!')
        return
    
    nome = input('\nDigite o nome: ')
    data_nascimento = input('Digite a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Digite o endereço - rua, número - bairro - cidade/siga estado: ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print('\nUsuário criado com sucesso.')



def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


'''
Armazenar tudo em uma lista
agência, número da conta e usuário
número da conta é sequencial, iniciando em 1.
Agência é fixo 0001
Usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário.
'''
def criarContaCorrente(agencia, numero_conta, usuarios):
    cpf = input('\nDigite o CPF: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if(usuario):
        print('\nContra corrente criada com sucesso.')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    else:
        print('\nErro: Usuário não encontrado.')


def listar_contas(contas):
    for conta in contas:
        linha = f"""\n
        Agência:{conta['agencia']}
        Cota Corrente:{conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        """
        print(linha)

def menu():
    menu = '''\n
    ########## MENU DE OPÇÕES ##########
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuário
    [5] Nova conta
    [6] Listar contas
    [0] Sair
    '''
    print(menu)
    return(int(input('Digite sua opção: ')))


def main():
    LIMITE_SAQUES = 3
    LIMITE = 500
    AGENCIA = '0001'
    # extrato = f'\n---Extrato Bancário---\nSaldo inicial: {saldo:.2f}'
    numero_saques = 0
    saldo = 0
    extrato = ''
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input('Digite o valor do depósito: '))
            saldo, extrato = deposito(saldo, valor, extrato)
            
        elif opcao == 2:
            valor = float(input('Digite o valor do saque: '))
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=LIMITE,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == 3:
            extrato(saldo, extrato=extrato)
        elif opcao == 4:
            criarUsuario(usuarios)
        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criarContaCorrente(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == 6:
            listar_contas(contas)
        elif opcao == 0:
            print('\nPrograma Finalizado!')
            break
        else:
            print('Opção inválida! Por favor, selecione novamente a operação desejada.')


main()