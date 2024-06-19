import random
import string

def gerar_senha(comprimento, usar_maiusculas, usar_minusculas, usar_numeros, usar_especiais):
    caracteres = ""
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_especiais:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Nenhum conjunto de caracteres selecionado")

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def obter_criterios_usuario():
    while True:
        try:
            comprimento = int(input("Digite o comprimento desejado para a senha (mínimo 6 caracteres): "))
            if comprimento < 6:
                print("Comprimento muito baixo. Escolha um comprimento de pelo menos 6 caracteres.")
                continue

            usar_maiusculas = input("Usar letras maiúsculas? (s/n): ").lower() == 's'
            usar_minusculas = input("Usar letras minúsculas? (s/n): ").lower() == 's'
            usar_numeros = input("Usar números? (s/n): ").lower() == 's'
            usar_especiais = input("Usar caracteres especiais? (s/n): ").lower() == 's'

            if not (usar_maiusculas or usar_minusculas or usar_numeros or usar_especiais):
                print("Você deve selecionar pelo menos um tipo de caractere.")
                continue

            return comprimento, usar_maiusculas, usar_minusculas, usar_numeros, usar_especiais

        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido para o comprimento.")

def main():
    print("Gerador de Senhas Aleatórias")
    while True:
        comprimento, usar_maiusculas, usar_minusculas, usar_numeros, usar_especiais = obter_criterios_usuario()
        senha = gerar_senha(comprimento, usar_maiusculas, usar_minusculas, usar_numeros, usar_especiais)
        print(f"Senha gerada: {senha}")

        if input("Deseja gerar outra senha? (s/n): ").lower() != 's':
            break

if __name__ == "__main__":
    main()
