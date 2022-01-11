#class Human:
#    def __init__(self,name,surname,place_of_birth,yeat_of_birth):
#        self.name=name
#        self.surname=surname
#        self.place_of_birth=place_of_birth
#        self.year_of_birth=yeat_of_birth
#    def info(self):
#        print(f"Name:{self.name},{self.surname}")
#    def year(self,years):
#        return years-self.year_of_birth
#p1=Human("Den","Dmitriev","ua =",1997)
#p1.info()
#print(p1.year(2022))
class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Person created")
    def info(self):
        print(f"Name:{self.name},age:{self.age}")
    def hello(self):
        print(f"{self.name} seys hello")
class Student(Human):
    def __init__(self,name,age,crs,mark):
        super().__init__(name,age)
        #Human.__init__(self,name,age)
        self.crs=crs
        self.mark=mark
    def studing(self):
        print(self.crs,self.mark)
    def hello(self):
        print(f"student created {self.name} emy {self.age}")
    def study(self):
        print(f"NameStudent:{self.name}-study")
class Teacher(Human):
    def teach(self):
        print(f"NameTeacher:{self.name}-teach,age-{self.age}")
s1=Student("Oleg","brodyaga",8,"5a")
s1.studing()
