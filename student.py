class Student:
    def __init__(self, ht, ag, hi, fl):
        self.hometown = ht
        self.age = ag
        self.height = hi
        self.flavor = fl
    def print_summary(self):
        print("I live in: "+str(self.hometown))
        print("I'm "+str(self.age)+" years old")
        print("My height is: "+str(self.height)+" cm")
        print("My favorite ice cream flavor is: "+str(self.flavor))
    def get_giraffe_gap(self):
        gap = 500-int(self.height)
        return gap
