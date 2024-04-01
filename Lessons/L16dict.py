# # DICT
# Student = {
#     "name":"Lochin",
#     "surname":"Orifov",
#     "age":19,
#     "year":2005
# }

# print(Student["age"])
# print(Student["name"])
# print(Student["surname"])
# print(Student["year"])



# fanlar = {
#     1:"ona tili",
#     2:"rus tili",
#     3:"ingliz tili",
#     4:"matematika"
# }

# print(fanlar[1])
# print(fanlar[2])
# print(fanlar[3])
# print(fanlar[4])



# student = {
#     "name":'Lochin',
#     "surname":'Orifov',
#     "fanlar":['math','eng','rus','programming']
# }
# print(student['fanlar'][0])
# print(student['fanlar'][1])
# print(student['fanlar'][2])
# print(student['fanlar'][3])



# bola = {
#     'otasi':{
#         'ismi':'Ali',
#         'familya':'Karimov'
#     },
#     'onasi':{
#         'ismi':'Zarina',
#         "familya":'karimov'
#     }
# }
# print(bola['otasi']['ismi'])
# print(bola['otasi']['familya'])
# print(bola['onasi']['ismi'])
# print(bola['onasi']['familya'])




# car = {
#     'name':'BMW',
#     'model':'X7',
#     'speed':360
# }
# a = car['name']
# b = car.get('name')           # recommented

# print(a,b)

# print(car.get('model'))
# print(car.get('speed'))



# family = {
#     'otam':{
#         'name':'Qobil',
#         'surname':'Ahatov',
#         'year':1979
#     },
#     'onam':{
#         'name':'Feruza',
#         'surname':'Pirmatova',
#         'year':1985
#     },
#     'men':{
#         'name':'Lochin',
#         'surname':'Orifov',
#         'year':2005
#     }
# }

# print(f"Otamning ismi {family['otam']['name']} familyasi {family['otam']['surname']}")
# print(f"Onamning ismi {family['onam']['name']} familyasi {family['onam']['surname']}")
# print(f"Mening ismim {family['men']['name']} familyam {family['men']['surname']}")

# for i in family:
#     print(f"{i}ning ismi {family[i]['name']} familiyasi {family[i]['surname']}")




# ovqatlar = {
#     'ali':'osh',
#     'vali':'shurva',
#     'shodi':'somsa',
#     'bodi':'shashlik',
#     'eldor':'mastava'
# }

# for i in ovqatlar:
#     print(f"{i}ning sevimli ovqati {ovqatlar[i]}")



python = {
    'print':"Bu so'z orqali biz terminalga biror bir qitmat chiqarishimiz mumkin",
    'input':"Bu so'z orqali foydalanuvchidan qiymat kiritishini so'rashimiz mumkin",
    'if_elif_else':"Bu esa shart operatori bu orqali biz dasturda burilishlar qilishimiz mumkin uning ma'nosi agar",
    'for':"Bu orqali biz sikl hosil qila olamiz",
    'while':"While orqali ham sikl hosil qilamiz ammo u cheksiz davom etadigan sikl buladi agar True bulsa",
    'list':"List orqali biz list yaratgan holga unga ma'lumotlarni saqlashimiz mumkin",
    'tuple':"Tuple bu o'zgarmas list",
    'dict':"Dictionary bunda biz kalit va qiymat orqali malumot saqlaymiz",
    'int':"Bu integet yani butun son",
    'str':"Bu string yani text",
    'float':"Haqiqiy son"
}
a = True
while a:
    keyword = input('input the key\n>>>')
    if keyword == 0:
        a = False
    if keyword in python:
        print(python[keyword])
    else:
        print('Bu lugatda bunaqa suz yuq')



