import random

# interface
print("="*100)
print("Rasakan sensasi gamenya")
print("Created by : swipper")
print("="*100)
print("Game started!!!!")

class hero:
    def __init__(self,inputName,inputPower,InputHealth):
        self.name = inputName
        self.power = inputPower
        self.health = InputHealth
    
    def whois(self):
        print("\n****Hi namaku : {}, AP : {}, HP : {}****\n".format(self.name, self.power, self.health))

    def serang(self, lawan):
        print("{} menyerang {}\n".format(self.name,lawan.name))
        lawan.health-=self.power
        if lawan.health <= 0:
            print("{} mati".format(lawan.name))
        else:
            print("sisa HP {} : {}\n".format(lawan.name,lawan.health))

    def regen(self):
        self.health+=10
        print("regen....\nsisa HP {} : {}\n".format(self.name,self.health))

guno = hero("guno",17,200)
thuy = hero("thuy",30,180)

# choose karakter
print("1.guno\n2.thuy")
choose = int(input("pilih karaktermu: \n"))
hero = thuy
lawan = guno
if choose == 1:
    hero = guno
    lawan = thuy
elif choose == 2:
    hero = thuy
    lawan = guno
else:
    print("restart dan masukkan nilai yang benar")
    exit()
hero.whois()

# mekanik game
while True:
    # action
    print("pilih action: \n1.serang\n2.regen\n")
    action = int(input("masukkan kode action : "))
    if action == 1:
        hero.serang(lawan)
    elif action == 2:
        hero.regen()
    else:
        print("restart dan masukkan nilai yang benar")
        exit()

    # random komp
    komp = random.randint(0,1)
    if komp == 0:
        print("lawan melakukan penyerangan\n")
        lawan.serang(hero)
    elif komp == 1:
        print("lawan melakukan regen\n")
        lawan.regen()

    # dead condition
    if hero.health <= 0:
        print("\n******ANDA KALAH******")
        print("="*100)
        print("Game ended")
        print("="*100)
        break
        exit()
    elif lawan.health <= 0:
        print("\n******ANDA KALAH******")
        print("="*100)
        print("Game ended")
        print("="*100)
        break
        exit()