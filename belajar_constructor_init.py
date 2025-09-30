class Hero: # template

    def __init__(self, umur):
        print("hello", umur)


hero1 = Hero(10)

hero2 = Hero(11)

class orang:
    def __init__(self, nama_orang, umur):
        self.nama = nama_orang
        
        if umur < 0: 
            raise ValueError("umur gaboleh negatif")
        else: 
            self.usia = umur



orang1 = orang("David", 20)
orang2 = orang("andhika", 14)


print(orang1.__dict__)
print(orang2.__dict__)
print(orang2.nama)
print(orang2.usia)