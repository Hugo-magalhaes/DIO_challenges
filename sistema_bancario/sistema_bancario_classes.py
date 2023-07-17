from time import sleep


class Conta:
    AGENCIA: str = '0001'
    contas: list = []

    def __init__(self, conta: int, agencia: str = AGENCIA,
                 saldo: float = 0, limite: float = 500,
                 extrato: str = "", num_saques: int = 3) -> None:

        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.limite = limite
        self.extrato = extrato
        self.num_saques = num_saques

    def deposito(self):

        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    def saque(self):

        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > self.saldo

        excedeu_limite = valor > self.limite

        excedeu_saques = self.num_saques == 0

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.num_saques -= 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    def gerar_extrato(self):

        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações."
              if not self.extrato else self.extrato)
        print(f"\nSaldo da conta {self.conta}: R$ {self.saldo:.2f}")
        print("==========================================")

    def seleciona_conta(self):
        agencia = input('Digite sua agência: ')

        if agencia != self.agencia:
            print(f'Agência {agencia} não encontrada, tente novamente')
            agencia = input('Digite sua agência: ')

        conta = input('Digite o número da conta sem os zeros à esquerda: ')

        if conta in self.contas:
            return conta
        else:
            print('Conta não encontrada, crie uma conta primeiro')


# class Sistema:

#     def __init__(self, contas: list[Conta] | None = None,
#                  clientes: dict | None = None,
#                  ultima_conta: int = 1) -> None:

#         self.contas = contas or []
#         self.clientes = clientes or {}
#         self._ultima_conta = ultima_conta

#     def _cadastro(self):

#         self.nome = input('Insira seu nome completo: ')
#         # self.data_nascimento = input('Insira sua data de nascimento: ')
#         # self.endereco = input(
#         #     '''Insira seu endereço no formato:
#         # Logradouro - bairro - cidade/Sigla do Estado: ''')

#         self.cria_conta()
#         self.atualiza_banco()

#         print()
#         print(
#             f'''Usuário {self.nome} criado!!! Parabéns,
#             agora você pode fazer seu primeiro depósito,
#             sacar seu dinhero e/ou consultar seu extrato''')

#     def cria_conta(self):
#         self.conta = Conta(self._ultima_conta)
#         self._ultima_conta += 1
#         self.contas.append(self.conta.conta)  # type:ignore
#         print(f'Conta {self.conta.conta:0>7} criada! Parabéns!! ')

#     def valida_usuario(self):
#         cpf = input('Digite o cpf com 11 digitos: ')

#         if len(cpf) != 11:
#             print('Formato inválido de CPF, escreva novamente')
#             cpf = input('Digite o cpf com 11 digitos: ')

#         if cpf not in self.clientes:
#             print('Cadastro inexistente, primeiro você deve criar um')
#             sleep(1)

#             self.cpf = cpf
#             self._cadastro()

#         else:
#             self.cria_conta()

#     def atualiza_banco(self):
#         self.clientes.update(
#             {self.cpf:  self.contas})

#     def validacao_cruzada(self, conta_selecionada):
#         if conta_selecionada in self.clientes[self.cpf]:
#             print(f'Bem-vindo a sua conta {conta_selecionada}')
#             return True
#         print('Conta não encontrada')
#         return False

#     def realiza_operacao(self, function):
#         conta_selecionada = self.conta.seleciona_conta()

#         if self.validacao_cruzada(conta_selecionada):
#             return function()
#         else:
#             print('Operação não realizada')


# sistema = Sistema()

conta = Conta(1)

while True:

    sleep(1)
    menu = """

    [d] Depositar
    [e] Extrato
    [s] Sacar
    [q] Sair

    => """

    opcao = input(menu)

    match opcao:
        # case "c":
        #   sistema.valida_usuario()

        case "d":
            # sistema.realiza_operacao(sistema.conta.deposito)
            conta.deposito()

        case "e":
            # sistema.realiza_operacao(sistema.conta.gerar_extrato)
            conta.gerar_extrato()

        case "s":
            # sistema.realiza_operacao(sistema.conta.saque)
            conta.saque()

        # case "a":
        #     print(conta.clientes)

        case "q":
            break

        case _:
            print('''Operação inválida, por favor selecione
                            novamente a operação desejada.''')
