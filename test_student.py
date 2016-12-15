from student import Student
georgeab = Student('Kfar Kana',15,173,'Pizza')
georger = Student('Reineh',15,154,'Chocolate')
ariel = Student('Mehavia',15,170,'Ferrero')
students = [georgeab,georger,ariel]
for i in students:
    i.print_summary()
    print(str(i.get_giraffe_gap()))
    print('~'*10)
    
