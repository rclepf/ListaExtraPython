# Gerenciador de Estoque
estoque = {}
for i in range(3):
    produto = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    estoque[produto] = preco
print("Estoque atualizado:", estoque)
