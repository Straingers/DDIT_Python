class Animal:
    def __init__(self):
        self.fullness = 0
    
    def eat(self):
        self.fullness += 1

    def mantang(self):
        self.fullness = 10
    
class Human(Animal):
    def __init__(self):
        super().__init__()
        self.flag_cook = False
    
    def goHakwon(self):
        self.flag_cook = True
    
hum = Human()
print(hum.fullness)
print(hum.flag_cook)

hum.eat()
print(hum.fullness)
hum.goHakwon()
print(hum.flag_cook)

hum.mantang()
print(hum.fullness)

