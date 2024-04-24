class Father:

    def __init__(self,name,surname,money):
        self.name = name
        self.surname = surname
        self.money = money

    def info(self):
        print(f"Mening ismim {self.name}")
    
    def skill(self):
        print('Tez yuguradi')

class Child1(Father):
    
    def skill(self):
        print("Ko'p gapiradi")
        super().skill()

father = Father(' ',' ',' ')

father.skill()

child1 = Child1('Ali','Bekov','$30 000')

print(child1.__dict__)

child1.info()

child1.skill()

class Child2(Father):
    
    def skill(self):
        print("Aqilliroq")
        super().skill()

child2 = Child2('Gulchapchap','Shamsiddinova','$10 000')

print(child2.__dict__)

child2.info()

child2.skill()

print('----------------------------------------------------------------------------------------------------')

class Kasb:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        
class Pro(Kasb):
    def __init__(self,name,surname,projects_num):
        super().__init__(name,surname)
        self.projects_num = projects_num

pro = Pro('Lochinbek','Orifov',0)
print(pro.__dict__)

print('----------------------------------------------------------------------------------------------------')

class Human:
    def __init__(self,name,surname,passport,b_year):
        self.name = name
        self.surname = surname
        self.passport = passport
        self.b_year = b_year

    def get_info(self):
        info = f"{self.name} {self.surname}"
        info += f" Passport: {self.passport}, {self.b_year} to'g'ilgan"
        return info
    
    def get_age(self,yil):
        return yil - self.b_year
    
class Student(Human):
    def __init__(self,name,surname,passport,b_year):
        super().__init__(name,surname,passport,b_year)
        self.subjects = ['History','English','Russian']

