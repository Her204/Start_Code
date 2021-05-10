class PartyAnimal:
    x = 2
    def party(self):
        self.x = self.x + 1
        print("so far",self.x)
an = PartyAnimal()
an.party()
an.party()
an.party()
print(dir(an))
print(type(an))