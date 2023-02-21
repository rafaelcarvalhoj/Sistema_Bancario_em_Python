menu = """
========== MENU ==========
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[nc]Nova conta
[lc]Listar contas
[nu]Novo usuário

=> """




def depositar(valor, extrato, saldo):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato




def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

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
        
    return saldo, extrato, numero_saques




def exibir_extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    
    
    
    
def criar_usuario(usuarios):
    cpf = str(input("Digite seu CPF: "))
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("CPF já registrado")
            return 
        
    nome = str(input("Digite seu nome completo: "))
    data_nascimento = str(input("Digite sua data de nascimento: "))
    endereco = str(input("Digite seu endereco: "))
    usuario = {
        "cpf" : cpf, 
        "nome": nome, 
        "data_nascimento": data_nascimento,
        "endereco" : endereco
        }
    
    print("Usuario criado com sucesso!")
    
    return usuario
    
    
    
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = str(input("Informe o CPF do usuario: "))
    
    existe_usuario = False
    
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            existe_usuario = True
            break
    
    if existe_usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuario nao encontrado")
    
    
    
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        print(linha)
    

    
    
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    contas = []

    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(valor,extrato,saldo)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            #*, saldo, valor, extrato, limite, numero_saques, limite_saques
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            break
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            contas.append(criar_conta(AGENCIA, numero_conta, usuarios))
            
        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == 'nu':
            usuario = criar_usuario(usuarios)
            usuarios.append(usuario)

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
        
        
    
    
main()