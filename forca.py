import random

# Lista de palavras para o jogo
palavras = ["python", "programacao", "jogo", "forca", "desenvolvimento", "algoritmo"]

def escolher_palavra(lista_de_palavras):
    # Escolhe uma palavra aleatória da lista
    return random.choice(lista_de_palavras)

def exibir_forca(erros):
    # Desenho básico da forca
    estagios = [
        """
           ------
           |    |
           |
           |
           |
           |
           -
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
           -
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
           -
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
           -
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
           -
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
           -
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
           -
        """
    ]
    return estagios[erros]

def jogo_da_forca():
    palavra = escolher_palavra(palavras)
    letras_acertadas = ["_"] * len(palavra)
    letras_erradas = []
    tentativas = 0
    max_tentativas = 6

    print("Bem-vindo ao jogo da Forca!")
    
    while tentativas < max_tentativas:
        print(exibir_forca(tentativas))
        print("Palavra: ", " ".join(letras_acertadas))
        print("Letras erradas: ", " ".join(letras_erradas))
        tentativa = input("Adivinhe uma letra: ").lower()

        if tentativa in letras_erradas or tentativa in letras_acertadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if tentativa in palavra:
            for i in range(len(palavra)):
                if palavra[i] == tentativa:
                    letras_acertadas[i] = tentativa
            if "_" not in letras_acertadas:
                print("Parabéns! Você adivinhou a palavra:", palavra)
                break
        else:
            letras_erradas.append(tentativa)
            tentativas += 1

    if tentativas == max_tentativas:
        print(exibir_forca(tentativas))
        print("Você foi enforcado! A palavra era:", palavra)

if __name__ == "__main__":
    jogo_da_forca()
