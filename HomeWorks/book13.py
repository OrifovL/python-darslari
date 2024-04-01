# # 1
# son = int(input("Sonni kiriting;\n>>>"))
# if son==1:
#     kun = "Dushanba"
# elif son==2:
#     kun = "Seshanba"
# elif son==3:
#     kun = "Chorshanba"
# elif son==4:
#     kun = "Payshanba"
# elif son==5:
#     kun = "Juma"
# elif son==6:
#     kun = "Shanba"
# elif son==7:
#     kun = "Yakshanba"
# else:
#     print("Sonlar 1 dan 7 gacha bo'lishi kerak")
# print("Bugun kun",kun)

# # 2
# K = int(input("1-5 gacha bo'lgan baho kiritilsin;\n>>>"))
# if K==1:
#     hol = "yomon"
# elif K==2:
#     hol = "qoniqarsiz"
# elif K==3:
#     hol = "qoniqarli"
# elif K==4:
#     hol = "yaxshi"
# elif K==5:
#     hol = "a'lo"
# else:
#     print("Sonlar 1-5 gacha bo'lishi kerak!")
# print(f"Sizning olgan bahoyingiz {hol} chunki u {K}")

# # 3
# month = int(input("Oy raqamini kiriting;\n>>>"))
# if 1<=month<=2 or month == 12:
#     season = "qish"
# elif 3<=month<=5:
#     season = "bahor"
# elif 6<=month<=8:
#     season = "yoz"
# elif 9<=month<=11:
#     season = "kuz"
# else:
#     print("Sonlar 1-12 gacha bo'lishi kerak")
# print(f"Hozir {season} fasli")

# # 4
# month = int(input("Oyni tarqib raqamini kiritsaning usha oyda necha kun borligi terminalda chiqariladi;\n>>>"))
# if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
#     days = 31
# elif month==2:
#     days = 29
# elif month==4 or month==6 or month==9 or month==11:
#     days = 30
# else:
#     print("Sonlar 1-12 gacha bo'lishi kerak")
# print(f"Bu oyda {days} kun bor!")

# # 5
# A = float(input("A ni kiriting;\n>>>"))
# amal = input("Amalni kiriting (1 - +, 2 - -, 3 - *, 4 - /,)")
# B = float(input("B ni kiriting;\n>>>"))
# if amal=="1":
#     qiymat = A+B
# elif amal=="2":
#     qiymat = A-B
# elif amal=="3":
#     qiymat = A*B
# elif amal=="4":
#     qiymat = A/B
# else:
#     print("A va B butun son bo'lishi kerak va amalni to'g'ri kiriting!")
# print(f"Javob = {qiymat}")

# # 6
# son = float(input("Son kiriting\n>>>"))
# ulchov = int(input("O'chov birligini kiriting yani kiritgan soningizning o'lchov birligini, ular \n1-dm\n2-km\n3-m\n4-mm\n5-sm\n>>>"))
# if ulchov==1:
#     javob = son/10
# elif ulchov==2:
#     javob = son*1000
# elif ulchov==3:
#     javob = son
# elif ulchov==4:
#     javob = son/1000
# elif ulchov==5:
#     javob = son/100
# else:
#     print("O'lchov birligini yo'ki sonni noto'g'ri kiritdingiz!")
# print(f"Sizning javobingiz = {javob} metrga ga teng!")

# # 7
# miqdor = int(input("Miqdorni kirgizing;\n>>>"))
# ulchov = int(input("O'lchov birligini kirgizing bunda,\n1-milligram\n2-gram\n3-kg\n4-sentner\n5-tonna\n>>>" ))
# if ulchov==1:
#     javob = miqdor/1000000
# elif ulchov==2:
#     javob = miqdor/1000
# elif ulchov==3:
#     javob = miqdor
# elif ulchov==4:
#     javob = miqdor*100
# elif ulchov==5:
#     javob = miqdor*1000
# else:
#     print("Miqdorni yoki o'lchov birligini xato kiritdingiz!" )
# print(f"Sizning javobingiz = {javob} kg ga teng!")

# # 8                                                                                   help
# D = int(input("Day;\n>>>"))
# M = int(input("Month;\n>>>"))
# if D==29 and M==2:
#     print("Kabisiya bo'lmagan yil sanasini kiriting!")
# elif (1<=D<=31 and 1<=M<=12):
#     print(f"Bugun {M}-oyning {D}-kuni")

# # 9
# day = int(input("day;\n>>>"))
# month = int(input("month;\n>>>"))
# if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) and (1<=month<=12):
#     day <= 31
# elif month==2 and (1<=month<=12):
#     day <= 28
# elif month==4 or month==6 or month==9 or month==11 and (1<=month<=12):
#     day <= 30
# else:
#     print("day ni yoki month ni noto'g'ri kiritdingiz!")
# print(f"Bugun {day+1}.{month}")

