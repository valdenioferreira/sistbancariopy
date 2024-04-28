# Sistema Bancário Simples em Python

Este é um sistema bancário simples desenvolvido em Python. Ele permite aos usuários realizar operações básicas como saque, depósito e consulta de extrato.

## Funcionalidades

1. **Realizar Saque**: Os clientes podem sacar uma determinada quantia de dinheiro de sua conta.
2. **Realizar Depósito**: Os clientes podem depositar uma quantia específica de dinheiro em sua conta.
3. **Consultar Extrato**: Os clientes podem verificar o histórico de transações de sua conta.
4. **Criar Cliente**: Pode criar um cliente vinculado ao banco.
5. **Exibir Cliente**: Exibe os dados do Cliente cadastrado como nome e endereço de cadastro.

## Conceitos Utilizados

- **Funções Personalizadas**: O módulo `function` é importado para utilizar a função `menu()`, que exibe o menu de operações bancárias.
- **Laço de Repetição (while)**: O laço `while True` é utilizado para criar um loop contínuo de interação com o usuário, permitindo que ele realize várias operações consecutivas.
- **Estruturas Condicionais (if, elif, else)**: As estruturas condicionais são empregadas para determinar o tipo de operação a ser realizada com base na entrada do usuário, como depósito, saque, consulta de extrato ou saída do programa.
- **Manipulação de Strings (f-strings)**: As f-strings são usadas para formatar e exibir mensagens ao usuário, incluindo valores de saldo, saque e depósito.
- **Controle de Fluxo (break)**: A instrução `break` é utilizada para interromper o loop de operações bancárias quando o limite diário de saques é atingido ou quando o usuário opta por sair do programa.
- **Validação de Limite de Saque**: Verificação do valor do saque em relação ao limite de saque diário e ao saldo disponível na conta do cliente.
- **Armazenamento de Transações em String**: As transações (depósito e saque) são armazenadas em uma string `extrato`, que é exibida quando o usuário solicita o extrato da conta.

## Como Usar

1. Clone este repositório:

https://github.com/valdenioferreira/sistbancariopy.git


2. Navegue até o diretório do projeto:

cd Criando um Sistema Bancário com Python

3. Execute o script `main.py`:

py main.py

4. Siga as instruções no console para realizar as operações desejadas.


        ============= Banco VBank S.A. =============
        
        [1] Depositar
        
        [2] Sacar
        
        [3] Extrato
        
        [4] Criar Cliente
        
        [5] Exibir cliente
        
        [6] Sair
        
        =============================================
    

