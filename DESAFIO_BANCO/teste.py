dict_1 = {'nome': 'ana', 'idade': 12}
dict_2 = {'nome': 'paula', 'idade': 14}
dict_3 = {'nome': 'helen', 'idade': 10}

lista_dict = []
lista_dict.append(list(dict_1.items()))
lista_dict.append(list(dict_2.items()))
lista_dict.append(list(dict_3.items()))



print(lista_dict[0][1])

print(lista_dict)

lista_dict.sort(key=lambda x:x[1][1],reverse=True)

print(lista_dict.split())