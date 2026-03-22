# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# # Entrada do usuário
# preco = float(input("Digite o preço:").strip())
preco = float(input().strip())
# cupom = input("Digite o cupom:").upper().strip()
cupom = input().upper().strip()

# TODO: Aplique o desconto se o cupom for válido:

if cupom == "DESCONTO10":
    preco -= preco*descontos["DESCONTO10"]

elif cupom == "DESCONTO20":
    preco -= preco*descontos["DESCONTO20"]

elif cupom == "SEM_DESCONTO":
    preco -= preco*descontos["SEM_DESCONTO"]

# print(f"preço com desconto R$: {preco:.2f}")
print(f"{preco:.2f}")

