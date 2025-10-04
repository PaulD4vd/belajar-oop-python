class Hero:
    jumlah_hero = 0

    def __init__(self, name, health, attack_power, defence_power):
        self.nama = name
        self.kesehatan = health
        self.kekuatan = attack_power
        self.armor = defence_power
    
    def serang(self, lawan):
        print(self.nama + " menyerang " + lawan.nama) # sniper menyerang goliath
        lawan.diserang(self, self.kekuatan) #lawan di serang sniper | self = sniper

    def diserang(self, lawan, kekuatan_lawan):
        print(self.nama + " di serang " + lawan.nama) # goliat di serang lawan
        damage = max(0, kekuatan_lawan - self.armor)
        print("damage terasa : " + str(damage))
        self.kesehatan -= damage
        print("darah tersisa : " + str(self.kesehatan))
        print("\n")

sniper = Hero('Sniper', 100, 15, 5)
goliath = Hero('goliath', 100, 8, 12)

# battle 
giliran = 0 # sniper = 0, goliath = 1
while sniper.kesehatan > 0 and goliath.kesehatan > 0:
    if giliran == 0:
        sniper.serang(goliath)
        giliran += 1
    else: 
        goliath.serang(sniper)
        giliran -= 1

if sniper.kesehatan <= 0:
    print("goliath menang")
else: 
    print("sniper menang")