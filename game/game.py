from models import Player, Enemy
from settings import MODE_NORMAL, MODE_HARD, HARD_MODE_MULTIPLIER, ATTACK_PAIRS_OUTCOME, WIN, DRAW, LOSE
from exceptions import GameOver, EnemyDown
from score import ScoreHandler

class Game:
    def __init__(self, player, mode):
        self.player = player
        self.mode = mode
        self.mode_multiplier = HARD_MODE_MULTIPLIER if mode == MODE_HARD else 1
        self.enemy = self.create_enemy()

    def create_enemy(self):
        level = self.enemy.level + 1 if hasattr(self, 'enemy') else 1
        return Enemy(level, self.mode_multiplier)

    def play(self):
        while True:
            try:
                result = self.fight()
                self.handle_fight_result(result)
            except GameOver:
                self.save_score()
                print("Игра окончена.")
                break
            except EnemyDown:
                print("Cоперник побежден!")
                self.player.add_score(5)
                self.enemy = self.create_enemy()

    def fight(self):
        player_attack = self.player.select_attack()
        enemy_attack = self.enemy.select_attack()
        return ATTACK_PAIRS_OUTCOME[(player_attack, enemy_attack)]

    def handle_fight_result(self, result):
        if result == WIN:
            self.enemy.decrease_lives()
        elif result == LOSE:
            self.player.decrease_lives()
        elif result == DRAW:
            print("Ничья!")

    def save_score(self):
        ScoreHandler().save(self.player)