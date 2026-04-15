



def exibir_menu():
    print(" MENU ".center(30,"=" ))

    print(""" 
          
    (1) - Saque
    (2) - Depósito
    (3) - Saldo
    (4) - Extrato
    (5) - Cadastrar Cliente
    (6) - Cadastrar Conta
    (7) - listar Contas
    (8) - listar Clientes
          
             
    """ )

    return int(input("Digite sua opção: \n"))


def sacar(*,valor_saque,saldo_nominal,extrato_nominal,limite_saque,saques):

    if valor_saque > 0:

        if valor_saque <= saldo_nominal and valor_saque <= limite_saque:
            saldo_nominal -= valor_saque
            saques.append(valor_saque)
            extrato_nominal += f"Saque: <---- R$ {valor_saque:.2f}\n"
            print("Saque realizado com sucesso!!")
            print("saque",len(saques))

        elif valor_saque > saldo_nominal:
            print("Seu saldo é insuficiente!")

        elif valor_saque > limite_saque:
            print("Seu limite de saque é R$ 500")
    else:
        print("Erro na operação!")

    return saldo_nominal,extrato_nominal


def depositar(valor_deposito,saldo_nominal,extrato_nominal,/):

    if valor_deposito > 0:
        saldo_nominal += valor_deposito
        # depositos.append(valor_deposito)
        extrato_nominal = f"Depósito: ---->  R$ {valor_deposito:.2f}\n"
        print(f"O valor depositado foi R$: {valor_deposito:.2f}")
    else:
        print("Erro na operação!")

    return saldo_nominal, extrato_nominal

    
def exibir_saldo(saldo_atual):
    print(f"Saldo atual R$: {saldo_atual:.2f}")


def exibir_extrato(saldo,/,*,extrato):
    print(extrato)
    print(" Saldo ".center(30,"="))
    print(f"\nSeu Saldo é R$: {saldo:.2f}\n")


def cadastrar_cliente(cli):
    cpf = input("Digite seu CPF: ")

    for k in cli.keys():
        if k == cpf:
            print("Já existe um cliente cadastrado com este cpf")
            return cli
        
    else:
        nome = input("Digite seu NOME: ")
        data_aniversario = input("Digite a DATA DO SEU ANIVERSÁRIO: ")

        cli.setdefault(cpf,{})["nome"]=nome
        cli.setdefault(cpf,{})["data_aniversario"]=data_aniversario
    
        endereco = dict()
    
        print("Digite seu ENDEREÇO:")
        endereco["logradouro"] = input("Digite o nome da RUA:")
        endereco["numero"] = (input("Digite o NUMERO: "))
        endereco["Bairro"] = (input("Digite o BAIRRO: "))
        endereco["cidade"] = (input("Digite a CIDADE: "))
        endereco["estado"] = (input("Digite o ESTADO: "))

        endereco_valores = list(endereco.values())
        endereço_string = endereco_valores[0]+", "

        for i in range(1,3):
            endereço_string += endereco_valores[i]+" - "

        endereço_string += "/".join(endereco_valores[3:5])
        cli.setdefault(cpf,{})["endereco"]=endereço_string
        
        return cli
    




def cadastrar_conta(agencia,num_conta,cli):
    conta = dict()
    is_client_valid = False
    cpf = input("Digite seu cpf: ")



    for cliente_key in cli.keys():
        if cliente_key == cpf:
            is_client_valid = True
            num_conta += 1
            conta = {'agencia':agencia,'numero_conta':num_conta,'titular':cpf}
        
    if is_client_valid == False:
        print("Cliente não cadastrado!!")
    
    return conta,num_conta


def listar_contas(contas_cadastradas,cli):
    agencia = ""
    titular = ""

    for conta, dados  in contas_cadastradas.items():
        agencia = dados['conta']['agencia']
        
        cpf_titular = dados['conta']['titular']

        for cpf in cli:
            if cpf_titular == cpf:
                titular = cli[cpf_titular]['nome']

        print(f"""\n
            Agencia: {agencia}
            C/C: {conta}
            Titular: {titular}
        """)

def listar_clientes(cli):
    cpf_consulta = input("Digite o cpf: ")

    for cpf in cli:
        if cpf_consulta == cpf:

            print(f"""\n
    Nome: {cli[cpf_consulta]['nome']}
    Endereço: {cli[cpf_consulta]['endereco']}
            """)
            


def main():

    AGENCIA = "0001"
    LIMITE_SAQUE =  500
    SAQUE_DIARIO = 3
    contas = dict()
    num_conta = 0
    valor_saque = 0
    saques = []
    saldo = 0
    valor_deposito = 0
    depositos = []
    extrato = ""
    option = -1
    contador_saque = 0
    clientes = dict()
   
    while True:
        option = exibir_menu()

        print("=".center(30,"="))

        match option: 
            case 1:
                if len(saques) < 3:
                    print(" SAQUE ".center(30,"="))         
                    valor_saque = float(input("Digite o valor do saque R$: "))
                    saldo, extrato = sacar(
                        valor_saque=valor_saque,
                        saldo_nominal=saldo,
                        extrato_nominal=extrato,
                        limite_saque=LIMITE_SAQUE,
                        saques=saques,)
                else:
                    print("Você excedeu sua quantidade de saques diários!")
            
            case 2:
                print(" DEPÓSITO ".center(30,"="))
                valor_deposito = float(input("Digite o valor do deposito R$: "))
                saldo, extrato = depositar(valor_deposito,saldo,extrato)

            case 3:
                print(" SALDO ".center(30,"="))
                print(f"Saldo R$: {saldo:.2f}")

            case 4:
                print(" EXTRATO ".center(30,"="))
                exibir_extrato(saldo,extrato=extrato)
            
            case 5:
                print(" CADASTRO DE CLIENTE ".center(30,"="))
                clientes = cadastrar_cliente(clientes)

            case 6:
                print(" CADASTRO DE CONTA ".center(30,"="))
                conta,num_conta = cadastrar_conta(AGENCIA,num_conta,clientes)
                
                if conta:
                    contas.setdefault(num_conta,{})["conta"]=conta

            case 7:
                print(" LISTAR CONTAS ".center(30,"="))
                listar_contas(contas,clientes)
            
            case 8:
                print(" LISTAR CLIENTES ".center(30,"="))
                listar_clientes(clientes)

            

main()
