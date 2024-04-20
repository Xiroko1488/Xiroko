import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3


    def to_chill(self):
        print("Time to chill")
        self.progress -= 0.1
        self.gladness -= 5

    def to_eat(self):
        print("Time to eat")
        self.progress += 0.3
        self.gladness += 5

    def to_sleep(self):
        print("Time to sleep")
        self.gladness += 3

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out")
            self.alive = False
        elif self.gladness <= 0:
               print('Depression')
               self.alive = False
        elif self.progress > 5:
            print('Passed externally...')
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day" +str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_chill()
            self.end_of_day()
            self.is_alive()


student1 = Student(name="Mark")

for day in range(365):
    if student1.alive == False:
        break
    student1.live(day)




