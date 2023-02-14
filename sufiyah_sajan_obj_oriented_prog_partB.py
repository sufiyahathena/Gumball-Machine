#Sufiyah Sajan
#Object_Oriented Programming

# Part B

import random

class Gumball_Machine:
    def __init__(self, amount):
        self.amount = amount
        self.money = 0.00
        self.gumballs = []
        colors = ["red", "green", "blue"]
        for i in range(int(self.amount)):
            self.gumballs.append(random.choice(colors))
        print("Gumball Machine constructed with ", self.amount, " random gumballs")
        print()
    def report(self):
        print("Gumball Machine Report:")
        print("- Gumballs in machine:", int(self.amount))
        print("- Money in machine: $", '%.2f' % float(self.money))
        print()
    def dispense(self, coin):
        self.coin = coin
        if self.amount != 0:
            if float(self.coin) == 0.25:
                print("Accepting 0.25; Dispensing a ", self.gumballs[-1], " gumball")
                del self.gumballs[-1]
                self.amount -= 1
                self.money += 0.25
                print()
            else:
                print("Invalid coin, no gumball will be dispensed")
                print()
        else:
            print("Machine is empty, no gumball will be dispensed")
            print()
    def count_gumballs_by_type(self, gumballtype):
        self.gumballtype = gumballtype
        if self.gumballtype == "red":
            red = self.gumballs.count("red")
            print("There are ", red, " gumballs of type red in the machine")
            print()
        elif self.gumballtype == "green":
            green = self.gumballs.count("green")
            print("There are ", green, " gumballs of type green in the machine")
            print()
        elif self.gumballtype == "blue":
            blue = self.gumballs.count("blue")
            print("There are ", blue, " gumballs of type blue in the machine")
            print()

machine = Gumball_Machine(5)
machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")

machine.dispense(0.10)
machine.dispense(0.50)
machine.dispense(0.01)

machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")

machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)

machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")

machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)

machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")

