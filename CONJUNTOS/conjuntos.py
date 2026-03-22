import random

#conjuntos exibe os elementos de forma nao ordenada
print(set("abacaxi")) 

range_inteiros = set()

for i in range(1,101):
    x = 0
    if i % 2 == 0:
        x = random.randint(1,500)
        range_inteiros.add(x)

    else:
        range_inteiros.add(x + random.randint(1000, 2000))


print(range_inteiros)

soma = 0
for i in range_inteiros:
    soma += i

print(soma)

for indice, inteiro in enumerate(range_inteiros):
    print(f"{indice}: {inteiro}")
    
    

