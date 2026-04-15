valor_saque = 0
saques = []
saldo = 0
valor_deposito = 0
depositos = []
limite_saque =  500
saque_diario = 3
option = -1
contador_saque = 0
clientes = dict()



def exibir_menu():
    print(" MENU ".center(30,"=" ))

    print(""" 
          
    (1) - Saque
    (2) - Depósito
    (3) - Saldo
    (4) - Extrato
    (5) - Cadastrar Cliente
    (6) - Cadastrar Conta
          
             
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
        
        case 5:
            print(" CADASTRO DE CLIENTE ".center(30,"="))
            cadastrar_cliente()

        case 6:
            cadastrar_conta()


def sacar(valor_saque = valor_saque):

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


def cadastrar_cliente():
    cpf = input("Digite seu CPF: ")
    nome = input("Digite seu NOME: ")
    data_aniversario = input("Digite a DATA DO SEU ANIVERSÁRIO: ")

    clientes.setdefault(cpf,{})["nome"]=nome
    clientes.setdefault(cpf,{})["data_aniversario"]=data_aniversario
    
    endereco = dict()
   
    print("Digite seu ENDEREÇO:")
    endereco["logradouro"] = input("Digite o nome da RUA:")
    endereco["numero"] = (input("Digite o NUMERO: "))
    endereco["Bairro"] = (input("Digite o BAIRRO: "))
    endereco["cidade"] = (input("Digite a CIDADE: "))
    endereco["estado"] = (input("Digite o ESTADO: "))

    clientes.setdefault(cpf,{})["endereco"]=endereco
    

    endereco_valores = list(endereco.values())

    endereço_string = endereco_valores[0]+", "

    for i in range(1,3):
        endereço_string += endereco_valores[i]+" - "

    endereço_string += "/".join(endereco_valores[3:5])

    print(endereço_string)


contas = dict()
AGENCIA = "0001"
num_conta = 0


def cadastrar_conta():
    global num_conta
    num_conta += 1
    cliente = input("Digite seu cpf: ")
    
    conta = dict()

    conta = {'agencia':AGENCIA,'usuario':cliente}
    contas.setdefault(num_conta,{})["conta"]=conta

    # contas.append(conta)

    print(contas)


   
while True:
    exibir_menu()
