temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

print("Ex01")
# Exercicio 01
for sala in temperaturas:
    for temp in sala:
        print(temp)

print("Ex02")
# Exercicio 02
for sala in temperaturas:
    soma = 0

    for temp in sala:
        soma += temp

    media = soma /len(sala)
    print(media)

print("Ex03")
# Exercicio 03
for sala in temperaturas:
    quantidade = 0

    for temp in sala:
        if temp >= 33:
            quantidade +=1
    print(quantidade)

print("Ex04")
# Exercicio 04
numeroSala = 1
for sala in temperaturas:
    soma = 0
    quantidade = 0

    for temp in sala:
        soma += temp

        if temp >= 33:
            quantidade += 1

    media = soma / len(sala)

    print(f"Sala: {numeroSala}")
    print(f"Media: {media}")
    print(f"Resgistro crítico: {quantidade}")
    print()

    numeroSala += 1

print("Ex05")
# Exercicio 05
maior = 0
maiorSala = 0
numeroSala = 1
for sala in temperaturas:
    quantidade = 0

    for temp in sala:
        if temp >= 33:
            quantidade += 1

    if quantidade > maior:
        maior = quantidade
        maiorSala = numeroSala

    numeroSala += 1

print(f"Sala com maior risco: {maiorSala}")
