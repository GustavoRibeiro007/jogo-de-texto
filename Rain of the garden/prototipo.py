import sys
import time
import os  # Import necessário para limpar o terminal

def digitar_lento(texto, velocidade=0.05):
    """Imprime o texto na tela como se estivesse sendo digitado lentamente."""
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()  # Adiciona uma nova linha ao final

def input_lento(texto, velocidade=0.05):
    """Exibe o texto como se estivesse sendo digitado lentamente e aguarda o input do usuário."""
    digitar_lento(texto, velocidade)
    return input()

def intro():
    digitar_lento("*Chuva caindo*")
    input_lento("Pressione Enter para continuar...")
    os.system('cls')  # Limpa o terminal
    digitar_lento("Ah... O barulho que a chuva faz... É uma melodia e tanto, não acha?")
    input_lento("...")
    os.system('cls')
    digitar_lento("Você não é muito de papo, não é?")
    input_lento("...")
    os.system('cls')
    digitar_lento("Assim como pensei... Sabe, eu amo a chuva, tempo fechado, me dá uma sensação maravilhosa, como se meu corpo recebesse uma carga de excitação.")
    input_lento("...")
    os.system('cls')
    digitar_lento("Um tempo propício para... Bom, ficar em casa, não é mesmo? Mas por que, então, adoramos sair na chuva, sentir ela na pele, sentir essa sensação como se fosse magia?")
    input_lento("...")
    os.system('cls')
    digitar_lento("Essa emoção de ouvir os pingos no telhado, sentir o cheiro de grama molhada... É bom aproveitar esses momentos em que o céu chora.")
    input_lento("...")
    os.system('cls')
    digitar_lento("Mas, e se essa dádiva que cai do céu fosse prejudicial? Bom, alagamentos, desmoronamentos... Tudo isso é causado pela chuva.")
    input_lento("...")
    os.system('cls')
    digitar_lento("Também tem os acidentes de carro, raios que caem em lugares bem inesperados... Coisas assim, sabe?")
    input_lento("...")
    os.system('cls')
    digitar_lento("E se uma simples chuva puder mudar a sua vida para sempre? Você está em casa, tranquilo e BOOM!!... A chuva cai, você vê a água pingando do seu teto, ela escorrendo pelas paredes...")
    digitar_lento("E, por fim, você se vê em um estado de desespero... Afinal, sua casa foi tomada pela água e você, como um simples humano, não pode impedir a força da natureza.")
    input_lento("...")
    os.system('cls')
    digitar_lento("E se você estiver dirigindo enquanto a chuva cai sobre a pista, e você perde o controle do seu querido e confiável carro, bate em algo, cai de um barranco e simplesmente... Morre.")
    input_lento("...")
    os.system('cls')
    digitar_lento("E se... Você só espera ansiosamente pela chuva, sai de casa para sentir ela na pele, os pingos gelados que fazem seu corpo tremer de animação e, de repente... Você nunca mais é visto...")
    input_lento("...")
    os.system('cls')
    digitar_lento("Foi o que aconteceu com aquela garota... Não é?")
    input_lento("...")
    os.system('cls')
    digitar_lento("Me fala...")
    os.system('cls')

    while True: 
        escolha = input_lento("A morte... É o fim? (Sim ou Não): ").lower()
        if escolha == 'sim':
            os.system('cls')
            digitar_lento("Sério? Acredita mesmo nisso?")
            os.system('cls')
            escolha = input_lento("Não acha que tem algo a mais nessas nossas vidas insignificantes?").lower()
            if escolha == 'sim':
                os.system('cls')
                digitar_lento("Olha, concordamos em algo então, ainda bem.")
                break
            elif escolha == 'não':
                os.system('cls')
                digitar_lento("Você é um poço de desespero, hein? *risos*")
            break 

        elif escolha == 'não':
            os.system('cls')
            digitar_lento("O que teria depois desse fim? Um novo mundo? Uma nova história? Quem sabe um... Novo amor? *risos*")
            break  
        else:
            digitar_lento("Não quer responder a minha pergunta? Vamos, o que tem a perder?")
            os.system('cls')

    # Continuação da narrativa após o loop
    os.system('cls')
    digitar_lento("*risos*... Você, não tem ideia do que uma simples chuva pode causar em nós...")
    input_lento("...")
    os.system('cls')
    digitar_lento("Efeito borboleta... Curioso não?")

def jogar():
    intro()

if __name__ == "__main__":
    jogar()