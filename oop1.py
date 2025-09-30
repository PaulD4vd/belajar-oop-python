class hero:
    pass

hero1 = hero()
hero2 = hero()

hero1.nama = "asmodeus"
hero1.umur = 12

hero2.nama = "beelzebub"
hero2.umur = 1123

print(hero1.__dict__) 
print(hero2.__dict__)
print(hero1)
print(hero2)

seluruh = hero1.nama + " " + hero2.nama
umur_seluruh = hero1.umur + hero2.umur
print(seluruh)
print(umur_seluruh)