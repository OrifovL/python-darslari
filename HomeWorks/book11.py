# IF ustida masalalar

# # 1
# a = int(input("Butun sonni kiriting; "))
# if a>0:
#     a+=1
#     print(a)
# else:
#     print(a)

# # 2
# a = int(input("Butun sonni kiriting; "))
# if a>0:
#     a+=1
#     print(a)
# else:
#     a-=2
#     print(a)

# # 3
# a = int(input("Butun sonni kiriting; "))
# if a>0:
#     a+=1
#     print(a)
# if a<0:
#     a-=2
#     print(a)
# if a==0:
#     a=10
#     print(a)

# # 4 
# a = int(input("a ni kiriting; "))
# b = int(input("b ni kiriting; "))
# c = int(input("c ni kiriting; "))
# if a>0 and b>0 and c>0:
#     print("Kiritilgan sonlarning hammasi musbat")
# if (a>0 and b>0 and c<0) or (a>0 and b<0 and c>0) or (a<0 and b>0 and c>0):
#     print("Bu sonlarning ikkitasi musbat")
# if (a>0 and b<0 and c<0) or (b>0 and a<0 and c<0) or (c>0 and a<0 and b<0):
#     print("Bu sonlarning faqat bittasi musbat")        

# # 5
# a = int(input("a ni kiriting; "))
# b = int(input("b ni kiriting; "))
# c = int(input("c ni kiriting; "))
# if a>0 and b>0 and c>0:
#     print("Kiritilgan sonlarning hammasi musbat")
# elif a<0 and b<0 and c<0:
#     print("Bu sonlarning hammasi manfiy")        
# if (a>0 and b>0 and c<0) or (a>0 and b<0 and c>0) or (a<0 and b>0 and c>0):
#     print("Bu sonlarning ikkitasi musbat va bittasi manfiy")
# if (a>0 and b<0 and c<0) or (b>0 and a<0 and c<0) or (c>0 and a<0 and b<0):
#     print("Bu sonlarning faqat bittasi musbat va ikkitasi manfiy") 

# # 6
# a = int(input("Birinchi sonni kiriting; \n>>>"))
# b = int(input("Ikkinchi sonni kiriting; \n>>>"))
# if a>b:
#     print("a>b a katta", a)
# if a<b:
#     print("a<b b katta", b)

# 7                


# # 8
# a = int(input("Birinchi sobbi kiriting;\n>>>"))
# b = int(input("Ikkinchi sonni kiriting;\n>>>"))
# if a>b:
#     print(f"kattasi {a}")
#     print(f"kichigi {b}")
# if a<b:
#     print(f"kattasi {b}")
#     print(f"kichigi {a}")

# # 9                                                          
# A = int(input("A ni kiriting;\n>>>"))
# B = int(input("B ni kiriting:\n>>>"))
# if A<B:
#     print(f"A={A}\nB={B} ")
# if A>B:
#     print(f"A={B}\nB={A}")

# # 10                                                           
# A = int(input("A ni kiriting;\n>>>"))
# B = int(input("B ni kiriting:\n>>>"))
# if A!=B:
#     yig = A+B
#     A = yig
#     B = yig
#     print(f"A={A}\nB={B}")
# else:
#     A = 0
#     B = 0
#     print(f"A={A}\nB={B}")

# # 11
# A = int(input("A ni kiriting;\n>>>"))
# B = int(input("B ni kiriting:\n>>>"))
# if A!=B and A>B:
#     print(f"A={A}\nB={A}")
# elif A!=B and A<B:
#     print(f"A={B}\nB={B}")
# else:
#     A=B=0
#     print(f"A={A}\nB={B}") 

# # 12
# a = int(input("a ni kiriting\n>>>"))
# b = int(input("b ni kiriting\n>>>"))
# c = int(input("c ni kiriting\n>>>"))
# if a<b<c or a<c<b:
#     print(f"Bu sonlar orasida eng kichigi {a} ga teng")
# if b<a<c or b<c<a:
#     print(f"Bu sonlar orasida eng kichigi {c} ga teng")
# if c<a<b or c<b<a:
#     print(f"Bu sonlar orasida eng kichigi {c} ga teng") 

# # 13
# a = int(input("a ni kiriting\n>>>"))
# b = int(input("b ni kiriting\n>>>"))
# c = int(input("c ni kiriting\n>>>"))
# if a<b<c or c<b<a:
#     print(f"Siz kiritgan raqamlarning o'rtasidagisi {b} ga teng")
# if b<a<c or c<a<b:
#     print(f"Siz kiritgan raqamlarning o'rtasidagisi {a} ga teng")    
# if a<c<b or b<c<a:
#     print(f"Siz kiritgan raqamlarning o'rtasidagisi {c} ga teng")

