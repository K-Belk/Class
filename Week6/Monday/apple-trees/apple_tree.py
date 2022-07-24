from apple import Apple

class AppleTree:
    def __init__(self):
        self.age = 0
        self.height = 0
        self.harvest = 0

    def age_tree(self):
        self.age += 1
        self.height += 2
        if self.age >= 8:
            self.harvest = self.age * self.height
        return self.age

    def is_dead(self):
        if self.age >= 60:
            return True
        else:
            return False
    
    def any_apples(self):
        if self.is_dead():
            return False
        elif self.age >= 8 and self.harvest != 0:
            return True
        else:
            return False

    def pick_an_apple(self):
        if not self.any_apples():
            raise Exception('No apples on your tree')
        else:
            apple = Apple(self.age)
            self.harvest -= 1
            return apple