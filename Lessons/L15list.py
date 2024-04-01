# # list ichida list

# list = [[1,2,3],[4,5,6],[7,8,9]]
# print(list[0][0],list[0][1],list[0][2],list[1][0],list[1][1],list[1][2],list[2][0],list[2][1],list[2][2])

# list = [[1,2,[3,4,[5,6]]],23]
# print(list[0][2][0])
# print(list[0][2][2][0])

# l = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# for i in l:
#     for a in i:
#         print(a)





# # TUPLE 

# dustlar = ('Ali','Ahmad','Zafar')
# dustlar = list(dustlar)
# dustlar.remove('Zafar')
# # del dustlar[2]
# print(dustlar)
# dustlar = tuple(dustlar)
# print(dustlar)




# nums = []
# for i in range(11,101,2):
#     i=i**3
#     nums.append(i)
# print(nums)



kinolar = []
for i in range(5):
    kinolar.append(input(f"Sevimli kinoyingiz {i+1}-"))
print(kinolar)



sikl = int(input("Bugun nechta odam bilan uchrashdingiz?\n>>>"))
names = []
for i in range(sikl):
    name = input(f"{i+1}-suhbat qilgan odamingiz kim?\n>>>")
    names.append(name)
print(names)



