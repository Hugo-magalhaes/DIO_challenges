# Resumo do desafio
Criar um sistema bancário no qual pode-se criar um usuário, este usuário criar uma ou várias contas. Além disso, existe funções para depositar, sacar, e gerar extrato da conta. Por fim, há também funções para listar todos os usuários e suas informações ou listar os titulares de conta e suas contas.

## 🔨 Funcionalidades do projeto

- `Funcionalidade 2` `Validação de CPF`: O cpf passa por uma validação de tamanho (11 dígitos) e depois a verificação se ele já existe no sistema. 
- `Funcionalidade 2` `Cadastro de Usuários`: É possível criar um usuário a partir do seu cpf. Após a validação, e se o usuário for novo, é pedido o nome completo, data de nascimento e Logradouro no formato: Cidade/Sigla do estado.
- `Funcionalidade 3` `Criação de Contas`: Para criar uma conta, é necessário estar cadastro no sistema. Será vinculado ao CPF também, então passa pela validação e depois pela verificação CPF cadastrado no sistema. A conta é única, se a possibilidade de criar contas iguais.
- `Funcionalidade 4` `Depósito em Conta`: Pode-se definir o montante e armazena-lo no saldo em conta.
- `Funcionalidade 5` `Saque de conta`: Caso haja saldo em conta, podemos saca-lo, com um limite de 3 saques por conta/interação.
- `Funcionalidade 6` `Gera extrato das movimentações de conta`: A partir da criação da conta, passa a existir um extrato que pode ser gerado a qualquer momento com todas as movimentações feitas.
- `Funcionalidade 7` `Listagem de usuários e Listagem de contas`: Para a gestão do sistema, é possível listar todos os usuários com seus dados inputados no sistema, o mesmo acontece caso queira listar os titulares de conta e suas contas.

## ✔️ Técnicas e tecnologias utilizadas

- ``Python``
- ``Definição de funções``
- ``Manipulação de listas e dicionários``
- ``Laços de repetição``

## 📁 Acesso ao projeto
Você pode acessar os arquivos do projeto clicando [aqui](https://github.com/Hugo-magalhaes/DIO_challenges/blob/main/sistema_bancario/desafio_sistema_bancario.py).