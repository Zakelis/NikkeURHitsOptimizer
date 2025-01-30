class Hit:
    def __init__(self, dmg, p1, p2, p3, p4, p5, bossName):
        self.dmg = dmg
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.bossName = bossName
        self.weight = 1

    def returnCompString(self):
        return self.p1 + "/" + self.p2 + "/" + self.p3 + "/" + self.p4 + "/" + self.p5
