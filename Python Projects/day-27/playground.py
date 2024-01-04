number = 0


def add(*num):
    global number
    for n in num:
        number += n
    return number


# print(add(1, 3, 5, 25, 55))


def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    # print(key)
    # print(value)
    # print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")


my_car = Car(make="Honda", model="Accord")
print(my_car.model)