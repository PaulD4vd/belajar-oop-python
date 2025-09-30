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