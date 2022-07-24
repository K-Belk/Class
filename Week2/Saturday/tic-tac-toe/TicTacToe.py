class TicTacToe:    

    def __init__(self):
        self.user1 = input('User 1 name input: ')
        self.user2 = input('User 2 name input: ')  
        self.board = self.load_board()  
        self.counter = 0 
        self.playing_game = True  
        self.turn = 0
        self.player = None
        self.char = None
        self.user_input() 
        
    
    def load_board(self):
        self.board = {
            '1': '1',
            '2': '2',
            '3': '3',
            '4': '4',
            '5': '5',
            '6': '6',
            '7': '7',
            '8': '8',
            '9': '9'
        }
        return self.board

    def whos_turn(self):
        if self.turn % 2 == 0:
            self.player = self.user1
            self.char = 'X'
        else:
            self.player = self.user2
            self.char = 'O'


    def user_input(self):
        print(self.board_location_display())
        while self.playing_game == True:
            self.whos_turn()
            update = [input(f'{self.player} what location of you want: '),self.char]
            self.update_board(update)
            self.check_winner()


    def update_board(self, update):
        if update[0] in self.board:
            if self.board[update[0]] != 'X' and self.board[update[0]] != 'O':
                self.board[update[0]] = update[1]
                self.turn += 1
            else:
                print('Space is taken, Select another space')                
                self.user_input()
        print(self.display_board())
        
    def board_location_display(self):
        return (f'\n|1|2|3|\n|4|5|6|\n|7|8|9|\n')

    def display_board(self):        
        return f'\n|{self.board["1"]}|{self.board["2"]}|{self.board["3"]}|\n|{self.board["4"]}|{self.board["5"]}|{self.board["6"]}|\n|{self.board["7"]}|{self.board["8"]}|{self.board["9"]}|\n'



    def check_winner(self):
        dict_list = list(self.board.values())
        
        for i in range(0,9,3):
            if all(element == dict_list[i] for element in dict_list[i:i+3]):
                print(f'{self.player} is the Winner!')
                self.playing_game = False

        for i in range(3):
            if all(element == dict_list[i] for element in dict_list[i::3]):
                print(f'{self.player} is the Winner!')
                self.playing_game = False

        if all(element == dict_list[0] for element in dict_list[0:9:4]):
                print(f'{self.player} is the Winner!')
                self.playing_game = False

        diagonal_list = dict_list[2:9:2]
        diagonal_list.pop(len(diagonal_list) -1)

        if all(element == diagonal_list[2] for element in diagonal_list):
            print(f'{self.player} is the Winner!')
            self.playing_game = False

    # check for cats game



tic = TicTacToe()

