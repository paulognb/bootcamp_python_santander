valor_saque = 0
saques = []
saldo = 0
valor_deposito = 0
depositos = []
limite_saque =  500
saque_diario = 3
option = -1
contador_saque = 0



def exibir_menu():
    print(" MENU ".center(30,"=" ))

    print(""" 
          
    (1) - Saque
    (2) - Depósito
    (3) - Saldo
    (4) - Extrato 
             
    """ )

    option = int(input("Digite sua opção: \n"))
    selecionar_servico(option)


def selecionar_servico(option):

    print("=".center(30,"="))

    match option: 
        case 1:
            if len(saques) < 3:
                print(" SAQUE ".center(30,"="))         
                sacar(float(input("Digite o valor do saque R$: ")))
            else:
                print("Você excedeu sua quantidade de saques diários!")
        
        case 2:
            print(" DEPÓSITO ".center(30,"="))
            depositar(float(input("Digite o valor do deposito R$: ")))

        case 3:
            print(" SALDO ".center(30,"="))
            exibir_saldo()

        case 4:
            print(" EXTRATO ".center(30,"="))
            exibir_extrato()


def sacar(valor_saque):

    if valor_saque > 0:
        global saldo

        if valor_saque <= saldo and valor_saque <= limite_saque:
            saldo -= valor_saque
            saques.append(valor_saque)
            print("saque",len(saques))

        elif valor_saque > saldo:
            print("Seu saldo é insuficiente!")

        elif valor_saque > limite_saque:
            print("Seu limite de saque é R$ 500")
    else:
        print("Erro na operação!")


def depositar(valor_deposito):
    if valor_deposito > 0:
        global saldo
        saldo += valor_deposito
        depositos.append(valor_deposito)
        print(f"O valor depositado foi R$: {valor_deposito:.2f}")
    else:
        print("Erro na operação!")

    
def exibir_saldo():
    print(f"\nSeu saldo é R$: {saldo:.2f}\n")


def exibir_extrato():
    global saldo

    for i in depositos:
        print(f"Entrada R$: {i:.2f}+")

    for j in saques:
        print(f"Saída R$: {j:.2f}-")

    print(" Saldo ".center(30,"="))
    print(f"\nSeu Saldo é R$: {saldo:.2f}\n")


while True:
    exibir_menu()
