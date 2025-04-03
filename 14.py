# Analisador de Números
numeros = []
pares = 0
impares = 0
for i in range(10):
    num = int(input(f"Digite o número {i+1}: "))
    numeros.append(num)
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Pares: {pares}, Ímpares: {impares}, Maior: {max(numeros)}, Menor: {min(numeros)}, Média: {sum(numeros)/10}")
