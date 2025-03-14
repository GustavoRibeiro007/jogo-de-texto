def intro():
    print("*Chuva caindo*")
    print("A morte nem sempre é sinal do fim, ou talvez seja...")
    input("Você... Você acha que é o fim?")
    
    


def escolha_porta():
    escolha = input("Digite 'esquerda' ou 'direita': ").lower()
    if escolha == 'esquerda':
        print("Você encontrou um baú com tesouros!")
    elif escolha == 'direita':
        print("Você encontrou um monstro e foi derrotado!")
    else:
        print("Escolha inválida! Tente novamente.")
        escolha_porta()

def jogar():
    intro()
    escolha_porta()

if __name__ == "__main__":
    jogar()
