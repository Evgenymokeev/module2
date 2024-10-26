from game import Game
from models import Player
from score import ScoreHandler
from settings import MODES

def create_player():
    name = input("Введите ваше имя: ")
    print("Выберите уровень сложности (1 - Normal, 2 - Hard): ")
    mode = MODES[input("Введите 1 или 2: ")]
    return Player(name, mode), mode 

def play_game():
    player, mode = create_player()
    game = Game(player, mode)
    game.play()

def show_scores():
    ScoreHandler().display()

def main():
    while True:
        choice = input("Выберите опцию:\n1. Начать игру\n2. Показать очки\n3. Выйти\nВведите 1, 2 или 3: ")
        if choice == '1':
            play_game()
        elif choice == '2':
            show_scores()
        elif choice == '3':
            print("Выход из игры.")
            break

if __name__ == "__main__":
    main()

