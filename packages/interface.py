from .random_number_gen import RandomNum

class UserInterface:
    def __init__(self):
        self.range_min = 0
        self.range_max = 0
        self.random_num = 0
        self.first_guess = 0
        self.heat_range = 0

    def user_input(self):
        print("Input a range to guess")
        try:
            self.range_min = int(input("minimum:"))
        except:
            print("Invalid entry ERROR")
            self.user_input()
        try:
            self.range_max = int(input("maximum:"))
        except:
            print("Invalid entry ERROR")
            self.user_input()

        if self.range_min >= self.range_max:
            print("Incorrect range Error")
            self.user_input()

        self.random_num = RandomNum.generate_random_number(self.range_min, self.range_max)

    def guess(self):

        try:
            self.guess = int(input("Guess a number:"))
        except:
            print("Incorrect range Error")
            self.guess()

        while True:
            if self.guess > self.random_num:
                print("That guess was ", self.heat_levels(self.guess, self.random_num), ", guess lower")
            elif self.guess < self.random_num:
                print("That guess was ", self.heat_levels(self.guess, self.random_num), ", guess higher")
            else:
                print("CORRECT!")
                break
            self.guess = int(input("Guess a number:"))

    def heat_levels(self, guess, goal):
        self.heat_range = abs(guess - goal)

        if self.heat_range <= 2:
            return "fire"
        elif self.heat_range < 5:
            return "hot"
        elif self.heat_range < 10:
            return "warm"
        elif self.heat_range < 20:
            return "cold"
        elif self.heat_range >= 20:
            return "ice"
