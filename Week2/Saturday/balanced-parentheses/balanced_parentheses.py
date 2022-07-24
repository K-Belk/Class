class Balance:

    def __init__(self, string):
        self.string =   string
        self.track = []
        self.find()
    
    def find(self):
        for index, char in enumerate(self.string):
            if char == '(':
                self.track.append(index)
            elif char == ')':
                if len(self.track) > 0:
                    self.track.pop()
                else:
                    self.track.append(index)
        self.clean()
            
    def clean(self):
        if len(self.track) > 0:
            for i in range(len(self.track), 0, -1):
                pos = self.track[i-1]
                self.string = self.string[:pos] + self.string[pos+1:]
        return self.string
