qtde_pacientes = int(input("Digite a quantidade de pacientes: "))
pacientes = dict()


def adicionar_paciente(nome,idade,status):
    pacientes[nome]={'idade':idade,'status':status}


def ordena_paciente_urgente(lista_urgentes):
    print(lista_urgentes.sorted())


def ordena_paciente_normal(lista_normais):
    print(lista_normais.sorted())



for i in range(0,qtde_pacientes):
    print(f"Paciente {i+1}")
    nome_paciente = input("Nome do paciente: ")
    idade = int(input("Idade do paciente: "))
    status = input("Informar o tipo de atendimento (URGENTE ou NORMAL): ")
    adicionar_paciente(nome_paciente,idade,status)


print(pacientes)

lista_pacientes = []

print(lista_pacientes)

for chave,valores in pacientes.items():

    #dicionario aninhado (pacientes), objetivo é criar dicionario com a chave e o valor
    #(que é o dicionario interno) no mesmo nivel

    dict_unificado = {'nome':chave} | valores
    lista_pacientes.append(dict_unificado)


#dupla ordenação da lista pelo status (ordem alfabetica decrescente) e idade (ordem decrescente)

lista_pacientes.sort(key=lambda x:(x['status'],x['idade']),reverse=True)


print(lista_pacientes)

for i in lista_pacientes:
    print(i['nome'],end=", ")