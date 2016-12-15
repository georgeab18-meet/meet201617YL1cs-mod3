import time
class Student:
    def __init__(self, ht, ag, hi, fl, bdd, bdm, bdy):
        self.hometown = ht
        self.age = ag
        self.height = hi
        self.flavor = fl
        self.birthdate_day = bdd
        self.birthdate_month = bdm
        self.birthdate_year = bdy
    def print_summary(self):
        print("I live in: "+str(self.hometown))
        print("I'm "+str(self.age)+" years old")
        print("My height is: "+str(self.height)+" cm")
        print("My favorite ice cream flavor is: "+str(self.flavor))
        print("I was born on "+str(self.birthdate_day)+"."+str(self.birthdate_month)+"."+str(self.birthdate_year))
    def get_giraffe_gap(self):
        gap = 500-int(self.height)
        return gap
    def get_days_to_birthday(self):
        cur_date = time.localtime()
        if self.birthdate_month < cur_date[1]:
            b_date = time.mktime((cur_date[0],self.birthdate_month,self.birthdate_day,0,0,0,0,0,0))
            
