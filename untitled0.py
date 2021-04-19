


# kocha = 'mardona'
# tuman = 'qibray'
# shahar = 'toshkent'
# mahalla = 'madaniyat'

# print(shahar, 'shahri',tuman, 'tumani',mahalla, 'mahallasi',kocha, 'ko\'chasi' )


# name = input("ismingizni kiriting:\n".capitalize())
# print("assalomu alaykum ".capitalize() + name.capitalize())

# adress = input("shaharni kiriting: ")
# input("tumanni kiriting: ")
# input("mahallani kiriting: ")
# print("rahmat")

# manzil = f"{kocha} kochasi,{tuman} tumani,{shahar} shahri, {mahalla} mahallasi"
# print(manzil.swapcase())


# son = int(input("Istalgan son kiriting: "))
# kub = son**2
# kv = son**3
# print(f"{son} ning kubi {kub} ga teng\n {son} ning kvadrati {kv} ga teng.")


# yosh = int(input("Tug'ilgan yilingizni kiriting: "))
# hisob = 2020-yosh
# print(f"Siz  {str(hisob)} yoshda ekansiz" )



# a = int(input("Birinchi sonni kiriting: \n "))
# b = int(input("Ikkinchi sonni kiriting: \n"))

# print("a+b=", a+b)
# print("a-b=", a-b)
# print("a/b=", a/b)
# print("a*b=", a*b)



# ismlar = ['anvar','olim','diyor']
# print('Salom'' '  + ismlar[0] + ' '  'mazala mazami?')
# print('qandasan' ' '+ ismlar[2])
# print('jollimi' ' '+ ismlar[1])


# sonlar = [22,65,55,25,36]
# a = sonlar.append(1000)
# c = sonlar.pop(4) 
# b = sonlar.remove(22)
# d = sonlar.insert(2, 888)
# print(sonlar[2] + sonlar[4])
# print('men', sonlar[2], 'raqamini yaxwi koraman')



# z_shaxslar = ['bill gates','pogba','ronaldo','anvar','narzullaev']
# t_shaxslar = ['Muhammad sallalohu alayhi vasallam','Imom al-Buhoriy','amir temur','mirzo_ulug\'bek']

# print("Bizning payg'ambarimiz", t_shaxslar[0].upper(), "hozirham juda obro'li shaxslardan!")
# print("zamaonayiv shaxslardan eng hurmatga sazovarlisi albatta".title(), z_shaxslar[3 ].upper(), ' ', z_shaxslar[4].upper())


# friends = []
# friends.append('zafar')
# friends.append('olim')
# friends.append('anvar')
# friends.append('tohir')
# friends.append('rustam')

# friends.remove('tohir')
# friends.remove('rustam')

# friends.insert(0, 'aziz')
# friends.insert(6,'g\'ulom')
# friends.insert(3, 'lola')

# mehmonlar = []
# mehmonlar.append(friends[5])
# # mehmonlar.append()

# friends.pop(0)

# print(friends)

# print(mehmonlar)


# davlatlar = ['germaniya','aqsh','kongo','russia','korea','kanada']
# davlatlar.sort(reverse=True)
# print(davlatlar)
# # print("davlatlar soni: ", len(davlatlar))
# print(davlatlar)
# print(sorted(davlatlar, reverse=True))

# sonlar = list(range(120,1200,2))
# print(sum(sonlar))
# print(min(sonlar))
# # print(sonlar)
# print(len(sonlar))
# print(sonlar [:20])
# print(sonlar[-20:])
# print(sonlar[530:550])


# taomlar = ['osh','manti','honim','mastava','shashlik','somsa']
# nonushta = taomlar [:]

# nonushta.remove('manti')
# nonushta.remove('mastava')
# nonushta.append('qaymoq')
# nonushta.append('non')
# nonushta[0] = 'sut va qant'
# print(taomlar)
# print(nonushta)
# nonushta=tuple(nonushta)
# nonushta = list(nonushta)


# ismlar = ['olim','jasur','botir','komil','temur']
# for ism in ismlar:
#     print('Salom', ism.title())
# print('kod 5 marta takrorlandi'.title())


# toq_sonlar = list(range(11,100,2))
# print(toq_sonlar)
# for son in toq_sonlar:
#     print(f"{son}ning kubi {son**3} ga teng")


# print('beshta eng sevimli filmingizni kiriting: ')
# kinolar = []
# for n in range(5):
#     kinolar.append(input(f"{n+1}-filmni kiriting: "))
# print(kinolar)

# odam = int(input('Bugun nechta odam bn suhbatlashdingiz: '))
# odamlar = []
# for n in range(odam):
#     odamlar.append(input(f'{n+1}-suhbatashgan odamingiz: '))
# print(odamlar)

# continue lesson 10

# cars = ['toyota', 'mazda','bmw', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car=='bmw':
#       print(car.upper())
#     else:
#        print(car.title())   
       
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car !='kia':
#         print(car.title())
#     else:
#         print(car.upper())


# ism = input('Login kiriting: ')
# if ism.lower() == 'admin':
#     print(f'Xush kelibsiz {ism} foydalanuvchilar ro\'yxatini ko\'rasizmi')
# else:
#     print(f'Xush kelibsiz {ism}')


# a= int(input('birinchi sonni kiriting: '.capitalize()))
# b = int(input('ikkinchi sonni kiriting: '.capitalize()))
# if a>b:
#     print(f'{a} katta {b} dan')
# if a==b:
#     print(f'{a} teng {b}')

# else:
#     print(f'{a} kivhik {b} dan')


# son = int(input("Istalgan son kiriting: "))
# if son == "-":
#     print(f"{son} son manfiy")
# else:
#     print(f"{son} son musbat")
 
# son = int(input("Istalgan musbat son kiriting: "))
# if son>0:
#     print(f" {son} kvadrati {son**2} ga teng")
# else:
#     print("Musbat son kiriting!!!")

# yosh = int(input("Yoshingizni kiriting: "))
# if yosh<=4 or yosh>60:
#     price =0
# elif yosh<18:
#     price=10000
# else:
#     price=20000
# print(f"Kirish {price} so'm")
    
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# if a==b: print(f"Sonlar teng: {a} = {b}")
# elif a<b: print(f"{a} < {b}")
# else:
#     print(f"{a} > {b}")



# mahsulotlar = ['tuz','qaymoq','olma','sabzi','kolbasa','non','sut','go\'sht','guruch']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1} - mahsulotni kiriting: "))
# bor_mahsulotlar = []
# mavjud_emas = []

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#         print("Siz so'ragan mahsulotlar do'konimizda bor")
#     else:
#          mavjud_emas.append(mahsulot)
            
# if mavjud_emas:
#     print("Do'konimizda quydagi mahsulotlar yo'q: ")
#     for mahsulot in mavjud_emas:
#      print(mahsulot)
# else:
#     print("barcha mahsulotlar bor")

# foydalanuvchilar = ['olim','aziz','polat','nur','reks']
# a = input("Yangi login kiriting: ")
# if a in foydalanuvchilar:
#     print("login band bowqa login kiriting")
# else:
#  print("Xush kelibsiz foydalanuvchi")


son = int(input("istalgan butun son kiriting: ".upper()))
for n in range(2,11):
    if not (son%n):
     print(f"{son} ni {n} ga qoldiqsiz bo'linadi")

















































