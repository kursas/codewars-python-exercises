# #patikrinti ar ivestas skaicius yra paprastas/naturalus ar ne
# a=int(input("iveskit skaiičių: "))
# k=0
# dalinas=[]
# for i in range(1,a+1):
#     if a%i==0:
#         k+=1
#         dalinas.append(i)
# if k==2:
#     print("skaičius paprastas/naturalus")
#     print(dalinas)
# else:
#     print("skaičius nepaprastas/nenatūralus")
#     print(dalinas)

# #rasti ivesto skaiciaus skaiciu suma
# a=int(input("iveskit skaiciu:"))
# suma_skaic=0
# while a>0:
#     suma_skaic+=a%10
#     a=a//10
# print(suma_skaic)

#duotas skaiciu sarasas,paversti ji kvadratais siu skaiciu
# skaic_saras=[7,8,4,10,5,9]
# tuscias_saras=[]
# for x in skaic_saras:
#     tuscias_saras.append(x**2)
# print(tuscias_saras)
#duotas skaiciu sarasas,paversti ji kvadratais siu skaiciu
#padaryti su imprehensions
# skaic_saras=[7,8,4,10,5,9]
# result=[x**2 for x in skaic_saras]
# print(result)

#ivestai eilutei pasalinti pasikartojancius simbolius ir visus tarpus
# stringas=input("Iveskite sakini:")
# sakinys_new=''
# for x in stringas:
#     if x not in sakinys_new and x!=' ':
#         sakinys_new+=x
# print(sakinys_new)

#ivestam sakinyje,sudarytam is is zodziu ir atskirtu tarpasis,
# reikia paskaiciutis visus zodzius sakinyje
# sakinys=input("iveskite sakini:")
# k=0
# for x in sakinys:
#     if x== " ":
#         k+=1
# print(k+1)

#ivestam sakinyje,sudarytam is is zodziu ir atskirtu tarpasis,
# reikia paskaiciutis visus zodzius sakinyje naudojant split() funkcija
# sakinys=input("iveskite sakini:")
# print(len(sakinys.split()))

#sukurkite skaiciatuva gyvybes laimingu skaiciu.Gyvybes laimingas skaicius
#tai suma visu gimimo datos skaiciu.Pvz. jei jus gimet 15 geguzes 1975,tai jusu
#guvybes skaicius bus lygus:1+5+5+1+9+7+5=33,gauta skaiciu toliau skaldom iki
#vienetu ir sudedam 3+3=6
# gimimo_data=input("iveskit savo gimimo data formatu(DD.MM.MMMM):")
# new_data=gimimo_data.split(".")
# print(new_data)
# day=int(new_data[0])
# month=int(new_data[1])
# year=int(new_data[2])
# sum=0
# while day>0:
#     sum+=day%10
#     day//=10
# while month>0:
#     sum+=month%10
#     month //= 10
# while year>0:
#     sum+=year%10
#     year//=10
# sum1=0
# while sum>0:
#     sum1=sum1+sum % 10
#     sum //= 10
# print(sum1)

#vartotojas turi ivesti 3 skaicius,
# turim atspausdinti is 3 didziausi ir maziausi skaiciu
# pirmas=int(input("iveskite pirma skaiciu:"))
# antras=int(input("iveskite antra skaiciu:"))
# trecias=int(input("iveskite trecia skaiciu:"))
# if pirmas>=antras:
#     if pirmas>=trecias:
#         print(pirmas)
#     else:
#         print(trecias)
# else:
#     if antras>=trecias:
#         print(antras)
#     else:
#         print(trecias)
#
# if pirmas<=antras:
#     if pirmas<=trecias:
#         print(pirmas)
#     else:
#         print(trecias)
# else:
#     if antras<=trecias:
#         print(antras)
#     else:
#         print(trecias)

#sutikrinti ar ivesti metai yra keliamieji ar ne
# metai=int(input("iveskite metus:"))
# if (metai % 4 == 0 and metai % 100 != 0) or metai % 400==0:
#     print(metai,"-keliamieji metai")
# else:
#     print(metai,"-nekeliamieji metai")

#parašyti funkciją square, kuri priima vieną argumentą-
#kvadrato šoną ir gražinanti perimetro ir ploto reikšmes.
# def square(a):
#     perimetras=4*a
#     plotas=a**2
#     return perimetras,plotas
# print(square(10))

#kitas budas,tesiai i printa
# def square(a):
#     print("perimetras,kurio kraštinė",a,"yrra lygus",4*a)
#     print("plotas,kurio kraštinė",a,"yra lygus",a**2)
# square(10)

#kitas budas,tesiai i inputa
# def square(a):
#     print("perimetras,kurio kraštinė",a,"yrra lygus",4*a)
#     print("plotas,kurio skraštinė",a,"yra lygus",a**2)
# a=int(input("iveskite kvadrato kraštinės ilgį:"))
# square(a)

#surasti sandaugą visų lyginių skaičių nuo 1 iki 100
# sandauga=1
# count=0
# for i in range(1,101):
#     if i % 2 == 0:
#         sandauga=sandauga*i
#         count+=1
#         print(f'for ciklo eiles numeris {count},lyginio skaiciaauas sandauga:{sandauga}')

#surasti suma visų lyginių skaičių nuo 1 iki 100
# s=0
# for i in range(1,101):
#     if i%2==0:
#         s=s+i
# print(s)

#surasti vidurki visų lyginių skaičių nuo 1 iki 100
# s=0
# k=0
# for i in range(1,101):
#     if i%2==0:
#         s=s+i
#         k=k+1
# print(s/k)

#surasti max be python funkcijos visų lyginių skaičių nuo 1 iki 100
# max=1
# for i in range(1,101):
#     if i%2==0 and i%3==0:
#         if i>max:
#             max=i
# print(max)

#surasti min be python funkcijos visų lyginių skaičių nuo 1 iki 100
# min=100
# for i in range(1,101):
#     if i%2==0 and i%3==0:
#         if i<min:
#             min=i
# print(min)

#surasti didziausia bendra dalikli(DBD) ivestu  2 skaiciu
# a=int(input("iveskit pirma skaiciu:"))
# b=int(input("iveskit antra skaiciu:"))
#
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
# print(a+b)
