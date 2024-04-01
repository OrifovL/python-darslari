# # Kiritish, chiqarish va o'zlashtirish operatori 





# # 1
# a = float(input('a ni kiriting\n>>>'))
# P = 4*a
# print(P)



# # 2
# a = float(input('a ni kirit\n>>>'))
# S = a**2
# print(S)



# # 3
# a = float(input('a ni kirit\n>>>'))
# b = float(input('b ni kirit\n>>>'))
# S = a*b
# P = 2*(a+b)
# print(f"peremetri={P}\nYuzasi={S}")



# # 4
# d = float(input('d ni kirit\n>>>'))
# pi = 3.14
# L = pi*d
# print(L)



# # 5
# a = float(input('a ni kirit\n>>>'))
# V = a**3
# S = 6*a**2
# print(f"Hajmi={V}\nyuzasi={S}")



# # 6
# a = float(input('a ni kirit\n>>>'))
# b = float(input('b ni kirit\n>>>'))
# c = float(input('c ni kirit\n>>>'))
# V = a*b*c
# S = 2*(a*b+b*c+a*c)
# print(f"Hajmi={V}\nSirti={S}")



# # 7
# R = float(input('R ni kirit\n>>>'))
# pi = 3.14
# L = 2*pi*R
# S = pi*R**2
# print(f"Uzunligi={L}\nYuzasi={S}")



# # 8
# a = float(input('a ni kirit\n>>>'))
# b = float(input('b ni kirit\n>>>'))
# urta_arfmetik = (a+b)/2
# print(urta_arfmetik)



# # 9
# a = float(input('a ni kirit (a>0)\n>>>'))
# b = float(input('b ni kirit (b>0)\n>>>'))
# urta_geo = (a*b)**0.5
# print(urta_geo)



# # 10
# a = float(input('a ni kirit\n>>>'))
# b = float(input('b ni kirit\n>>>'))
# yig = a+b
# kup = a*b
# a2 = a**2
# b2 = b**2
# print(f"Yig'indisi={yig}\nKo'paytmasi={kup}\na ning kvadrati={a2}\nb ning kvadrati={b2}")



# # 11
# a = float(input('a ni kirit\n>>>'))
# b = float(input('b ni kirit\n>>>'))
# yig = a+b
# kup = a*b
# modul_a = abs(a)
# modul_b = abs(b)
# print(f"Yig'indisi={yig}\nKo'paytmasi={kup}\nModul a = {modul_a}\nModul b = {modul_b}")



# # 12
# a = float(input('a ni kirit\n>>>'))
# b = float(input('b ni kirit\n>>>'))
# c = (a**2+b**2)**0.5
# P = a+b+c
# print(f"Gepotinuza={c}\nPeremetr={P}")



# # 13
# print("R1>R2")
# R1 = float(input('R1 ni kirit\n>>>'))
# R2 = float(input('R2 ni kirit\n>>>'))
# pi = 3.14
# S1 = pi*R1
# S2 = pi*R2
# S3 = pi*(R1-R2)
# print(f"S1={S1}\nS2={S2}\nS3={S3}")



# # 14
# L = float(input('L ni kirit\n>>>'))
# pi=3.14
# R = L/2*pi
# S = pi*R**2
# print(f"R={R}\nS={S}")





# # (if-elif-else)  





# # 1
# day = int(input('kunni kiriting son bilan\n>>>'))
# if day == 1:
#     kun = 'Dushunba'
# elif day == 2:
#     kun = "Seshanba"
# elif day == 3:
#     kun = 'Chorshanba'
# elif day == 4:
#     kun = 'Payshanba'
# elif day == 5:
#     kun = "Juma"
# elif day == 6:
#     kun = 'Shanba'
# elif day == 7:
#     kun = 'yakshanba'
# else:
#     kun = '1-7 gacha son kiriting!'
# print(kun)



# # 2
# K = int(input("Son kirit 1-5\n>>>"))
# if K==1:
#     result = 'yomon'
# elif K==2:
#     result = 'qoniqarsiz'
# elif K == 3:
#     result = 'qoniqarli'
# elif K==4:
#     result = 'yaxshi'
# elif K == 5:
#     result = "a'lo"
# else:
#     result = "1-5 gacha bo'lgan baho kiriting"
# print(result)



# # 3
# month = int(input('Oy raqamini kiriting\n>>>'))
# if month==12 or month==1 or month == 2:
#     result = 'qish'
# elif 3<=month<=5:
#     result = 'bahor'
# elif 6<=month<=8:
#     result= 'yoz'
# elif 9<=month<=11:
#     result = 'kuz'
# else:
#     result = '1-12 bulgan son kiriting!'
# print(result)



# 4
# month = int(input('Oy raqamini kiriting\n>>>'))
# if month==1 or month==3 or month==5 or month==7 or month== 8 or month==10 or month==12:
#     result = 31
# elif month == 2:
#     result = 29
# elif month==2 or month==4 or month==6 or month ==9 or month==11:
#     result = 30
# else:
#     result="1-12 gacha son kiriting"
# print(result)



# # 5
# A = float(input('A ni kirit\n>>>'))
# amal = int(input('1-4 gacha 1+, 2-, 3:, 4*'))
# B = float(input('B ni kirit\n>>>'))
# if amal==1:
#     result = A+B
# elif amal==2:
#     result=A-B
# elif amal==3:
#     result=A/B
# elif amal==4:
#     result = A*B
# else:
#     result="Amallar 1-4 gacha"
# print(result)



