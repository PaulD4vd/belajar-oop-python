class hero: #template
    
    #class varible / local varible / static variable
    jumlah_orang = 0
    
    def __init__(self, nama, asal, domisili, umur):
        # instance variable
        self.nama = nama
        self.lahir = asal
        self.domisili = domisili
        if not isinstance(umur, int):
            raise ValueError("Error bukan angka")
        self.usia = umur
        
        #cara akses class varibale
        hero.jumlah_orang += 1
        
    

orang1 = hero("Paul", "jakarta", "jogja", 19) 
print(hero.jumlah_orang)
orang2 = hero("david","jogja","jogja",18) 
print(hero.jumlah_orang)

print(orang1.__dict__)
print(orang2.__dict__)



        