# # 02 - dars

# print('Assalomu alaykum')

# print(Hayrli tong!)     # Xato

# print(2+4*2)

# print(19/5)

# print(2**4)



# # 03 - dars

# print("Nexia","Tico","Damas","ko'rganlar qilar havas")
# print(5**4)
# print(22%4)

# a = 125
# S = a**2
# P = 4*a
# print(f"Yuzi = {S} Peremetri = {P}")

# d = 12
# R = d/2
# pi = 3.14
# doira_yuzi = pi*R**2
# print(doira_yuzi)

# a = 6
# b = 7
# c = (a**2+b**2)**0.5
# print(c)



# # 04 - dars
# txt = 'Hello world!'
# print(txt)

# xabar = "Assalomu alaykum!"
# print(xabar)
# xabar = "Xayir"
# print(xabar)

# class = "hi"            # xato class ga o'zgaruvchi saqlab bo'lmaydi
# print(class)

# R = 5
# pi = 3.14159
# S = pi*R**2
# print("Radiusi",R,"ga teng aylana yuzi =",S)



# # 05 - dars

# kucha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"

# print(f"{kucha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# kucha = input("Ko'chaniz nomini kiriting\n>>>")
# mahalla = input("Mahallaningiz nomini kiriting|n>>>")
# tuman = input("Tumaningiz nomini kiriting\n>>>")
# viloyat = input("Viloyatingiz nomini kiriting\n>>>")
# print(f"{kucha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# print(f"{kucha} ko'chasi,\n{mahalla} mahallasi,\n{tuman} tumani,\n{viloyat} viloyati")

# manzil = f"{kucha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"

# manzil.title()
# manzil.upper()
# manzil.lower()
# manzil.capitalize()



# # 06 - dars

# num = int(input("Islalgan son kiriting\n>>>"))
# num2 = f"{num} ning kvadrati {num**2} ga teng"
# num3 = f"{num} ning kubi {num**3} ga teng"
# print(num2)
# print(num3)

# age = int(input("Yoshingizni kiriting\n>>>"))
# year = f"Siz {2024-age}-yilda tug'ilgansiz!"
# print(year)

# a = float(input("Birinchi sonni kiriting\n>>>"))
# b = float(input("Ikkinchi sonni kiriting\n>>>"))
# yig = f"{a}+{b}={a+b}"
# ayr = f"{a}-{b}={a-b}"
# kup = f"{a}*{b}={a*b}"
# bul = f"{a}/{b}={a/b}"
# print("",yig,"\n",ayr,"\n",kup,"\n",bul)



# # 07 - dars

# ismlar = ['Shuxrat','Shexroz','Eldor']
# print(f"Salom {ismlar[0]} qandaysan?")
# print(f"{ismlar[1]} bugun nima qilamiz?")
# print(f"haa {ismlar[2]} k*t qandaay")

# nums = [12,5.3,18,-5,-2.6,21,-7,-7.3]

# nums[0]=7
# nums[4]=0
# a=nums[0]+nums[7]
# print(a)
# b=nums[3]-nums[2]
# print(b)
# c=nums[6]/nums[1]
# print(c)
# print(nums)

# t_sh = ["Imom Buxoriy","Ibn Sino","Mirso Ulug'bek","Amir Temur"]
# z_sh = ['Bill Gates','Stiw Jobs','Ilon Mask','Murk Sukerberk']
# a = f"Men tarixiy shaxslardan {t_sh.pop(1)} bilan,\nzamonaviy shaxslardan esa {z_sh.pop(0)} bilan\nsuhbat qilishni istardim"
# print(a)

# friends = []
# friends.append("Shuxrat")
# friends.append('Shexroz')
# friends.append("Eldor")
# friends.append("Ulug'bek")
# friends.append("Elyor")
# print(friends)

# friends.remove("Eldor")
# friends.remove("Ulug'bek")
# print(friends)

# friends.insert(0,"Islom")
# friends.append("Lochin")
# print(friends)

# mehmonlar = []
# mehmonlar.append(friends.pop(0))
# mehmonlar.append(friends.pop(1))
# mehmonlar.append(friends.pop(2))
# print(mehmonlar)



# # 08 - dars

# davlatlar = ["O'zbekiston","Avg'oniston","Qirg'iziston","Tojikiston","Qozog'izson"]

# print(len(davlatlar))

# print(sorted(davlatlar))

# print(davlatlar)

# davlatlar.reverse()
# print(davlatlar)

# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)

nums = []
for i in range(120,1201,2):
    nums.append(i)
# print(nums)

# s = 0
# for i in nums:
#     s+=i
# print(s)

# a = max(nums)
# b= min(nums)
# c = a-b
# print(c)

# print(len(nums))

# print(nums[:20])
# print(nums[int(len(nums)/2-10):int(len(nums)/2+10)])
# print(nums[len(nums)-20:])

# taomlar = ["kabob","somsa","osh","manti","barak","shurva","dimlama","amlet"]

# nonushta = taomlar.copy()

