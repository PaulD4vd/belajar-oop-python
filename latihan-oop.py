class Hero:
    jumlah_hero = 0

    def __init__(self, name, health, attack_power, defence_power):
        self.nama = name
        self.kesehatan = health
        self.kekuatan = attack_power
        self.armor = defence_power
    
    def serang(self, lawan):
        print(self.nama + " menyerang " + lawan.nama)
        lawan.diserang(self)

    def diserang(self, lawan):
        print(self.nama + " di serang " + lawan.nama)

sniper = Hero('Sniper', 100, 10, 5)
goliath = Hero('goliath', 100, 5, 10)

sniper.serang(goliath)