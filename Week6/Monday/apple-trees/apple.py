class Apple:
    def __init__(self, tree_age):
        self.tree_age = tree_age
        self.diameter = 1
        self.increase_size()

    def increase_size(self):
        increase = self.tree_age * .1
        self.diameter *= increase
        return self.diameter
