from classes.player import Player


class Game:

    def __init__(self) -> None:
        self.players = {}
        self.number_of_players = 0
        self.current_frame = 0

    def add_player(self):
        name = input('Enter player name - ')
        self.number_of_players += 1
        self.players[self.number_of_players] = Player(name)

    def load_players(self):
        amount_of_players = int(input('How many players? - '))
        while self.number_of_players != amount_of_players:
            self.add_player()
        print('players loaded')

    def play(self):
        self.load_players()
        while self.current_frame != 10:
            self.current_frame += 1
            for p in self.players:
                self.players[p].main()
                print(f'{self.players[p].name} has a score of - {self.players[p].score} in frame {self.current_frame}')