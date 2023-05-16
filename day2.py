import matematik 


faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

#bir stringi int olarak dönüştürüyoruz.
print(int(vade) + 12)
#print(int(krediAdi)) hatalıdır çünkü str içerisinde harf temelli olursa dönüşmez.
faiz = str(faiz)
print(type(faiz))



# string interpolation
# seçtiğiniz vade sonucu çıkan vade:
print("Seçtiginiz vade sonucu ortaya çikan vade: " + str(vade))
print("Seçtiginiz vade sonucu ortaya çikan vade: {vadeSayisi}".format(vadeSayisi=vade))
print ( f"Seçtiginiz vade sonucu ortaya çikan vade: {vade}")

isim = "Doga"
metin = "Merhaba{name}".format(name= "Doga" )
print(metin)


# f- string 
metin = f"Hosgeldiniz { 1 + 1 }"
print(metin)




#listeler
#döngüler
#fonksiyonlar

dizi = ["İhtiyaç Kredisi" , 10, 5.2]
print(dizi)

krediler = ["İhtiyaç Kredisi", "Tasit Kredisi", "Konut Kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler))  #length


krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("Taşit Kredisi")
print(krediler)


krediler.remove("Taşit Kredisi")
print(krediler)

krediler.extend(["Y Kredisi" , " Z Kredisi"])
print(krediler)

#for 
# i=0 i<10
x=10
for i in range(10): 
    print("xx")
    print(i)
print("*************")

for i in range(5,11):
     print(i)

print("*************")
for i in range(0,51,10):
     print(i)
print("*************")
#for i in rande(0,1,5):
#print(i)
krediler = ["İhtiyaç Kredisi" , "Taşit Kredisi" , "Konut Kredisi"]
for kredi in krediler: 
     print(kredi)
print ("*********")
for i in range(len(krediler)): 
     print(krediler[i])



#sonsuz döngü 
i = 0 
while i < 10: 
     print("x")
     i +=1
# i yi 1 arttır demek
print("y")
print("********")

while True:
     print("X")
     break
print("**** Son Döngü ***")

krediler = ["İhtiyaç Kredisi" , "Taşit Kredisi" , "Konut Kredisi"]
i = 0 


while i < len(krediler):
 print(i)
 print(krediler[i])
 i+=1
 if krediler[i] == "Konut Kredisi":
  break

#fonksiyonarlar

fiyat = 100
indirim = 20 
 #definition define
def calculate(): 
     print(100-20)

def calculatesWithParams(fiyat,indirim):
     print(fiyat-indirim)


def sayHello(name):
     print(f"Mehaba {name}")

     calculate()
     calculatesWithParams(50.10)
     calculatesWithParams(100,30)
     sayHello("Doga")
     sayHello("Reyh")
     sayHello("Bet")


def calculateAndReturn(fiyat,indirim):
     return fiyat-indirim

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat + 10)




















class Human: 
  #built-in #constructor #initialize
  def __init__(self,name): 
    self.name = name
    print("Bir Human instance üretildi")
  def __str__(self) : 
    return f"STR Fonksiyonunda donen deger : {self.name}"
  def talk (self,sentence):
     print(f"{self.name}: {sentence}")
  def walk(self):
     print(f"{self.name} is walking..")
              
# instance => örnekler
human1 = Human("Enes")
human1.talk("Merhaba")
human1.walk()
print(human1)


human2 = Human("Halit")
human2.talk("Selam")
human2.walk()
print(human2)

