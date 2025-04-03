# Jogo da Adivinhação
import random
numero_secreto = random.randint(1, 50)
tentativa = 0
while True:
    tentativa = int(input("Adivinhe o número (entre 1 e 50): "))
    if tentativa < numero_secreto:
        print("Tente um número maior.")
    elif tentativa > numero_secreto:
        print("Tente um número menor.")
    else:
        print("Parabéns! Você acertou.")
        break
