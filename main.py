from function import menu

saldo = 0
extrato = ""
limite = 500
numero_saques = 0
MAXIMO_SAQUE_DIARIO = 3
cliente = []
conta = []

def depositar(saldo, extrato,/):
    valor_deposito = float(input("Quanto deseja depositar? "))
    saldo += valor_deposito
    extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
    return saldo, extrato

def sacar(*,saldo, extrato, limite, numero_saques):
    valor_saque = float(input("Quanto deseja sacar? "))
    if valor_saque >= limite:
        print("Limite de saque excedido. Tente novamente mais tarde.")    
    else:
        saldo -= valor_saque
        numero_saques += 1
        extrato += f"Saque: R$ {valor_saque:.2f}\n"
        if numero_saques >= MAXIMO_SAQUE_DIARIO:
            print("Limite de saques excedido. Tente novamente mais tarde.")
            return saldo, extrato, numero_saques
        elif valor_saque > saldo:
            print("Saldo insuficiente.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /,extrato, numero_saques):
    print("EXTRATO".center(50, "="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("SALDO ATUALIZADO".center(50, "="))
    print(f"\nSaldo: R$ {saldo:.2f}\n")
    print("".center(50, "="))
    print(f"\nSaques: {numero_saques}\n")
    
def usuario(nome,data_de_nascimento,cpf,endereco):

        cliente.append(nome)
        cliente.append(cpf)
        cliente.append(endereco)
        cliente.append(data_de_nascimento)
        return cliente

while True:
    opcao = input(menu())
    
    if opcao == "1":
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == "2":
        saldo, extrato, numero_saques = sacar(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques)
    elif opcao == "3":
        exibir_extrato(saldo=saldo, extrato=extrato, numero_saques=numero_saques)
    elif opcao == "4":
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu cpf: ")

        # Verifica se o CPF já existe
        cpf_existe = False
        for c in cliente:
            if c == cpf:
                cpf_existe = True
                print("CPF já existe.")
                break
        
        # Se o CPF não existir, solicita as informações adicionais
        if not cpf_existe:
            endereco = input("Digite seu endereco: ")
            data_de_nascimento = input("Digite sua data de nascimento: ")
            usuario(nome=nome, cpf=cpf, endereco=endereco, data_de_nascimento=data_de_nascimento)

    elif opcao == "5":
        break