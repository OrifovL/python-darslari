# def map1(func,ls):
#     for i in ls:
#         print(func(i),end=" ")
# map1(lambda a:a*a,[1,2,3,4])

# val = lambda name : f"Mening ismim {name}"
# print(val("Lochin"))

m1 = lambda name,age : print(f"{name} {2024-age}")
m1("Lochin",19)

m2 = lambda a : print(a**2,a**3)
m2(2)

m3 = lambda a : print("Juft") if a%2==0 else (print("Toq"))
m3(12)

(lambda son2,son3:print(son2) if son2 > son3 else print("teng") if son2==son3 else print(son3))(3,3)

(lambda x,y=2:print(x**y))(2)

(lambda son4:[print(f"{son4} son {i}ga qoldiqsiz bolinadi")for i in range(2,10+1)  if son4%i==0 ] )(70)