# nonushta.remove("kabob")
# nonushta.remove("osh")
# nonushta.remove("dimlama")
# nonushta.remove("somsa")
# nonushta.append("tuxum")
# nonushta.append("sut")
# print(nonushta)

# print(taomlar)

# nonushta.insert(0,"qaymoq va non")
# print(nonushta)

# nonushta = tuple(nonushta)



# # 09 - dars
    
# names = ["Ali","Vali","Hasan","Husan","Olim"]

# s=0
# for i in names:
#     s+=1
#     print("Salom",i)
# print("Kod",s,"marta takrorlandi")

# nums = []
# for i in range(11,100,2):
#     nums.append(i**3)
# print(nums)

# kino = []
# print("Beshta eng sevimli kinolaringizni kiriting")
# for i in range(5):
#     kino.append(input(f"{i+1}-sini kiriting\n>>>"))
# print(kino)   

# names = []
# count = int(input("Bugun nechta odam bilan suhbat qildingiz\n>>>"))
# for i in range(count):
#     names.append(input(f"{i+1}-suhbat qilgan odaminiz kim edi: "))
# print(names)



# # 10 - dars
    
# cars = ['toyota','mazda','hyundai','gm','kia']
# for i in cars:
#     if i != 'gm':
#         print(i.capitalize())
#     else:
#         print(i.upper())

# login = input("Loginingizni kiriting\n>>>")
# if login != 'Admin':
#     print(f"Xo'sh kelibsiz {login}")
# else:
#     print("Xo'sh kelibsiz,Admin\nFoydalanuvchilar ro'yxatini ko'rasizmi")
    
# a = int(input("Birinchi sonni kiriting\n>>>"))
# b = int(input("ikkinchi sonni kiriting\n>>>"))
# if a==b:
#     print("Bu sonlar teng")

# num = float(input("Istalgan sonni kiriting\n>>>"))
# if num>0:
#     print("Musbat son")
# elif num<0:
#     print("Manfiy son")

# num = float(input("son kiriting\n>>>"))
# if num > 0 :
#     a = num**0.5
#     print(a)
# else:
#     print("Musbat son kiriting!")



# # 11 - dars
# num = int(input('Juft son kiriting: '))
# if num % 2 == 0:
#     print('Rahmat!')
# else:
#     print('Bu juft son emas.')

# age = int(input("Yoshingizni kiriting\n>>>"))
# if age<=4 or age>=60:
#     print("Sizga chipta narxi bepul!")
# elif age <=18:
#     print("Sizga chipta narxi 10 000 so'm")
# elif age > 18:
#     print("Sizga chipta narxi 20 000 so'm")

# num1 = float(input("Birinchi sonni kiriting\n>>>"))
# num2 = float(input("Ikkinchi sonni kiriting\n>>>"))
# if num1<num2:
#     print(num1,'<',num2)
# elif num1==num2:
#     print(num1,'=',num2)
# elif num1>num2:
#     print(num1,'>',num2)

# mahsulotlar = ['non','sut','tuxum','olma','anor','banan','tarvuz','qovun','gusht','shaftoli','limon','tort','pepsi','fanta']
# savat = []
# for i in range(5):
#     savat.append(input(f"{i+1}-mahsulotni qo'shing\n>>>"))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")

# mahsulotlar = ['non','sut','tuxum','olma','anor','banan','tarvuz','qovun','gusht','shaftoli','limon','tort','pepsi','fanta']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
# for i in range(5):
#     savat.append(input(f"{i+1}-mahsulotni qo'shing\n>>>"))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Quyidagi mahsulotlarning hammasi do'konimizda bor")

# foydalanuvchilar = ['lochin','shuxrat','shexroz','eldor','botir']
# login = input("Yangi login tanlang: ")
# if login in foydalanuvchilar:
#     print("Login band, yangi login tanlang!")
# else:
#     print("Xo'sh kelibsiz!")

# num = int(input())
# if num %2 == 0:
#     print(num,"2 ga qoldiqsiz bo'linadi")
# if num%4==0:
#     print(num,"4 ga qoldiqsiz bo'linadi")
# if num%5==0:
#     print(num,"5 ga qoldiqsiz bo'linadi")
# if num%10==0:
#     print(num,"10 ga qoldiqsiz bo'linadi")
# num2 = int(input())
# if num2%2==0:
#     print(num2,"2 ga qoldiqsiz bo'linadi")
# if num2%7==0:
#     print(num2,"7 ga qoldiqsiz bo'linadi")

# 14 - dars
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

# family_foods = {
#     'Otam':'osh',
#     'Onam':'dulma',
#     'singlim':'shashlik',
#     'lochin':'somsa',
#     'ilyos':'pichak'
# }
# for i in family_foods:
#     print(f"{i}ning sevimli ta'omi {family_foods[i]}")

# python = {
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
# a = True
# while a:
#     keyword = input('input the key\n>>>')
#     if keyword == 0:
#         a = False
#     if keyword in python:
#         print(python[keyword])
#     else:
#         print('Bu lugatda bunaqa suz yuq')

