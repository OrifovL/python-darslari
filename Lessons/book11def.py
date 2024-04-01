# # 1
# def m1():
#     num = int(input())
#     if num > 0:
#         num+=1
#     return num
# print(m1())

# # 2
# def m2():
#     num = int(input())
#     if num>0:
#         num+=1
#     else:
#         num-=2
#     return num
# print(m2())

# # 3
# def m3():
#     num = int(input())
#     if num > 0:
#         num+=1
#     elif num <0:
#         num-=2
#     else:
#         num = 10
#     return num
# print(m3())

# # 4
# def m4():
#     a,b,c = map(int,input().split())
#     if a>0 and b>0 and c>0:
#         javob = 3
#     elif a<0 and b<0 and c<0:
#         javob = 0
#     elif a>0 and b<0 and c<0:
#         javob = 1
#     elif b>0 and a<0 and c<0:
#         javob =1
#     elif c>0 and a<0 and b<0:
#         javob = 2
#     elif a>0 and b>0 and c<0:
#         javob = 2
#     elif b>0 and a>0 and c>0:
#         javob =2
#     elif c>0 and a<0 and b>0:
#         javob = 2
#     return javob
# print(m4())

# # 6
# def m6():
#     a,b=map(int,input().split())
#     if a>b:
#         javob = a
#     elif b>a:
#         javob = b
#     return javob
# print(m6())

# # 7
# def m7():
#     a,b=map(int,input().split())
#     if a>b:
#         j = 2
#     elif a<b:
#         j = 1
#     else:
#         j = "Sonlar teng!"
#     return j
# print(m7())

# # 8
# def m8():
#     a,b=map(int,input().split())
#     if a>b:
#         j = f"{b} {a}"
#     elif a<b:
#         j = f"{a} {b}"
#     else:
#         j = "Sonlar teng!"
#     return j
# print(m8())

# # 9
# def m9():
#     A,B = map(int,input().split())
#     if A>B:
#         A,B = B,A
#     return A,B
# print(m9()) 

# # 10
# def m10():
#     A,B = map(int,input().split())
#     if A==B:
#         A,B = 0,0
#     else:
#         A,B=A+B,A+B
#     return A,B
# print(m10())

# # 11
# def m11():
#     A,B = map(int,input().split())
#     if A==B:
#         A,B = 0,0
#     else:
#         if A>B:
#             A,B = A,A
#         elif B>A:
#             A,B=B,B
#     return A,B
# print(m11())

# # 12
# def m12():
#     A,B,C = map(int,input().split())
#     if A>B and C>B:
#         r = B
#     elif B>A and C>A:
#         r = A
#     elif A>C and B>C:
#         r = C
#     return r
# print(m12())

# # 13
# def m13():
#     A,B,C = map(int,input().split())
#     if A<B<C:
#         r = B
#     elif C<B<A:
#         r = B
#     elif B<A<C:
#         r = A
#     elif C<A<B:
#         r = A
#     elif A<C<B:
#         r=C
#     elif B<C<A:
#         r=C
#     return r
# print(m13())

# # 14
# def m13():
#     A,B,C = map(int,input().split())
#     if A<B<C:
#         r = f"{A} {C}"
#     elif C<B<A:
#         r = f"{C} {A}"
#     elif B<A<C:
#         r = f"{B} {C}"
#     elif C<A<B:
#         r = f"{C} {B}"
#     elif A<C<B:
#         r= f"{A} {B}"
#     elif B<C<A:
#         r = f"{B} {A}"
#     return r
# print(m13())

# 15
