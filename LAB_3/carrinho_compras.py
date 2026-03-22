qtde_itens = int(input()) #quantidade de itens

produto = ""
valor = ""
total = 0

produtos = dict()

for i in range (qtde_itens):
    produto, valor = input().split() #produto e seu valor
    valor = float(valor)
    produtos[produto] = valor
    total += valor


for produto,valor in produtos.items():
    print(f"{produto}: R${valor:.2f}")

print(f"Total: R${total:.2f}")