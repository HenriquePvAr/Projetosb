print("digite uma palavra")
palavra  = input()
contador = 0
for letra in palavra:
    if letra in "aeiouAEIOU":
        contador += 1
print("Número de vogais:", contador)