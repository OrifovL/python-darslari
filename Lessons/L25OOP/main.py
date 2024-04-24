class Student():
    def __init__(self,name,surname,age,course):
        self.name = name
        self.surname = surname
        self.age = age
        self.course = course

# 
student101 = Student('Lochin','Orifov',19,2)
student102 = Student('Ali','Toirov',20,2)
student103 = Student('Mamarayim','Qutbiddinov',23,4)
student104 = Student(input('Name; '),input('Surname; '),int(input('Age; ')),int(input('Course; ')))

# Alohida alohida chiqarish
print(student101)
print(student102)
print(student103)
print(student103)

print(student101.name)
print(student102.name)
print(student103.name)
print(student104.name)

print(student101.surname)
print(student102.surname)
print(student103.surname)
print(student104.surname)

print(student101.age)
print(student102.age)
print(student103.age)
print(student104.age)

print(student101.course)
print(student102.course)
print(student103.course)
print(student104.course)

# Lug'at shaklida chiqarish
print(student101.__dict__)
print(student102.__dict__)
print(student103.__dict__)
print(student104.__dict__)


class Car():
    def __init__(self,name,color,speed,company,year):
        self.name = name
        self.color = color
        self.speed = speed
        self.company = company
        self.year = year
    
car1 = Car('Lacetti','Black',220,'GM',2024)
car2 = Car('Cobalt',"White",220,'GM',2024)
car3 = Car('i5','Black',380,'BMW',2020)
car4 = Car('G63','White',320,"Mercedes Benz",2024)
car5 = Car('nexia2 LEGENDA','Blue',220,"Daewoo",2012)

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)
print(car4.__dict__)
print(car5.__dict__)

