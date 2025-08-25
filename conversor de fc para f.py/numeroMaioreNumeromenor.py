print("digite 10 números:")
numeros = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    if num == 0:
        break
    numeros.append(num)
if numeros:
    maior = max(numeros)
    menor = min(numeros)
    print(f"O maior número é {maior} e o menor é {menor}.")
else:
    print("Nenhum número válido foi digitado.")
if numeros:
    print("ordem do menor para o maior:")
    numeros.sort()
    for num in numeros:
        print(num)