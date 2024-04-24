# 1st EXAMPLE
class User:
    def __init__(self,name,surname,phone,e_mail,login,age):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.e_mail = e_mail
        self.login = login
        self.age = age
    
    def get_full_name(self):
        print(f"Mening ismim {self.name} {self.surname}")

    def get_phone(self):
        print(f"Mening telefon raqamim {self.phone}")

    def get_e_mail(self):
        print(f"Mening e-mail im {self.e_mail}")

    def get_login(self):
        print(f"Mening loginim {self.login}")

    def get_year(self,year):
        j = year - self.age
        print(f"Siz {j} chi yilsiz")

    def get_info(self):
        print(f"Men {self.name} {self.surname} yoshim {self.age} da, e-mail manzilim {self.e_mail}, tel raqamim {self.phone}")

userN1 = User('Lochin','Orifov','+998 95 100 05 56','lochinorifov19@icloud.com','L_879',19)
userN2 = User('Ali','Bekov','+998 33 003 03 80','alibekov21@gmail.com','AB33',23)

userN1.get_full_name()
userN2.get_full_name()

userN1.get_phone()
userN2.get_phone()

userN1.get_e_mail()
userN2.get_e_mail()

userN1.get_login()
userN2.get_login()

userN1.get_year(2024)
userN2.get_year(2030)

userN1.get_info()
userN2.get_info()

print(userN1.__dict__)
print(userN2.__dict__)



# 2nd EXAMPLE
class Student():
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
        self.couse = 1
        self.subjects = []

    def get_info(self):
        print(f"Mening ismim {self.name} yoshim {self.age} va men {self.couse} kursman")

    def set_course(self):
        self.couse += 1

    def add_subjects(self,subject):
        self.subjects.append(subject)

student11 = Student('Lochin','Orifov',19)

student11.set_course()

student11.add_subjects('IT')

print(student11.__dict__)



# 3rd EXAMPLE
class Avto:
    def __init__(self,model,rang,karobka,narh):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narh = narh
        self.km = 0
        
    def get_info(self):
        print(f"Model {self.model}\nRang {self.rang}\nUzatmalar qutisi {self.karobka}\nNarhi {self.narh}\nBosib o'tgan masofasi {self.km}")
    
    def update_info(self,change):
        if change == 'model':
            self.model = input("Modelni o'zgartirishingiz mumkin; ")
        elif change == 'rang':
            self.rang = input("Rangni o'zgartirishingiz mumkin; ")
        elif change == 'narh':
            self.narh = input("Narhni o'zgartirishingiz mumkin; ")
        elif change == 'karobka':
            self.karobka = input("Uzatmalat qutisi turini o'zgartirishingiz mumkin; ")
        elif change == 'km':
            self.km = input("Km ni o'zgartirishingiz mumkin; ")

avto11 = Avto('Lasetti','Black','Avtomat',15000)

avto11.get_info()

avto11.update_info('km')

print(avto11.__dict__)



# 4th EXAMPLE
class Avtosalon:
    def __init__(self,name,adress):
        self.name = name 
        self.adress = adress
        self.cars = ['Lasetti','Cobalt','Damas','Labo','Onix','Tracker','Equinox','Malibu']
    
    def add_cars(self,car):
        self.cars.append(car)
    
    def remove_cars(self,car):
        self.cars.reverse(car)

    
avtosalon11 = Avtosalon('GM',"O'zbekistan")

avtosalon11.add_cars('Tahoe')

print(avtosalon11.__dict__)

