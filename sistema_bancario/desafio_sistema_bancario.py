import textwrap
from time import sleep


def menu():
    sleep(1.5)
    menu = """\n
    ================ MENU ================
    [u] Novo usuário
    [c] Nova conta
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [a] Usuários cadastrados
    [b] Contas existentes
    [q] Sair

    => """
    return input(textwrap.dedent(menu))


def validacao_conta(lista_contas: dict):
    cpf = valida_cpf()
    conta = int(input('Digite o número da conta: '))
    agencia = input('Digite o número da agência completo: ')

    if cpf not in lista_contas:
        print('Usuário não tem conta, crie primeiro')
        return

    if conta not in lista_contas[cpf]:
        print('Conta não encontrada')
        return

    if agencia not in lista_contas[agencia]:
        print('Agência não encontrada')


def deposito(saldo, extrato, /):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def saque(*, saldo, limite, numero_saques, extrato):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, numero_saques, extrato


def gera_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def valida_cpf():
    cpf = input('Digite os 11 números do seu CPF: ')

    if len(cpf) != 11:
        print('CPF inválido')
        return
    else:
        return cpf


def cria_usuario(info_usuarios: dict):
    cpf = valida_cpf()
    if cpf:
        if cpf not in info_usuarios:
            nome = input('Digite nome completo: ')
            data = input('Digite data de nascimento: ')
            cidade = input('Digite cidade/sigla do estado: ')

            novo_usuario = {cpf: [nome, data, cidade]}

            info_usuarios.update(novo_usuario)
            print()
            print('Usuário criado, agora você pode criar sua conta!')
        else:
            print('Usuário já existente')
    return info_usuarios


def cria_conta(info_usuarios: dict, lista_contas: dict, ultima_conta: int,
               agencia: str = '0001'):
    cpf = valida_cpf()
    if cpf:
        if cpf in info_usuarios:
            if cpf in lista_contas:
                lista_contas[cpf].append(agencia)
                lista_contas[cpf].append(ultima_conta)
                print(f'Conta {ultima_conta:0>7} criada!!')
                ultima_conta += 1
            else:
                nova_conta = {cpf: [agencia, ultima_conta]}
                lista_contas.update(nova_conta)
                print('Primeira conta criada, parabéns!!')
                print(f'Sua conta é {ultima_conta}')
                ultima_conta += 1

        else:
            print(' Usuário inexistente, crie um primeiro!')

    return info_usuarios, lista_contas, ultima_conta


def lista_usuarios(info_usuarios: dict):
    for cpf in info_usuarios.keys():
        nome, data, cidade = info_usuarios.get(cpf)  # type: ignore
        print(textwrap.dedent(f'''
        ------------------------------
        Usuário : {nome}
        CPF: {cpf}
        Data de nascimento: {data}
        Logradouro: {cidade}
        ------------------------------
        '''))


def listar_contas(lista_contas: dict):
    for cpf in lista_contas.keys():
        dados_contas = lista_contas.get(cpf)  # type: ignore
        print(textwrap.dedent(f'''
        ------------------------------
        Titular : {cpf}
        '''))
        for i, conta in enumerate(dados_contas):  # type: ignore
            if i % 2 == 0:
                print(f'Agência {conta}')
            else:
                print(f'Conta {conta:0>7}')
                print()
        print('------------------------------')


saldo = 0
limite = 500
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3
ultima_conta = 1
usuarios = {}
contas = {}


if __name__ == '__main__':
    while True:

        opcao = menu()

        match opcao:
            case "u":
                usuarios = cria_usuario(usuarios)

            case "c":
                usuarios, contas, ultima_conta = cria_conta(usuarios, contas,
                                                            ultima_conta)

            case "d":
                saldo, extrato = deposito(saldo, extrato)

            case "e":
                gera_extrato(saldo, extrato=extrato)

            case "s":
                saldo, num_saques, extrato = saque(saldo=saldo, limite=limite,
                                                   numero_saques=num_saques,
                                                   extrato=extrato)

            case "a":
                lista_usuarios(usuarios)

            case "b":
                listar_contas(contas)

            case "q":
                break

            case _:
                print('''Operação inválida, por favor selecione
                                novamente a operação desejada.''')
