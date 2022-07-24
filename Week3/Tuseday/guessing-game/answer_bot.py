import math


class AnswerBot:

    def __init__(self):
        
        self.answer = 50
        self.last_answer = 0
        self.max = 100 
        self.min = 1

    def answer_calculation(self, responce):
        self.last_answer = self.answer
        if responce == 'high':
            self.max = self.last_answer 
        elif responce == 'low':
            self.min = self.last_answer
        elif responce == 'correct':
            return 'Winner'
        self.answer = self.midpoint(self.min, self.max)
        return self.answer

    def midpoint(self, first_num, second_num):
        return math.floor((first_num + second_num)/2)
