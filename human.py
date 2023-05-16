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
