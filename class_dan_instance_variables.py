class orang: #template

    jumlah = 0 #variable local / class variable

    def __init__(self, x, y, z):
        self.nama = x #instance variable
        
        if y <= 0:
            print("angka gak boleh minus")
        else:
            self.umur = y

        self.asal = z

        orang.jumlah += 1

orang1 = orang("david", 14, "jakarta") 
orang2 = orang("paul", 10, "jogja")

print(orang1.__dict__)
print(orang2.__dict__)
print(orang1.nama, orang1.umur, orang1.asal, sep="\n\n")
print(orang2.nama, orang2.umur, orang2.asal, sep="\n\n")
print(orang.__dict__)
print(orang.jumlah)