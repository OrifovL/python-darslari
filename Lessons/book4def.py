# # MASALALAR

# # 1
# print("Birinchi misolning javobi;")
# def m1(a=1):
#     p = 4*a
#     print(p)
# m1()

# # 2
# print("Ikkinchi misolning javobi;")
# def m2(a=1):
#     s = a**2
#     print(s)
# m2()

# # 3
# print("Uchinchi misolning javobi;")
# def m3(a=1,b=2):
#     s = a*b
#     p = 2*(a+b)
#     print(s)
#     print(p)
# m3()

# # 4
# print("To'rtinchi misolning javobi;")
# def m4(d=1):
#     p = 3.14
#     l = p*d
#     print(l)
# m4()

# # 5
# print("Beshinch misolning javobi;")
# def m5(a=1):
#     v = a**3
#     s = 6*(a**2)
#     print(v)
#     print(s)
# m5()

# # 6
# print("Oltinchi misolning javobi;")
# def m6(a=1,b=2,c=2):
#     v = a*b*c
#     s=2*(a*b+b*c+a*c)
#     print(v)
#     print(s)
# m6()

# # 7
# print("Yettinchi masalaning javobi;")
# def m7(r=1):
#     p = 3.14
#     l = 2*p*r
#     s = p*(r**2)
#     print(l)
#     print(s)
# m7()

# # 8
# print("Sakizinchi misolning javobi;")
# def m8(a=1,b=2):
#     ua = (a+b)*0.5
#     print(ua)
# m8()

# # 9 
# print("To'qqizinchi misolning javobi;")
# def m9(a=1,b=2):
#     ug = (a*b)**0.5
#     print(ug)
# m9()

# # 10
# print("O'ninchi misolning javobi;")
# def m10(a=1,b=2):
#     plus = a+b
#     multiply = a*b
#     kv_a = a**2
#     kv_b = b**2
#     print(plus)
#     print(multiply)
#     print(kv_a)
#     print(kv_b)
# m10()

# # 11
# def m11(a=1,b=2):
#     yig = a+b
#     kup = a*b
#     abs_a = abs(a)
#     abs_b = abs(b)
#     print(f"Ularning yig'indisi {yig} ga, kupaytmasi {kup}ga, a ning moduli {abs_a} va b ning moduli {abs_b} ga teng")

# # 12
# def m12(a=3,b=4):
#     c = (a+b)**0.5
#     p = a+b+c
#     print(F"Gepotinuzasi {c} ga va peremetri {p} ga teng")
# m12()

# # 13
# def m13(r1=3,r2=2):
#     P = 3.14
#     s1 = P*r1
#     s2 = P*r2
#     s3 = P*(r1-r2)
#     print(f"Birinchisining yuzi {s1} ga, ikkinchisining yuzi {s2} ga, uchunchisining yuzi {s3} ga teng")
# m13()

# # 14
# def m14(l=2):
#     P = 3.14
#     r = l/(2*P)
#     s = P*r**2
#     print(f"Uning radiusi {r} ga va yuzasi {s} ga teng")
# m14()

# # 15
# def m15(s=10):
#     P = 3.14
#     r = (s/P)**0.5
#     l = 2*P*r
#     d = 2*r
#     print(f"Aylananing deametri {d} ga va radeusi {r} ga teng")
# m15()


# # 16
# def m16():
#     x1 = int(input("Birinchi nuqtani kiriting (bu nuqta ikkinchisidan kichik bo'lishi kerak); "))
#     x2 = int(input("Ikkinchi nuqtani kiriting; "))
#     or_m = x2-x1
#     print(f"Bu nuqtalar orasidagi masofa {or_m} ga teng")
# m16()

# # 17
# def m17():
#     print("A<B<C")
#     A = int(input("Birinchi nuqtani kiriting; "))
#     B = int(input("Ikkinchi nuqtani kiriting; "))
#     C = int(input("Uchunchi nuqtani kiriting; "))
#     AC = C-A
#     BC = C-B
#     uy = AC+BC
#     print(f"AC ning uzunligi {AC} ga, BC ning uzunligi {BC} ga va ular yig'indisi {uy} ga teng")
# m17()

# # 18
# def m18():
#     print("A<C<B")
#     A = int(input("A nuqtani kiriting; "))
#     B = int(input("B nuqtani kiriting; "))
#     C = int(input("C nuqtani kiriting; "))
#     AC = C-A
#     BC = B-C
#     print(f"A va C nuqtalar orasidagi masofqa {AC} ga, C va B nuqtalar orasidagi masofa {BC} ga teng.")
# m18()

# # 20
# def m20():
#     x1,y1=map(int,input().split())
#     x2,y2=map(int,input().split())
#     r = ((x2-x1)**2+(y2-y1)**2)**0.5
#     return r
# print(m20())

# # 21
# def m21():
#     x1,y1=map(int,input().split())
#     x2,y2=map(int,input().split())
#     x3,y3=map(int,input().split())
#     a=((x2-x1)**2+(y2-y1)**2)**0.5
#     b=((x3-x2)**2+(y3-y1)**2)**0.5
#     c=((x3-x1)**2+(y3-y1)**2)**0.5
#     p=(a+b+c)/2
#     S=(p*(p-a)*(p-b)*(p-c))**0.5
#     return S
# print(m21())

# # 22
# def m22():
#     A = 6
#     B = 8
#     A,B = B,A
#     return A,B
# print(m22())

# # 23
# def m23():
#     A = 1
#     B = 2
#     C = 3
#     A,B,C=B,C,A
#     return A,B,C
# print(m23())

# # 25
# def m25():
#     x=int(input())
#     y = 3*x**6-6*x**2-7
#     return y
# print(m25())

# # 26
# def m26():
#     x = int(input())
#     y = 4*(x-3)**6-7*(x-3)**3+2
#     return y
# print(m26())

# # 27
# def m27():
#     A = int(input())
#     A2 = A**2
#     A4 = A**4
#     A8 = A**8
#     return A2,A4,A8
# print(m27())

# # 28
# def m28():
#     A = int(input())
#     a2 = A**2
#     a3 = A**3
#     a5 = A**5
#     a10 = A**10
#     a15 = A**15
#     return a2,a3,a5,a10,a15
# print(m28())

# # 29
# def m29():
#     a = float(input())
#     R = a/57.2958
#     return R
# print(m29())

# # 30
# def m30():
#     R = float(input())
#     a = R*57.2958
#     return a
# print(m30())

# # 31
# def m31():
#     Tf = float(input())
#     Tc = (Tf-32)*5/9
#     return Tc
# print(m31())

# # 33
# def m33():
#     konfet_narxi = 20000
#     kg = float(input())
#     return konfet_narxi,kg
# print(m33())

