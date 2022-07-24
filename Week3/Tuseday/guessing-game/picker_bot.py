import random

class PickerBot:

    def __init__(self) -> None:
        self.guess = 0
        self.last_guess = 0
        self.answer = 0
        self.solved = False
        self.answer = random.randint(1,100)
    
    # def play(self, guess):
    #     while self.solved == False:
    #         if self.guess != self.last_guess:
    #             print(self.check_guess())

    def check_guess(self, guess):
        print(f"correct answer {self.answer}")
        self.guess = guess
        self.last_guess = self.guess
        print(f"guess {guess}")
        if self.guess > self.answer:
            print("high")
            return 'high'
        elif self.guess < self.answer:
            print('low')
            return 'low'
        elif self.guess == self.answer:
            self.solved = True
            print(f"correct")
            return 'correct'


