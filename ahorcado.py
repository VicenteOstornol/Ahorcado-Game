import random
from os import system, name
from time import sleep
from unidecode import unidecode

file_path = "./archivos/data.txt"


def clear_screen():
    if name == 'nt':
        return system('cls')
 
    else:
        return system('clear')


def letra_usuario():
    user_letter = input("Ingresa una letra (escribe 'ESC' para salir):\n ").upper()
    return user_letter


def read_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        words = [word.strip().upper() for word in f]
        return words


def guessing_loop(random_word, underscores, letra_usuario, clear_screen):
    health = 6
    while underscores != random_word:
        clear_screen()
        if health == 0:
            print("Te has quedado sin puntos de vida")
            retry = input("Para reintentar: A\nPara salir: B\n").upper()
            if retry == "A":
                clear_screen()
                print('la palabra era: ', random_word)
                sleep(1)
                run()
            elif retry == "B":
                clear_screen()
                print('la palabra era: ', random_word)
                sleep(1)
                clear_screen()
                print("Nos vemos pronto!")
                sleep(1)
                clear_screen()
                exit()
        print(f"Tienes {str(health)} de vida, pierdes 1 de vida por cada intento fallido")
        print(underscores)
        user_letter = letra_usuario()

        if user_letter == "ESC":
            clear_screen()
            print("Juego terminado")
            sleep(1)
            clear_screen()
            exit()

        elif user_letter in random_word:
            for idx, word_letter in enumerate(random_word):
                if user_letter == word_letter:
                    underscores = list(underscores)
                    underscores[idx] = word_letter

        elif user_letter not in random_word:
            health -= 1
        underscores = "".join(i for i in underscores)
    
    return underscores


def run():
    random_word = unidecode(random.choice(read_data(file_path)))
    underscores = "_"*len(random_word)
    underscores = guessing_loop(random_word, underscores, letra_usuario, clear_screen)
    print(underscores)



if __name__ == '__main__':
    run()