# # 15 - dars
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

# dav = {
#     "O'zbekiston":'Toshkent',
#     'Rassiya':'Maskva',
#     'AQSH':'Washington D.C',
#     'Italiya':'Rim',
#     'Tojikiston':'Dushanbe',
#     'Singapur':'Sungapur',
#     'Malayziya':'Kuala-Lampur'
# }
# print('DAVLATLAR')
# for i in sorted(dav.keys()):
#     print(i)
# print('')
# print('POYTAXTLAR')
# for i in sorted(dav.values()):
#     print(i)

# dav = {
#     "O'zbekiston":'Toshkent',
#     'Rassiya':'Maskva',
#     'AQSH':'Washington D.C',
#     'Italiya':'Rim',
#     'Tojikiston':'Dushanbe',
#     'Singapur':'Sungapur',
#     'Malayziya':'Kuala-Lampur'
# }
# poytaxt = input("qaysi davlatning poytaxtini bilishni istaysiz?\n>>>")
# if poytaxt in dav:
#     print(f"{poytaxt} ning poytaxti {dav[poytaxt]}")

# menu = {
#     'osh':26000,
#     'fri':20000,
#     'manti':15000,
#     'grechka':17000,
#     'non':5000,
#     'choy':3000
# }
# buyurtmalat=[]
# print("3 ta taom kiriting!")
# for i in range(3):
#     buyurtmalat.append(input(f"{i+1}-taom: "))
# for buyurtma in buyurtmalat:
#     if buyurtma in menu:
#         f"{buyurtma} {menu[buyurtma]} so'm"
#     else:
#         print(f"KECHIRASIZ BIZDA {buyurtma} YO'Q")

# 16 - dars
famous_humans = {
    'Al Xorazmiy':"Xorazmiy, Abu Jaʼfar (Abu Abdulloh) Muhammad ibn Muso al-Xorazmiy (783, Xiva — 850, Bagʻdod) — xorazmlik matematik, astronom, geograf, fan tarixidagi ilk qomusiy olimlardan. Dastlabki maʼlumotni Xiva shahrida olgan va yetuk olim boʻlib shakllangan. Bunda arab istilosidan soʻng muayyan darajada saqlanib qolgan qadimgi Xorazm fani anʼanalari asosiy rol oʻynagan. Xalifa Horun ar Rashidning oʻgʻli va uning Xurosondagi voliysi al Maʼmun huzuriga — Marvga taklif etilgan. 819-yilda Bagʻdodni egallagan al Maʼmun Markaziy Osiyolik olimlardan Xorazmiy, Ahmad al Fargʻoniy, Habash al Hosib Marvaziy, Abul Abbos Javhariy va boshqalarni oʻzi bilan olib ketib, oʻziga xos ilmiy jamoa tashkil etgan. Bu jamoa fan tarixidagi dastlabki rosmana akademiya deb qaraladigan ilmiy muassasa — „Bayt ul Hikmat“ („Donishmandlik uyi“)ning asosini tashkil etgan. Bu akademiyada Xorazmiy yetakchi olim va ilmiy rahbar boʻlgan. U shu davrdan boshlab Bagʻdodda al Maʼmun (813-833), soʻng al Motasim (833-842), al Vosiq (842-847) xalifaligi davrlarida yashab ijod etgan.",
    "Mirzo Ulug'bek":"Mirzo Ulugʻbek (toʻliq ismi: Sulton Muhammad ibn Shohrux ibn Temur Ulugʻbek Koʻragon; 1394-yil 22-mart, Sultoniya — 1449-yil 27-oktyabr, Samarqand) — Temuriylar davlatining hukmdori, buyuk oʻzbek astronomi (yulduzshunos) va matematigi. U otasi Shohrux Mirzo davrida Mavarounnahr hokimi va otasi vafot etgach butun Temuriylar imperiyasi sultoni (1447—1449) boʻldi.",
    'Ilon Mask':"Mask Janubiy Afrikaning Pretoriya shahrida tug'ilib o'sgan. Bir muncha vaqt Pretoriya universitetida o'qigan, 17 yoshida esa Kanadaga ko'chib o'tgan. Kingstondagi Kvins universitetiga o'qishga kiradi va ikki yildan so'ng Pensilvaniya universitetiga o'tadi, u yerda iqtisodiyot va fizika bo'yicha bakalavr darajasini oladi. 1995-yilda Stanford universitetida o'qish uchun Kaliforniyaga ko'chib o'tdi, ammo buning o'rniga akasi Kimbal (ingl.) rus tili. Internet uchun dasturiy ta'minot ishlab chiqaruvchi Zip2 kompaniyasiga asos solgan. 1999-yilda kompaniya Compaq tomonidan 307 million dollarga sotib olingan. O'sha yili Maks onlayn bankka asos solgan X.com, 2000-yilda konglomerativ ravishda Confinity bilan birlashtirilgan va PayPal-ni tashkil etgan. 2002-yilda kompaniya eBay tomonidan 1,5 milliard dollarga sotib olingan.",
      
}