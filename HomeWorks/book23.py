# # 1
# def powerA3(a):
#     A3=a**3
#     return A3
# print(powerA3(3))


# # 2
# def powerA234(a):
#     A2=a**2
#     A3=a**3
#     A4=a**4
#     return A2,A3,A4
# print(powerA234(3))

# # 3
# def mean(a,b):
#     ua=(a+b)/2
#     ug=(a*b)**0.5
#     return ua,ug
# print(mean(10,8))

# # 4
# def Triangle(a):
#     S=((3)**0.5/4)*a**2
#     return S
# print(Triangle(5))

# 5

# 6
def DigitCountSum():
    num = int(input("Num = "))
    count = 0
    sum = 0
    while num > 0:
        a = num % 10
        num//=10
        count+=1
        sum+=a
        return count,sum
print(DigitCountSum())
