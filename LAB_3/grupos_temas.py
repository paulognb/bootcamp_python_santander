temas = dict()

qtde_participantes = int(input())


for i in range(qtde_participantes):
    nome, tema = input().split(',')
    
    """
    o metodo setdefault(chave,valor_da_chave) verifica se a chave passada existe no dicionário
    se não existir, cria a chave e adiciona o valor passado no argumento
    que no caso é uma lista.
    append(item_lista) adiciona o argumento como item de uma lista (que é o valor
    da chave).
    """
   
    temas.setdefault(tema,[]).append(nome)


for tema, nome in temas.items(): #tema: chave - nome: valor --> dic: temas
    print(f"{tema}: {', '.join(nome)}")



