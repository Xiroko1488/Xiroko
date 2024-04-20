class Human:
    height = 170


class Student(Human):
    height = 175


class Worker(Human):
    pass


vasya = Student()
liliya = Worker()

print(vasya.height)
print(liliya.height)


