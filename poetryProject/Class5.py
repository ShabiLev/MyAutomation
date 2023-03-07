# #Reverse String
# x = 'Hello'
# print(x[::-1]) # olleH

class Shark:
    def __init__(self, name, age: int):
        self.name = name
        self.age = age

    def swim(self):
        print("The shark is swimming")

    def eat(self):
        print("The shark is eating")

def main():
    sammy = Shark(6, 'John')
    sammy.swim()
    sammy.eat()
    print(sammy.age)
    # sammy.name = 'Sammy'
    # sammy.age = 6

main()


class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

class ElectricCar(Car):
    def __init__(self, model, color, battery_type):
        Car.__init__(self,model,color)
        self.battery_type = battery_type

class ElectricCar2(ElectricCar):
    def __init__(self, model, color, battery_type, something):
        ElectricCar.__init__(self, model, color, battery_type)
        self.something = something

def main():
    regular_volvo = Car("volvo", "white")
    electric_volvo = ElectricCar("electronic_volvo", "red", "lithium")

main()