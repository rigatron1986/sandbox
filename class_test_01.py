class RepeMixin:
    def __init__(self):
        pass

    def __repr__(self):
        s = self.__class__.__name__ + "("
        # print(self.__dict__.items())
        for k, v in self.__dict__.items():
            if not k.startswith("_"):
                s += "{}={}, ".format(k, v)
        s = s.rstrip(", ") + ")"
        return s


class Person(RepeMixin):
    def __init__(self, name, gender, age):
        RepeMixin.__init__(self)
        self.name = name
        self.gender = gender
        self.age = age


p2 = Person("pavith", "male", 23)
print(p2)
print(p2.name)
