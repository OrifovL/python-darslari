# # while True bo'lsa ishlaydi
# while True:
#     print('Hello')

# while False:
#     print('Bye')



# # Shart berish orqali
# a = 0
# while a < 5:
#     print('Hi!')
#     a+=1



# # Example with if (break works only with if!!!)
# true_password = "q1w2e3r4"
# while True:
#     password = input('Input the password\n>>>')
#     if password==true_password:
#         print("To'g'ri!")
#         break
#     else:
#         print("Noto'g'ri!")



# # Example 
# true_password='qwer'
# count=0
# while True:
#     if count<3:
#         password=input('input the password\n>>>')
#         if password==true_password:
#             print("Xo'sh kelibsiz!")
#             break
#         else:
#             print("Password xato!")
#     else:
#         print("Juda ko'p urunish 30 soniyaga bloklanda")
#         break
#     count+=1



# # Example
# a = 6
# b = 23
# while a<=b:
#     print(a)
#     a+=1



# # Example
# a = 6
# b = 23
# while a<=b:
#     print(b)
#     b-=1



# # with break or with False  (recomented False)
# a = True
# count=0
# while a:
#     print(count)
#     if count==10:
#         # break
#         a = False
# count+=1



# # continue     (1,2,3,4,(5),6,7,8,9)
# a = 0
# while a<10:
#     a+=1
#     if a==5:
#         continue
#     print(a)



# book19
A = 13
B = 3
count=0
while A>=B:
    A-=B
    count+=1
print(count)



