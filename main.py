from function import menu

saldo = 0
extrato = ""
limite = 500
numero_saques = 0
MAXIMO_SAQUE_DIARIO = 3

while True:
    opcao = input(menu())
    
    if opcao == "1":
        valor_deposito = float(input("Quanto deseja depositar? "))
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        
    elif opcao == "2":
        valor_saque = float(input("Quanto deseja sacar? "))
        if valor_saque >= limite:
            print("Limite de saque excedido. Tente novamente mais tarde.")    
        else:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
        if numero_saques >= MAXIMO_SAQUE_DIARIO:
            print("Limite de saques excedido. Tente novamente mais tarde.")
            break
        elif valor_saque > saldo:
            print("Saldo insuficiente.")
            
            
    elif opcao == "3":
        print("EXTRATO".center(50, "="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("SALDO ATUALIZADO".center(50, "="))
        print(f"\nSaldo: R$ {saldo:.2f}\n")
        print("".center(50, "="))
        print(f"\nSaques: {numero_saques}\n")
    elif opcao == "4":
        break