# # 10
# Y = input("Robot yo'nalishi ular\ns-shimol\nsq-sharq\nj-janub\ng-g'arb\n>>>")
# K = int(input("Komandani kiriting ular\n0-harakatni davom ettir\n1-chapga buril\n2-unga buril\n>>>"))
# if Y.lower()=="s" and K==0:
#     yunalish = "shimol"
#     kamanda = "harakatni davom ettir"
# elif Y.lower()=="s" and K==1:
#     yunalish = "shimol"
#     kamanda = "chapga buril"
# elif Y.lower()=="s" and K==2:
#     yunalish = "shimol"
#     kamanda ="unga burul"
# elif Y.lower()=="sq" and K==0:
#     yunalish = "sharq"
#     kamanda = "harakatni davom ettir"
# elif Y.lower()=="sq" and K==1:
#     yunalish = "sharq"
#     kamanda = "chapga buril"
# elif Y.lower()=="sq" and K==2:
#     yunalish = "sharq"
#     kamanda ="unga burul"
# elif Y.lower()=="j" and K==0:
#     yunalish = "janub"
#     kamanda = "harakatni davom ettir"
# elif Y.lower()=="j" and K==1:
#     yunalish = "janub"
#     kamanda = "chapga buril"
# elif Y.lower()=="j" and K==2:
#     yunalish = "janub"
#     kamanda ="unga burul"
# elif Y.lower()=="g" and K==0:
#     yunalish = "g'arb"
#     kamanda = "harakatni davom ettir"
# elif Y.lower()=="g" and K==1:
#     yunalish = "g'arb"
#     kamanda = "chapga buril"
# elif Y.lower()=="g" and K==2:
#     yunalish = "g'arb"
#     kamanda ="unga burul"
# else:
#     print("Yo'nalish yoki kamandani xato kiritdingiz!")
# print(f"Hozirda robot {yunalish} tomonga va {kamanda}ib ketayabdi")

# 16
# age = int(input("Yoshingizni kiriting;\n>>>"))
# if age==20:
#     suz="Siz yigirma yoshdasiz"
# elif age==21:
#     suz="siz yigirma bir yoshdasiz"
# elif age==22:
#     suz="siz yigirma ikki yoshdasiz"
# elif age==23:
#     suz = "siz yigirma uch yoshdasiz"
# elif age==24:
#     suz="siz yigirma turt yoshdasiz"
#     suz="siz yigirma besh yoshdasiz"
# elif age==25:
#     suz = "siz yigirma besh yoshdasiz"
# elif age==26:
#     suz="siz yigirma olti yoshdasiz"
# elif age==27:
#     suz="siz yigirma yetti yoshdasiz"
# elif age==28:
#     suz = "siz yigirma sakkiz yoshdasiz"
# elif age==29:
#     suz="siz yigirma tuqqiz yoshdasiz"
# elif age==30:
#     suz="siz uttiz yoshdasiz"
# elif age==31:
#     suz = "siz uttiz bir yoshdasiz"
# elif age==32:
#     suz="siz uttiz ikki yoshdasiz"
# elif age==33:
#     suz="siz uttiz uch yoshdasiz"
# elif age==34:
#     suz = "siz uttiz turt yoshdasiz"
# elif age==35:
#     suz="siz uttiz besh yoshdasiz"
# elif age==36:
#     suz="siz uttiz olti yoshdasiz"
# elif age==37:
#     suz = "siz uttiz yetti yoshdasiz"
# elif age==38:
#     suz="siz uttiz sakkiz yoshdasiz"
# elif age==39:
#     suz="siz uttiz tuqqiz yoshdasiz"
# elif age==40:
#     suz = "siz qirq yoshdasiz"
# elif age==41:
#     suz="siz qirq bir yoshdasiz"
# elif age==42:
#     suz="siz qirq ikki yoshdasiz"
# elif age==43:
#     suz = "siz qirq uch yoshdasiz"
# elif age==44:
#     suz = "siz qirq turt yoshdasiz"
# else:
#     print("Bu dastur faqat 20 yoshdan 44 yoshgacha bulgan yoshlarni suz shaklida yoza oladi!")

# print(suz)



# # O'ZGARUVCHILAT
# age = input("Yoshingizni kiriting;\n>>>")
# bir = 'bir'
# ikki = 'ikki'
# uch = 'uch'
# turt = 'turt'
# besh = 'besh'
# olti = 'olti'
# yetti = 'yetti'
# sakkiz = 'sakkiz'
# tuqqiz = 'to\'qqiz'
# un = 'o\'n '
# yigirma = 'yegirma '
# uttiz = 'o\'ttiz '
# qirq = 'qirq '
# ellik = 'ellik '
# oltmish = 'oltmish '
# yetmish = 'yetmish '
# sakson = 'sakson '
# tuqson = 'to\'qson '
# s = ''

