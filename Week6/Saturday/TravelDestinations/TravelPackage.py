from Source import Source


class TravelPackage:

    DEST_DICT = None

    def __init__(self, file_type):
        self.user_budget = 0
        self.filtered_destination = []
        self.DEST_DICT = Source(file_type).contents
        self.main()


    def get_user_budget(self):
        try:
            budget = int(input("What is your budget? "))
        except:
            raise Exception("Must pass in an integer")
        if budget <= 0:
            raise Exception("Can't have negative budget")
        else:
            self.user_budget = budget

    def filter_destinations_based_on_budget(self):
        self.filtered_destination = [i for i in self.DEST_DICT if i["Cost"] <= self.user_budget]

    def display_filtered_destinations(self):
        print(self.filtered_destination)

    def get_user_destination(self):
        dest = input("Choose a destination: ")
        if dest in [d["Country"] for d in self.filtered_destination]:
            self.chosen_destination = dest
        else:
            raise Exception("Not a valid choice")

    def print_confirmation_message(self):
        print(f"You are going to {self.chosen_destination}")
    

    def main(self):
        self.get_user_budget()
        self.filter_destinations_based_on_budget()
        self.display_filtered_destinations()
        self.get_user_destination()
        self.print_confirmation_message()


