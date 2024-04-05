# # GLOBAL (orqali biz funksiyaning tashqarisidagi qiymatni ichkarida foydalana olamiz)
# a = 3
# def change():
#     global a
#     a = 10
# change()
# print(a)

# # NONLOCAL
# a=1
# def change1():
#     a=3
#     def change2():
#         nonlocal a
#         a=5
#         return a
#     print(change2())
# change1()


# # 7
# def InverDigit():
#     num = input("num = ")
#     print(num[::-1])
# InverDigit()

# # 10
# def Swap():
#     A,B = map(int,input().split())
#     A,B=B,A
#     return A,B
# print(Swap())

# # 11
# def Minmax():
#     X,Y = map(int,input().split())
#     if X>Y:
#         X,Y=Y,X
#     elif X<Y:
#         return X,Y
#     else:
#         print("Raqamlar o'zaro teng!!!")
#     return X,Y
# print(Minmax())

# # 16
# def ishora(num):
#     if num>0:
#         print("Musbat")
#     elif num<0:
#         print("Manfiy")
#     else:
#         print("0 ga teng")
# ishora(12.4)
# ishora(-12.9)
# ishora(0)

# # 21
# def SumRange(A,B):
#     sum = 0
#     for i in range(A,B+1):
#         sum+=i
#     return sum
#     if A>B:
#         return 0
# print(SumRange(1,5))
# print(SumRange(5,1))

# # 22
# def Calc(a,b,arif):
#     if arif == '+':
#         return a+b
#     elif arif == '-':
#         return a-b
#     elif arif == '*':
#         return a*b
#     elif arif == '/':
#         return a/b
# print(Calc(12,13,'+'))
# print(Calc(2,6,'-'))
# print(Calc(1223,109,'*'))
# print(Calc(205,5,'/'))

# # 24
# def Even(K):
#     if K%2==0:
#         print("Juft")
#     elif K%2!=0:
#         print("Toq")
# Even(13)
# Even(12)

# # 25
# def IsSquare():
#     K = int(input("K = "))
#     if K>0:
#         a = K**0.5
#         if int(a)**2==K:
#             print("Ha")
#         else:
#             print('Yuq')
# IsSquare()

