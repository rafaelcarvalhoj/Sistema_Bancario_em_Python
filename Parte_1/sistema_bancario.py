menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 100032
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = str(input(menu))
    if opcao == 'd':
        print("Deposito")
        valorDepositado = float(input("Informe o valor a ser depositado: "))
        saldo += valorDepositado
        print(f"R${valorDepositado} depositado com sucesso")                       
    elif opcao == 's':
        if numero_saques < 3:
            print(f"Saldo atual: {saldo:.2f}")
            valorASerSacado = float(input("Quanto você deseja sacar?"))
            if saldo <= valorASerSacado:
                print("Saldo insuficiente para saque\n")
                
            elif valorASerSacado > 500.0:
                print("Limite de R$500.00 para saque excedido\nSaque cancelado!")
            else:
                print("Sacando...")
                saldo -= valorASerSacado
                print("Saque efetuado com sucesso")
                print(f"Saldo atual: R${saldo:.2f}")
                numero_saques += 1
        else:
            print("Limite de saques diarios exedidos")                
    elif opcao == 'e':
        print("Extrato")
        print(f"R$ {saldo:.2f}")
    elif opcao == 'q':
        print("Saindo...")
        break
    else:
        print("Operacao invalida, por favor selecione novamente a operacao desejada.")