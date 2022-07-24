

from classes.frame import Frame


class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.scores = []
        self.current_frame = 0
        self.frames = {}
        

    def main(self):
        self.play_frame()
        self.scoring()
        print(self.scores)
        return self.score

    def play_frame(self):
        self.current_frame += 1
        self.frames[self.current_frame] = Frame()
        frame = self.frames[self.current_frame]
        frame.main()
        if frame.strike == True:
            if self.current_frame == 10:
                frame.main()
                frame.main()
            else:
                return frame.score
        else:
            frame.main()
            if self.current_frame == 10 and frame.spare == True:
                frame.main()
        return frame.score

    def play_tenth_frame(self):
        pass
    
    def scoring(self):
        self.score = 0
        for f in self.frames:
            if self.frames[f].strike == True:
                self.score += self.strike(f)
            elif self.frames[f].spare == True:
                self.score += self.spare(f)
            else:
                self.score += sum(self.frames[f].score)
            if len(self.scores) <= f:
                self.scores.append(self.frames[f].score)
        return self.score

    def strike(self, f):
        if self.current_frame > f:
            self.frames[f].score[1] = sum(self.frames[f+1].score)
        return sum(self.frames[f].score)

    def spare(self,f):
        if self.current_frame > f:
            return sum(self.frames[f].score) + self.frames[f+1].score[0]
        return sum(self.frames[f].score)



