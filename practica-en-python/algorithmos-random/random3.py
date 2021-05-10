class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name," constructed")
    def party(self):
        self.x = self.x + 1
        print(self.name, " party count ", self.x)
class footballscore(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name," Points ",self.points,"\n")

for i in range(10):
    a =  "bot_" + str(i) + "."
    g = footballscore(a)
    for b in range(i):
        g.party()
        g.touchdown()
    
#ab = "abcdefghijklmnñopqrstuvwxyz"
#for a in ab:
    #p = footballscore("root_" + a)
    #p.party()
    #p.touchdown()
    #p.touchdown()