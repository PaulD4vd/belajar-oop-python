#methods

# methods itu seperti fungsi untuk suatu objek

# methods ada 2
# 1. interaksi dengan client ==> misal bergerak dalam game
# 2. interaksi dengan object ==> objek dalam game menyerang NPC

class hero:
    #class variable
    jumlah_hero = 0
    
    def __init__(self, nama, health, power, armor):
        #instance variable
        self.nama = nama
        self.kesehatan = health
        self.kekuatan = power
        self.pertahanan = armor
        
     # bayangkan methods dengan function 
     
    #method tanpa return void function
    def siapa(self):
        print("nama ku adalah " + self.nama)
        
    #methods dengan argumen
    def healthup(self, up):
        self.kesehatan += up
        
    #methods dengan return
    def gethealth(self):
        return self.kesehatan
     
    
sniper = hero("sniper", 100, 90, 10)
tank = hero('balmond', 100, 20,  90)

print(sniper.__dict__)
print(tank.__dict__)
print("\n\n")

sniper.siapa()
sniper.healthup(10) #bertambah

print(sniper.gethealth())