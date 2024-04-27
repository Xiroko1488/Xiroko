import inspect


class Human:
    def __init__(self, age, height, name = "john"):
        self.age = age
        self.name = name
        self.lastname = "Wick"


sig = inspect.signature(Human)
for paramenter in sig.parameters.values():
    print(paramenter.name, paramenter.default)