# # BIRINCHI IF
# if age[0]=='2':
#     s+=yigirma
# elif age[0]=='3':
#     s+=uttiz
# elif age[0]=='4':
#     s+=qirq
# elif age[0]=='5':
#     s+=ellik
# elif age[0]=='6':
#     s+=oltmish
# elif age[0]=='7':
#     s+=yetmish
# elif age[0]=='8':
#     s+=sakson
# elif age[0]=='9':
#     s+=tuqson

# # IKKINCHI IF
# if age[1]=='1':
#     s+=bir
# elif age[1]=='2':
#     s+=ikki
# elif age[1]=='3':
#     s+=uch
# elif age[1]=='4':
#     s+=turt
# elif age[1]=='5':
#     s+=besh
# elif age[1]=='6':
#     s+=olti
# elif age[1]=='7':
#     s+=yetti
# elif age[1]=='8':
#     s+=sakkiz
# elif age[1]=='9':
#     s+=tuqqiz

# # JAVOB
# print(f"Sizning yoshingiz {s} da!")



# # 17
# misol = input("Misol raqamini kiriting;\n>>>")

# # O'ZGARUVCHILAR
# bir = 'bir'
# ikki = 'ikki'
# uch = 'uch'
# turt = 'turt'
# besh = 'besh'
# olti = 'olti'
# yetti = 'yetti'
# sakkiz = 'sakkiz'
# tuqqiz = 'to\'qqiz'
# un = 'o\'n '
# yigirma = 'yigirma '
# uttiz = 'o\'ttiz '
# qirq = 'qirq '
# s = ''
# # BIRINCHI IF
# if misol[0]=='1':
#     s+=un
# elif misol[0]=='2':
#     s+=yigirma
# elif misol[0]=='3':
#     s+=uttiz
# elif misol[0]=='4':
#     s+=qirq

# # IKKINCHI IF
# if misol[1]=='1':
#     s+=bir
# elif misol[1]=='2':
#     s+=ikki
# elif misol[1]=='3':
#     s+=uch
# elif misol[1]=='4':
#     s+=turt
# elif misol[1]=='5':
#     s+=besh
# elif misol[1]=='6':
#     s+=olti
# elif misol[1]=='7':
#     s+=yetti
# elif misol[1]=='8':
#     s+=sakkiz
# elif misol[1]=='9':
#     s+=tuqqiz

# # JAVOB
# print(f"Misolning raqami {s}!")

# 18
a = input('Son kiriting\n>>>')
bir = 'bir'
ikki = 'ikki'
uch = 'uch'
turt = 'turt'
besh = 'besh'
olti = 'olti'
yetti = 'yetti'
sakkiz = 'sakkiz'
tuqqiz = 'to\'qqiz'
un = 'o\'n  '
yigirma = 'yigirma '
uttiz = 'uttiz '
qirq = 'qirq '
ellik = 'ellik '
oltmish = 'oltmish '
yetmish = 'yetmish '
sakson = 'sakson '
tuqson = 'tuqson '
yuz = 'bir yuz '
ikkiy = 'ikki yuz '
uchy = 'uch yuz '
turty = 'turt yuz '
beshy = 'besh yuz '
oltiy = 'olti yuz '
yettiy = 'yetti yuz '
sakkizy = 'sakkiz yuz '
tuqqizy = 'tuqqiz yuz '
s = ''

if a[0]=='1':
    s+=yuz
elif a[0]=='2':
    s+=ikkiy
elif a[0]=='3':
    s+=uchy
elif a[0]=='4':
    s+=turty
elif a[0]=='5':
    s+=beshy
elif a[0]=='6':
    s+=oltiy
elif a[0]=='7':
    s+=yettiy
elif a[0]=='8':
    s+=sakkizy
elif a[0]=='9':
    s+=tuqqizy

if a[1]=='1':
    s+=un
elif a[1]=='2':
    s+=yigirma
elif a[1]=='3':
    s+=uttiz
elif a[1]=='4':
    s+=qirq
elif a[1]=='5':
    s+=ellik
elif a[1]=='6':
    s+=oltmish
elif a[1]=='7':
    s+=yetmish
elif a[1]=='8':
    s+=sakson
elif a[1]=='9':
    s+=tuqson

if a[2]=='1':
    s+=bir
elif a[2]=='2':
    s+=ikki
elif a[2]=='3':
    s+=uch
elif a[2]=='4':
    s+=turt
elif a[2]=='5':
    s+=besh
elif a[2]=='6':
    s+=olti
elif a[2]=='7':
    s+=yetti
elif a[2]=='8':
    s+=sakkiz
elif a[2]=='9':
    s+=tuqqiz

print(s)

