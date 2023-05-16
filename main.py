print("kkadayolmasin")
baslik = "Taşit Kredisi" 
print(baslik)
#string => metinsel ifade 
baslik = "İhtiyaç Kredisi"
print(baslik)
#int => tam sayı 
vade = 36
ekVade = 6
vade2 = "36"

# float decimal, double 
aylikOdeme = 200.50

# bool , boleen => doğru yada yanlış
yükselisteMi = False

#matematiksel ifadeler 
print(5 + 5)
print(vade + 12)
print(vade+ekVade)
#vade degerini yukarıda 36 verdik 19.satırda 12 arttırdık 36+12 oldu.


print(5-5)
print(vade-12)
print(vade - ekVade)
print(36-6)



# * çarpma işlemi
print(vade * 2)
print(vade * ekVade)
print(10*10)


# / bölme
print(5/5)
print(vade / 2)
print(vade / ekVade)
print(10/2)


yeniVade = vade / 2
fiyat = 100
indirimlifiyat = fiyat - 20 

print(yeniVade)
print(indirimlifiyat)

# mod operator
print(10%2)
print(vade % 5)
print(vade % ekVade)
print(30 % 10)


#mantıksal operatörler
print(1 == 1)
print(1 == 2)
# CTRL K + CTRL C YORUM İÇİN 
print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)


print(1 != 1)
print(1 != 2)


# or and 

#or veya 
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and 5 > 2 and 3 > 2 )

print(2 > 1 or 1 > 2 and 3 > 2)  


#karar yapıları
# if else 
sayi1 = 10 
sayi2 = 15 
#sayi1 sayi2' den büyükse ekrana sayi 1 daha büyük yazdır 
#condition 

#indint 
if  sayi1 < sayi2: 
        print("Sayi 1 Sayi 2'den küçüktür")
elif sayi1 == sayi2: 
        print("iki sayi eşittir")
#eğer if ve else if bloğuna girmez ise 
else: 
         print("Sayi 1 Sayi 2' den büyüktür")


if sayi1 <= sayi2:
       print("Sayi 1 Sayi 2 'den küçüktür") 
if sayi1 == sayi2: 
       print("iki sayi eşittir")
else:   
    print("Sayi 1 Sayi 2 'den büyüktür") 

    print("Burasi if bloğunun dişindadir") 
    