import random

list_of_job = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1}
}

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(list_of_job)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
            else:
                self.satiety += 5
                self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if not self.car.drive():
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return

        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("I bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hurray delicacies!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_house(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def day_indexes(self, day):
        print(f"Today is day {day} of {self.name}'s life")
        print(f"Money: {self.money}\nGladness: {self.gladness}\nSatiety: {self.satiety}")
        print(f"Home:\nFood: {self.home.food}\nMess: {self.home.mess}")
        print(f"Car:\nFuel: {self.car.fuel}\nStrength: {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression")
            return False
        if self.satiety < 0:
            print("Dead")
            return False
        if self.money < -500:
            print("Bankrupt")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False

        if self.home is None:
            print("Settled in a house")
            self.get_home()

        if self.car is None:
            self.get_car()
            print(f"I bought a {self.car.brand}")

        if self.job is None:
            self.get_job()
            print(f"I got a job - {self.job.job}")

        self.day_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            self.eat()
        elif self.gladness < 20:
            self.chill()
        elif self.money < 0:
            self.work()
        elif self.car.strength < 15:
            self.to_repair()

        if dice == 1:
            print("Let's chill")
            self.chill()
        elif dice == 2:
            print("Go to work")
            self.work()
        elif dice == 3:
            print("Clean house")
            self.clean_house()
        elif dice == 4:
            print("Time for treats")
            self.shopping("delicacies")

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}
}

# *******************************************
class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Not enough fuel to drive")
            return False

# *******************************************
class House:
    def __init__(self):
        self.food = 0
        self.mess = 0

# *******************************************
class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

my_human = Human(name="Vlad")
for day in range(1, 8):
    if not my_human.live(day):
        break
