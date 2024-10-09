import random
import time

class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 35
        self.happiness = 55

    def __str__(self):
        return f"Кіт {self.name} | Голод: {self.hunger}, Енергія: {self.energy}, Щастя: {self.happiness}"

    def eat(self):
        if self.hunger > 0:
            print(f"{self.name} їсть...")
            self.hunger += 15
            self.energy += 5
            self.happiness += 5
        else:
            print(f"{self.name} не голодний.")

    def sleep(self):
        print(f"{self.name} спить...")
        self.energy += 17
        self.happiness -= 15
        time.sleep(1)

    def purr(self):
        print(f"{self.name} муркоче... Муррр!")
        self.happiness += 5
        self.energy -= 5

    def play(self):
        if self.energy > 20:
            print(f"{self.name} грається...")
            self.happiness += 5
            self.energy -= 14
        else:
            print(f"{self.name} занадто втомлений, щоб гратися.")

    def simulate(self):
        actions = [self.eat, self.sleep, self.purr, self.play]
        while self.happiness > 0 and self.energy > 0:
            print(self)
            action = random.choice(actions)
            action()
            time.sleep(2)

        print(f"{self.name} занадто втомився або нещасливий... Симуляція завершена.")

# Використання
my_cat = Cat("Барсик")
my_cat.simulate()
