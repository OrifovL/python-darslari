# # Teskarisiga chiqarish
# for i in range(10,0,-1):
#     print(i)



# # Ko'paytmasi 
# a = 1
# for i in range(1,101):
#     a*=i
# print(a)



# # STR
# a = 'Zafar'
# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(a[i])



# # Example
# narx = 10000
# for i in range(10):
#     print(i/10*narx)



# # Example
# a = int(input('a ni kirit\n>>>'))
# b = int(input('b ni kirit\n>>>'))
# javob =0
# for i in range(a,b+1):
#     javob+=i
# print(javob)



# # Silk ichida sikl
# for i in range(10):
#     for j in range(10):
#         print(j)



# # Example                 (end="") yonma yon chiqaradi 1223334444...
# for i in range (1,11):
#     for j in range(1,i+1):
#         print(i,end="")



import math
n = int(input())
S = 0
for i in range(1,n+1):
    S+=(math.sin(i)/2**i)
print(round(S, 2))
