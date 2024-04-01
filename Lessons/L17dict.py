# DICT METHODS

user = {
    'name':'Lochin',
    'surname':'Orifov',
    'age':18,
    'password':'q1w2e3r4',
    'user_name':'lochin_orifov'
}

# # .keys()
# print(user.keys())         

# # .values()
# print(user.values())

# # .get() 
# print(user.get('name'))
# print(user.get('surname'))

# # .items()
# print(user.items())

# # .updete()            malumot qushish
# user.update({'user_name':'lochin_orifov'})
# print(user['user_name'])

# # .clear()          faqat dict ni ichini tozalab bera oladi ichidan malum bir qiymatni ololmaydi
# user.clear()
# print(user)

# # .pop()            o'chirib boshqa qiymatga saqlash mn
# a = user.pop('name')
# print(user)
# print(a)

# user.pop('surname')
# user.pop('age')
# print(user)

# # .popitem()             oxiridagi qiymatni o'chirib beradi
# print(user)
# user.popitem()
# print(user)

# # for da dict dan foydalanish
# for i in user:
#     print(i)

# print('1 usul')
# for i in user:
#     print(user[i])

# print('2 usul')
# for i in user.values():
#     print(i)

# pyt = {
#     'print':"Bu so'z orqali biz terminalga biror bir qitmat chiqarishimiz mumkin",
#     'input':"Bu so'z orqali foydalanuvchidan qiymat kiritishini so'rashimiz mumkin",
#     'if_elif_else':"Bu esa shart operatori bu orqali biz dasturda burilishlar qilishimiz mumkin uning ma'nosi agar",
#     'for':"Bu orqali biz sikl hosil qila olamiz",
#     'while':"While orqali ham sikl hosil qilamiz ammo u cheksiz davom etadigan sikl buladi agar True bulsa",
#     'list':"List orqali biz list yaratgan holga unga ma'lumotlarni saqlashimiz mumkin",
#     'tuple':"Tuple bu o'zgarmas list",
#     'dict':"Dictionary bunda biz kalit va qiymat orqali malumot saqlaymiz",
#     'int':"Bu integet yani butun son",
#     'str':"Bu string yani text",
#     'float':"Haqiqiy son"
# }
# for i in sorted(pyt):
#     print(i,'-',pyt[i])

dav = {
    "O'zbekiston":'Toshkent',
    'Rassiya':'Maskva',
    'AQSH':'Washington D.C',
    'Italiya':'Rim',
    'Tojikiston':'Dushanbe',
    'Singapur':'Sungapur',
    'Malayziya':'Kuala-Lampur'
}
print('DAVLATLAR')
for i in sorted(dav.keys()):
    print(i)
print('')
print('POYTAXTLAR')
for i in sorted(dav.values()):
    print(i)

