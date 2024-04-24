# # 1
# class KvadratP:
#     def __init__(self,a):
#         self.a = a

#     def Peremtr(self):
#         P = 4*self.a
#         return P
    
# kv1 = KvadratP(6)
# print(kv1.Peremtr())

# # 2 
# class KvadratS:
#     def __init__(self,a):
#         self.a = a

#     def Yuzi(self):
#         S = self.a**2
#         return S
# kv2 = KvadratS(7)
# print(kv2.Yuzi())

# # 3
# class Turtburchak:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
    
#     def t_t_yuzi(self):
#         S = self.a * self.b
#         return S
    
#     def t_t_peremetri(self):
#         P = 2*(self.a+self.b)
#         return P
    
# turtburchak1 = Turtburchak(12,7)
# print(turtburchak1.t_t_peremetri())
# print(turtburchak1.t_t_yuzi())

# # 4
# class Aylana:
#     def __init__(self,d):
#         self.d = d
#         self.pi = 3.14

#     def aylana_uzunligi(self):
#         L = self.pi*self.d
#         return L
    
# aylana1 = Aylana(2)
# print(aylana1.aylana_uzunligi())

# # 5
# class Kub:
#     def __init__(self,a):
#         self.a = a

#     def hajm(self):
#         V = self.a ** 3
#         return V
    
#     def yuza(self):
#         S = 6*self.a**2
#         return S
    
# kub1 = Kub(5)
# print(kub1.hajm())
# print(kub1.yuza())

# # 6
# class Paralelepepet:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def hajm(self):
#         V = self.a * self.b * self.c
#         return V
    
#     def yuza(self):
#         S = 2*(self.a * self.b + self.a * self.c + self.b * self.c)
#         return S
    
# paralelepepet1 = Paralelepepet(4,3,2)
# print(paralelepepet1.hajm())
# print(paralelepepet1.yuza())

# # 7
# class Doira:
#     def __init__(self,R):
#         self.R = R
#         self.pi = 3.14

#     def a_uzun(self):
#         L = 2*self.pi*self.R
#         return L
    
#     def a_yuza(self):
#         S = self.pi * self.R ** 2
#         return S
    
# doira2 = Doira(4)
# print(doira2.a_uzun())
# print(doira2.a_yuza())

# # 8
# class U_arifmetik:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def arifmetik(self):
#         j = (self.a + self.b)/2
#         return j
    
# nums = U_arifmetik(34,17)
# print(nums.arifmetik())

# # 9
# class U_geo:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def geo(self):
#         from math import sqrt
#         j = sqrt(self.a*self.b)
#         return j
    
# nums2 = U_geo(2,2)
# print(nums2.geo())

# # 10
# class Nums:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def add(self):
#         j = self.a + self.b
#         return j
    
#     def sub(self):
#         j = self.a * self.b
#         return j
    
#     def kv(self):
#         j1 = self.a**2
#         j2 = self.b **2
#         return j1,j2
    
# nums3 = Nums(5,10)
# print(nums3.add())
# print(nums3.sub())
# print(nums3.kv())

# # 11
# class Nums:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def add(self):
#         j = self.a + self.b
#         return j
    
#     def sub(self):
#         j = self.a * self.b
#         return j
    
#     def modul(self):
#         j1 = abs(self.a)
#         j2 = abs(self.b)
#         return j1,j2
    
# nums4 = Nums(30,10)
# print(nums4.add())
# print(nums4.modul())
# print(nums4.sub())

# # 12
# class Uchburchak:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def gepotenuza(self):
#         from math import sqrt
#         C = sqrt(self.a**2 + self.b**2)
#         return C
    
#     def peremetr(self):
#         P = self.a + self.b + self.gepotenuza()
#         return P
    
# uchb = Uchburchak(3,4)
# print(uchb.gepotenuza())
# print(uchb.peremetr())

# # 13
# class AylabaS:
#     def __init__(self,R1,R2):
#         self.R1 = R1
#         self.R2 = R2
#         self.pi = 3.14
    
#     def S1_S2(self):
#         S1 = self.pi*self.R1**2
#         S2 = self.pi*self.R2**2
#         return S1,S2
    
#     def S3(self):
#         S3 = self.pi*(self.R1-self.R2)
#         return S3
    
# ayl = AylabaS(12,10)
# print(ayl.S1_S2())
# print(ayl.S3())

# # 14
# class AylanaL:
#     def __init__(self,L):
#         self.L = L
#         self.pi = 3.14
    
#     def R(self):
#         R = self.L/2*self.pi
#         return R
    
#     def S(self):
#         S = self.pi * self.R() ** 2
#         return S
    
# ayla = AylanaL(12)
# print(ayla.R())
# print(ayla.S())

# # 15
# class AylanaS:
#     def __init__(self,S):
#         self.S = S
#         self.pi = 3.14

#     def R(self):
#         from math import sqrt
#         R = sqrt(self.S/self.pi)
#         return R
    
#     def D(self):
#         D = 2*self.R()
#         return D
    
# aylan = AylanaS(10)
# print(aylan.R())
# print(aylan.D())

# # 16
# class Oq:
#     def __init__(self,x1,x2):
#         self.x1 = x1
#         self.x2 = x2

#     def or_mas(self):
#         j = abs(self.x2 - self.x1)
#         return j
    
# nums5 = Oq(-17,0)
# print(nums5.or_mas())

# # 17
# class Son_oq:
#     def __init__(self,A,B,C):
#         self.A = A
#         self.B = B
#         self.C = C

#     def AC(self):
#         j = self.C - self.A
#         return j

#     def BC(self):
#         j = self.C - self.B
#         return j

#     def yig(self):
#         j = self.AC() + self.BC()
#         return j
    
# nums6 = Son_oq(12,24,36)
# print(nums6.AC())
# print(nums6.BC())
# print(nums6.yig())

# # 18
# class Son_oq2:
#     def __init__(self,A,B,C):
#         self.A = A
#         self.B = B
#         self.C = C

#     def AC(self):
#         j = self.C - self.A
#         return j

#     def BC(self):
#         j = self.B - self.C
#         return j

#     def sub(self):
#         j = self.AC() * self.BC()
#         return j
    
# nums6 = Son_oq2(12,36,24)
# print(nums6.AC())
# print(nums6.BC())
# print(nums6.sub())

# # 19

# # 20
# class T_O_masofa:
#     def __init__(self,x1,y1,x2,y2):
#         self.x1 = x1
#         self.x2 = x2
#         self.y1 = y1
#         self.y2 = y2

#     def or_mas(self):
#         from math import sqrt
#         j = sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
#         return j

# kords = T_O_masofa(1,0,12,18)
# print(kords.or_mas())
