import random
from guessing_game import GuessingGame
from picker_bot import PickerBot
from answer_bot import AnswerBot
loop = True
while loop == True:
    game_mode = input("'1' to play '2' to for the cpu to play or 'Q' to quit - " )

    if game_mode == '1':

        game = GuessingGame(random.randint(1,100))

    elif game_mode == '2':

        game = PickerBot()
        answer = AnswerBot()
        count = 1

        while game.solved == False:

            print('-------------------------')
            print(answer.answer_calculation(game.check_guess(answer.answer)))

            print(f'Attempt number {count}')
            count += 1

    elif game_mode == 'Q':
        loop = False
