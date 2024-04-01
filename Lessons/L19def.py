# def add(*a):
#     print(a)
# add(1,2,3,4,5)


# def add(*a):
#     s=0
#     for i in a:
#         s+=i
#     print(s)
# add(1,2,3,4,5,6,7,8,9,10)


# def juft(*b):
#     s = 0
#     for i in b:
#         if i % 2 == 0:
#             s += i
#     print(s)
# juft(1,2,3,4,5,6,7,8,9,10)


# def users(*a):
#     pass                         # pass funksiyani yaratib kiyinchalik ishlatish uchun


# def users(**a):
#     for i in a:
#         print(f"{a[i]},",end=" ")
# users(name = "Lochin",surname = "Orifov")


# # Programmalarda biz RETURNDAN amallar va shunga uxshash narsalarni bajarish uchun kk PRINT dan farqi bu qiymatni kiyin ishlatsa buladi
# def a():
#     return 5
# def b():
#     return 9

# s = a()+b()
# print(s)


# def info(**user):
#     print(user)
# info(name=input("Input your name; "),surname=input('Input your surname; '),age=input("Input your birth year; "),phone=input('Input your phone number; '))


# def big_num(a=0,b=0,c=0):
#     if a>b and a>c:
#         print(a)
#     elif b>a and b>c:
#         print(b)
#     elif c>a and c>b:
#         print(c)
#     elif a==b==c:
#         print("Bu sonlar o'zaro teng")
# big_num(12,13,14)

def Peremetr(a=0):
    p=4*a
    print(p)
Peremetr(3)

def big(a=0,b=0):
    if a>b:
        print(a)
    elif b>a:
        print(b)
    else:
        print('Bu sonlar uzaro teng!')
big(4,12)

def week(a):
    if a=='1':
        print('Dushanba')
    elif a=='2':
        print('Seshanba')
    elif a=='3':
        print('Chorshanba')
    elif a=='4':
        print('Payshanba')
    elif a=='5':
        print('Juma')
    elif a=='6':
        print('Shanba')
    elif a=='7':
        print('Yakshanba')
    else:
        print("1-7 gacha son kirit!")
week(4)

def PowerA3(*a):
    l=[]
    for i in a:
        l.append(i**3)
    print(l)
PowerA3(5,7,12,-9,12.6)

