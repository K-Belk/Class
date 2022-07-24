
class GuessingGame:

    def __init__(self, answer) -> None:
        self.answer = answer
        self.user_guess = int
        self.correct = False
        self.guess()
        

    def guess(self):
        while self.correct == False:
            try:
                self.user_guess = int(input('What number am I thinking? - '))
            except ValueError:
                print("Please enter a intiger")
                self.guess()
            if self.user_guess > self.answer:
                print('high')
            elif self.user_guess < self.answer:
                print('low')
            elif self.user_guess == self.answer:
                self.correct = self.solved()
                return 'correct'
        
    def solved(self,):
        return True

