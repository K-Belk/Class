from random import randint


class Frame:

    def __init__(self) -> None:
        self.pins_remainding = 10
        self.throw = 0
        self.gutter = False
        self.strike = False
        self.spare = False
        self.score = []

    def main(self):
        start = self.pins_remainding
        pins_down = self.roll()
        self.check_condition(start)
        self.score_frame(pins_down)
        return self.score
        

    def roll(self):
        self.throw += 1
        pins_down = randint(0,self.pins_remainding)
        self.pins_remainding -= pins_down
        return pins_down

    def check_condition(self, start):
        if self.pins_remainding == start:
            self.gutter = True
        elif self.throw == 1 and self.pins_remainding == 0:
            self.strike = True
        elif self.throw == 2 and self.pins_remainding == 0:
            self.spare = True

    def score_frame(self,pins_down):
        if self.strike:
            self.score.append(pins_down)
            self.score.append(0)
        else:
            self.score.append(pins_down)