# # 14
# a = int(input("a ni kiriting\n>>>"))
# b = int(input("b ni kiriting\n>>>"))
# c = int(input("c ni kiriting\n>>>"))
# if a<b<c:
#     print("\n",a,"\n",b,"\n",c)
# if a<c<b:
#     print("\n",a,"\n",c,"\n",b)    
# if b<a<c:
#     print("\n",b,"\n",a,"\n",c) 
# if b<c<a:
#     print("\n",b,"\n",c,"\n",a)    
# if c<a<b:
#     print("\n",c,"\n",a,"\n",b)
# if c<b<a:
#     print("\n",c,"\n",b,"\n",a)           

# # 15
# a = int(input("a ni kiriting\n>>>"))
# b = int(input("b ni kiriting\n>>>"))
# c = int(input("c ni kiriting\n>>>"))
# if a>b>c or b>a>c:
#     print(f"a={a}\nb={b}")
# if a>c>b or c>a>b:
#     print(f"a={a}\nb={b}") 
# if b>c>a or c>b>a:
#     print(f"b={b}\nc={c}")      

# # 16
# A = int(input("A ni kiriting\n>>>"))
# B = int(input("B ni kiriting\n>>>"))
# C = int(input("C ni kiriting\n>>>"))    
# if A<B<C:
#     print(f"A={A*2}\nB={B*2}\nC={C*2}")
# else:
#     print(f"A={A*-1}\nB={B*-1}\nC={C*-1}")

# # 17
# A = int(input("A ni kiriting\n>>>"))
# B = int(input("B ni kiriting\n>>>"))
# C = int(input("C ni kiriting\n>>>"))
# if A<B<C or A>B>C:
#     print(f"A={A*2}\nB={B*2}\nC={C*2}")
# else:
#     print(f"A={A*-1}\nB={B*-1}\nC={C*-1}")   

# # 18                                                                        (help)
# a = int(input("1-sonni kiriting;\n>>>"))
# b = int(input("2-sonni kiriting;\n>>>"))
# b = int(input("3-sonni kiriting;\n>>>"))

# 19

# # 20
# A = int(input("A ni kiriting\n>>>"))
# B = int(input("B ni kiriting\n>>>"))
# C = int(input("C ni kiriting\n>>>"))
# if A<B<C:
#     or_m = B-A
#     print(f"A ga eng yaqin nuqta B nuqta va orasidagi masofa {or_m} ga teng")
# if A<C<B:
#     or_m = C-A
#     print(f"A ga eng yaqin nuqta C nuqta va orasidagi masofa {or_m} ga teng") 
# if B<A<C:
#     or_m = C-A
#     print(f"A ga eng yaqin nuqta C nuqta va orasidagi masofa {or_m} ga teng")   
# if C<A<B:
#     or_m = B-A
#     print(f"A ga eng yaqin nuqta B nuqta va orasidagi masofa {or_m} ga teng") 
# if B<C<A:
#     or_m = A-C
#     print(f"A ga eng yaqin nuqta C nuqta va orasidagi masofa {or_m} ga teng")

# if C<B<A:
#     or_m = A-B
#     print(f"A ga eng yaqin nuqta B nuqta va orasidagi masofa {or_m} ga teng")  

# # 21                                                            (help)
# x1 = int(input("x1 ni kiriting\n>>>"))
# y1 = int(input("y1 ni kiriting\n>>>"))   
# if x1==0 and y1==0:
#     print(0)
# if x1==0 or y1==0:
#     print(1,2)
# if x1!=0 or y1!=0:
#     print(3)
         
# # 22
# x1 = int(input("X1 ni kiriting\n>>>"))
# y1 = int(input("y1 ni kiriting\n>>>"))
# if x1>0 and y1>0:
#     print("Birinchi chorrakda yotadi")
# if x1>0 and y1<0:
#     print("to'rtinchi chorrakda yotadi") 
# if x1<0 and y1>0:
#     print("Ikkinchi chorrakda yotadi")
# if x1<0 and y1<0:
#     print("Uchinchi chorrakda yotadi")  

# # 28                                                          help
# year = int(input('Yilni kiriting;\n>>>'))
# if year > 0 and year % 4 == 0 or year % 400 == 0:
#     days = 366
# else:
#     days = 365
# print(days)

# # 29
# number = int(input('Son kiriting;\n>>>'))
# if number > 0 and number % 2 == 0:
#     info = 'musbat juft son'
# elif number > 0 and number % 2 == 1:
#     info = 'musbat toq son'
# elif number < 0 and number % 2 ==0:
#     info = 'manfiy juft son'
# elif number < 0 and number % 2 == 1:
#     info = 'manfiy toq son'
# 
# elif number == 0:
#     info = 'son nolga teng'
# print(info)



