class Hero:

    #class variabel
    jumlah = 0

    def __init__(self, name, health):
        if not isinstance (name, str):
            raise TypeError("harus string")
        if not isinstance (health, int):
            raise TypeError("harus angka")
        
        self.nama = name
        self.kesehatan = health

david = Hero("lina", 100)

print(david.__dict__)