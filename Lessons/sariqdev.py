# # 19-mavzu

# # 1
# def age():
#     year=int(input())
#     name=input()
#     now=2024
#     print(f"{name} sizning yoshingiz {now-year} da")
# age()

# # 2
# def num():
#     numb = float(input())
#     numb2=numb**2
#     numb3=numb**3
#     print(f"{numb} ning kvadrati {numb2} ga teng kubi esa {numb3} ga teng")
# num()

# # 3
# def situ():
#     num = int(input())
#     if num%2==0:
#         result="Juft"
#     elif num%2==1:
#         result="Toq"
#     print(result)
# situ()

# # 4
# def big():
#     a,b=map(int,input().split())
#     if a>b:
#         print(a)
#     elif b>a:
#         print(b)
#     else:
#         print('Sonlar teng!')
# big()

# # 5
# def pro():
#     x,y = map(int,input().split())
#     c = x**y
#     print(c)
# pro()

# # 6
# def pro2():
#     x=int(input())
#     y = 2
#     c=x**y
#     print(c)
# pro2()

# # 7
# def qoldiq():
#     num = int(input())
#     for i in range(2,11):
#         if num%i==0:
#             print(f"{num} {i} ga qoldiqsiz bo'linadi")
# qoldiq()



# 20-mavzu

# # 1
# def info(**user):
#     print(user)
# info(name=input("Input your name; "),surname=input('Input your surname; '),age=input("Input your birth year; "),phone=input('Input your phone number; '))

# # 3
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

# # 4
# def aylana():
#     info_aylana={}
#     r = float(input())
#     info_aylana['r']=r
#     d=2*r
#     info_aylana['d']=d
#     pi=3.14
#     l=2*pi*r
#     info_aylana['l']=l
#     S=pi*r**2
#     info_aylana['S']=S
#     print(info_aylana)
# aylana()

# # 5
# def tub_sonlar():
#     for i in range(2,100):
#         for a in range(1,100):
#             if i%a==0:
                

