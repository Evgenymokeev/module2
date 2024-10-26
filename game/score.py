from settings import SCORE_FILE, MAX_RECORDS_NUMBER

class PlayerRecord:
    def __init__(self, name, mode, score):
        self.name = name
        self.mode = mode
        self.score = score

    def __gt__(self, other):
        return self.score > other.score

    def __eq__(self, other):
        return self.name == other.name and self.mode == other.mode

    def __str__(self):
        return f"{self.name}\t{self.mode}\t{self.score}"


class GameRecord:
    def __init__(self):
        self.records = []

    def add_record(self, player_record):
        for i, record in enumerate(self.records):
            if record == player_record:  
                if player_record.score > record.score:
                    self.records[i] = player_record
                return
        self.records.append(player_record)

    def prepare_records(self):
        self.records.sort(reverse=True)  
        self.records = self.records[:MAX_RECORDS_NUMBER]


class ScoreHandler:
    def __init__(self):
        self.game_record = GameRecord()
        self.file_name = SCORE_FILE
        self.read()

    def read(self):
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    if line.startswith("Name") or not line.strip():
                        continue
                    name, mode, score = line.strip().split('\t')
                    self.game_record.add_record(PlayerRecord(name, mode, int(score)))
        except FileNotFoundError:
            pass

    def save(self, player):
        self.game_record.add_record(PlayerRecord(player.name, player.mode, player.score))
        self.game_record.prepare_records()
        with open(self.file_name, 'w') as file:
            file.write("Name\tMode\tScore\n")
            for record in self.game_record.records:
                file.write(str(record) + '\n')

    def display(self):
        print("Лучшие результаты:")
        for record in self.game_record.records:
            print(record)
