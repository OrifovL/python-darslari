from func import *
def calc(a,b,arif):
    if arif == '+':
        j = add(a,b)
    elif arif == '-':
        j = sub(a,b)
    elif arif == '*':
        j = mult(a,b)
    elif arif == '/':
        j = div(a,b)
    else:
        j = "Bunaqa amal mavjud emas!!!"
    print(j)     