class Hit:
    def __init__(self, playerName, dmg, p1, p2, p3, p4, p5, bossName):
        self.playerName = playerName
        self.dmg = dmg
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.bossName = bossName
        self.playerWeight = 1
        self.bossWeight = 0.42

    def getInfo(self):
        return (self.playerName + " hit against " + self.bossName + " : " + str(self.dmg) + " with comp :" + self.returnCompString() +
                " --- Player weight : " + str(self.playerWeight) + " --- Boss weight : " + str(self.bossWeight))

    def dumpInfo(self):
        print(self.getInfo())

    def returnCompString(self):
        return self.p1 + "/" + self.p2 + "/" + self.p3 + "/" + self.p4 + "/" + self.p5
