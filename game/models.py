import random
from settings import PLAYER_LIVES, ALLOWED_ATTACKS
from exceptions import GameOver, EnemyDown

class Player:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode 
        self.lives = PLAYER_LIVES
        self.score = 0

    def select_attack(self):
        while True:
            attack = input("Выберите атаку (1 - Бумага, 2 - Камень, 3 - Ножницы): ")
            if attack in ALLOWED_ATTACKS:
                return ALLOWED_ATTACKS[attack]
            print("Некорректный ввод. Пожалуйста, введите 1, 2 или 3.")

    def decrease_lives(self):
        self.lives -= 1
        if self.lives <= 0:
            raise GameOver(f"Игрок {self.name} проиграл. Игра окончена.")

    def add_score(self, points):
        self.score += points

class Enemy:
    def __init__(self, level, mode_multiplier):
        self.level = level
        self.lives = level * mode_multiplier

    def select_attack(self):
        return random.choice(list(ALLOWED_ATTACKS.values()))

    def decrease_lives(self):
        self.lives -= 1
        if self.lives <= 0:
            raise EnemyDown("Соперник побежден!")
