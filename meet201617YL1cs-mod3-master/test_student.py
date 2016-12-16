from student import Student
georgeab = Student('Kfar Kana',15,173,'Pizza',1,6,2001)
georger = Student('Reineh',15,154,'Chocolate',11,10,2001)
ariel = Student('Mehavia',15,170,'Ferrero',5,10,2001)
students = [georgeab,georger,ariel]
for i in students:
    i.print_summary()
    print(str(i.get_giraffe_gap()))
    print(str(i.get_days_to_birthday()))
    print('~'*10)
    
