from function import menu
import random

saldo = 0
extrato = ""
limite = 500
numero_saques = 0
MAXIMO_SAQUE_DIARIO = 3
cliente = []
conta = []
agencia = "0001"

def depositar(saldo, extrato):
    valor_deposito = float(input("Quanto deseja depositar? "))
    saldo += valor_deposito
    extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
    return saldo, extrato

def sacar(*, saldo, extrato, limite, numero_saques):
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

def exibir_extrato(saldo, extrato, numero_saques):
    print("EXTRATO".center(50, "="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("SALDO ATUALIZADO".center(50, "="))
    print(f"\nSaldo: R$ {saldo:.2f}\n")
    print("".center(50, "="))
    print(f"\nSaques: {numero_saques}\n")
    
def usuario(nome, data_de_nascimento, cpf, endereco):
    cliente = {
        "nome": nome,
        "data_de_nascimento": data_de_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    return cliente
    
def exibir_cliente_cadastrado(nome, endereco):
    dados_cliente = {}
    dados_cliente["nome"] = nome
    dados_cliente["endereco"] = endereco
    return dados_cliente

def criar_conta(cliente, agencia, conta,saldo):
    conta = {
        "numero_da_conta": random.randint(10000, 99999),
        "cliente": cliente,
        "agencia": agencia,
        "saldo": saldo,
        "extrato": ""
    }
    return conta


while True:
    opcao = input(menu())
    
    if opcao == "1":
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == "2":
        saldo, extrato, numero_saques = sacar(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques)
    elif opcao == "3":
        exibir_extrato(saldo, extrato, numero_saques)
    elif opcao == "4":
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu cpf: ")

        # Verifica se o CPF já existe
        cpf_existe = False
        for c in cliente:
            if c == cpf:
                cpf_existe = True
                print(50*"=")
                print("\nEste CPF já tem uma conta cadastrada!.\n")
                print(50*"=")
                break
        
        # Se o CPF não existir, solicita as informações adicionais
        if not cpf_existe:
            endereco = {
                "logradouro": input("Digite sua rua: "),
                "bairro": input("Digite seu bairro: "),
                "cidade": input("Digite sua cidade: "),
                "sigla_do_estado": input("Digite a UF do estado: "),
                "estado": input("Digite seu estado: ")
            }
            data_de_nascimento = input("Digite sua data de nascimento: ")
            novo_cliente = usuario(nome=nome, cpf=cpf, endereco=endereco, data_de_nascimento=data_de_nascimento)
            cliente.append(novo_cliente)
    elif opcao == "5":
        cpf_busca = input("Digite o cpf do cliente: ")

        for c in cliente:
            if c["cpf"] == cpf_busca:
                dados_cliente = exibir_cliente_cadastrado(nome=c["nome"], endereco=c["endereco"])
                print("DADOS DO CLIENTE".center(50, '='))
                print("CLIENTE CADASTRADO NO BANCO".center(50, '='))
                print(f"Nome do Cliente: {dados_cliente['nome']}\n")
                print("ENDERECO DO CLIENTE".center(50, "="))
                endereco_formatado = dados_cliente["endereco"]
                endereco_formatado_str = f"{endereco_formatado['logradouro']} - {endereco_formatado['bairro']} - {endereco_formatado['cidade']}/{endereco_formatado['sigla_do_estado']} - {endereco_formatado['estado']}"
                print(f"Endereço de cadastro: {endereco_formatado_str}")
            else:
                print(f"{cpf_busca} não encontrado no banco VBank, por favor crie uma conta.")
                decisao_conta = input("Deseja criar uma conta? (Sim ou Não) : ")
                if decisao_conta == "Sim":
                    nome = input("Digite seu nome: ")
                    cpf = input("Digite seu cpf: ")

                    # Verifica se o CPF já existe
                    cpf_existe = False
                    for c in cliente:
                        if c["cpf"] == cpf:
                            cpf_existe = True
                            print(50*"=")
                            print("\nEste CPF já tem uma conta cadastrada!.\n")
                            print(50*"=")
                            break
                    
                    # Se o CPF não existir, solicita as informações adicionais
                    if not cpf_existe:
                        endereco = {
                            "logradouro": input("Digite sua rua: "),
                            "bairro": input("Digite seu bairro: "),
                            "cidade": input("Digite sua cidade: "),
                            "sigla_do_estado": input("Digite a UF do estado: "),
                            "estado": input("Digite seu estado: ")
                        }
                        data_de_nascimento = input("Digite sua data de nascimento: ")
                        novo_cliente = usuario(nome=nome, cpf=cpf, endereco=endereco, data_de_nascimento=data_de_nascimento)
                        cliente.append(novo_cliente)
                        pass
                    else:
                        print("Tenha um bom dia!")
                        break
                else:
                    print("Tenha um bom dia!")
                break
    elif opcao == "6":
        agencia
        conta = criar_conta(cliente, agencia, conta,saldo)
        print("CONTA CRIADA COM SUCESSO\n".center(50, "="))
        print(f"Agencia: {conta['agencia']}\n")
        print(f"Conta: {conta['numero_da_conta']}\n")
        print(f"Saldo: {conta['saldo']}\n")
    elif opcao == "7":
        break
