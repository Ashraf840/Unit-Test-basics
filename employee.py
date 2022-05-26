class Employee:
    # SMaple Employee class
    # ** Creating employee entrances & setting the email & full name into the system **

    raise_amnt = 1.05   # class-based global scoped variable/attribute

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first.lower(), self.last.lower())

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amnt)

