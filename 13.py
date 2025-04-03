# Fila do Atendimento
fila = []
while True:
    paciente = input("Digite o nome do paciente (ou 'sair' para encerrar): ")
    if paciente.lower() == 'sair':
        break
    fila.append(paciente)
print("Ordem de atendimento:")
while fila:
    print(fila.pop(0))
