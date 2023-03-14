import random

palavras = ["python", "programacao", "computador", "teclado", "mouse", "monitor", "internet"]

palavra_secreta = random.choice(palavras)
palavra_secreta_lista = list(palavra_secreta)
sequencia_principal = ["_" for letra in palavra_secreta_lista]

letras_corretas = []

vidas = 6

print(" ".join(sequencia_principal))

while vidas > 0:
    letra = input("\nDigite uma letra: \n")
    if letra in palavra_secreta_lista:
        for i in range(len(palavra_secreta_lista)):
            if letra == palavra_secreta_lista[i]:
                letras_corretas.append(i)
        for i in letras_corretas:
            sequencia_principal[i] = palavra_secreta_lista[i]
        print(" ".join(sequencia_principal))
        if "_" not in sequencia_principal:
            print("\nParabéns, você descobriu a palavra!\n")
            break
    else:
        vidas -= 1
        print(f"\nLetra '{letra}' não está na palavra. Você ainda tem {vidas} vidas.\n")
else:
    print(f"\nVocê perdeu! A palavra era '{palavra_secreta}'.\n")