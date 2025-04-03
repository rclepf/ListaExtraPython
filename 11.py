# Controle de Temperatura
temperaturas = []
for i in range(5):
    temp = float(input(f"Digite a temperatura {i+1}: "))
    temperaturas.append(temp)
print(f"Média: {sum(temperaturas)/5:.2f}, Máxima: {max(temperaturas)}, Mínima: {min(temperaturas)}")
