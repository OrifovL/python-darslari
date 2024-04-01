# from algo



# # 0061
# import math
# n = int(input())
# S = 0
# for i in range(1,n+1):
#     S+=math.sin(i)/2**i
# print(round(S, 2))



# # 0062
# import math
# n = int(input())
# S = 0
# for i in range(1,n+1,2):
#     S+=math.sin(i**i)/2**i
# for a in range(2,n+1,2):
#     S-=math.sin(a**a)/2**a
# print(round(S, 2))



# # 0063                                   HELP
# import math
# n = int(input())
# S = 0
# for i in range(1,n+1,2):
#     S+=(-1)**(i+1)*(1/math.factorial(i))
# print(round(S))



# # 0064                                  HELP
# n,x = map(int,input().split())
# S = 0
# for i in range(2,n+1,4):
#     S+=1/x**2*i
# for a in range(4,n+1,4):
#     S-=1/x**2*a
# print(round(S, 3))





# from book



# # 1
# k,n = map(int,input().split())
# for i in range(n):
#     print(k,end="")



# # 2
# a,b = map(int,input().split())
# for i in range(a,b+1):
#     print(i)
# print(b+1-a,' ta son bor')



# # 3
# a,b = map(int,input().split())
# for i in range(a+1,b):
#     print(i)
# print(b-1-a,"ta son bor")



# # 4
# narh = 10000
# for i in range(1,11):
#     print(i*narh)



# # 5
# narh = 10000
# for i in range(1,11):
#     print(narh*i/10)



# # 6
# narh = 10000
# for i in range(12,21,2):
#     print(narh*i/10)



# # 7
# a,b = map(int,input().split())
# s = 0
# for i in range(a,b+1):
#     s+=i
# print(s)



# # 8
# a,b = map(int,input().split())
# s = 1
# for i in range(a,b+1):
#     s*=i
# print(s)



# # 9
# a,b = map(int,input().split())
# s = 1
# for i in range(a,b+1):
#     s+=i**2
# print(s)



# # 10
# n = int(input())
# S = 0
# for i in range(1,n+1):
#     S+=1/i
# print(S)



# # 11
# n = int(input())
# S = 0
# for i in range(0,2*n):
#     S+=(n+i)**2
# print(S)



# # 12
# n = 10
# s = 1
# for i in range(n):
#     d = 1.1
#     s *= d
#     d+=0.1
# print(s)



# # 13
# n = int(input())
# s = 0
# p = 0
# for i in range(n+1):
#     d = 1.1
#     s+=d
#     d+=0.2
# for a in range(n+1):
#     c = 1.2
#     p+=c
#     c+=0.2
# print(s-p)





# # 14
# n = int(input())
# s=0
# for i in range(n+1):
#     if i%2==1:
#         s+=i
# print(s)



# # 15
# a = float(input())
# n = int(input())
# s = 1
# for i in range(n):
#     s*=a
# print(s)



# # 16
# n = int(input())
# a = float(input())
# for i in range(1,n+1):
#     print(a**i)



# 17





# from algo



# 0063
n = int(input())
s=0
x=1
for i in range(1,n+1):
    x=(2*i-1)
    for j in range(1,x):
        x*=j
    s+=((-1)**(i-1))/x
print(f"{s:.4f}")



