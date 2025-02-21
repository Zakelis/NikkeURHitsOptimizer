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
        self.bossWeight = 1

    def getInfoInHitRoute(self, playerHitCount, currDmg, hitIndex, isLast, bossHP):
        hitDmgPercentage = round(self.dmg / bossHP * 100, 3)
        hpLeft = max(bossHP - currDmg, 0)
        hpLeftPercentage = round(max(hpLeft / bossHP * 100, 0), 3)
        isLastText = ""
        if isLast is True:
            isLastText = " --- KILL - Hit restored."
        return (str(hitIndex) + " : " + str(self.playerName) + " --- " + self.returnCompString() +
                " --- DMG : " + str(self.dmg) + " (" + str(hitDmgPercentage) + " %)" +
                " --- HP LEFT : " + str(hpLeft) + " (" + str(hpLeftPercentage) + " %)" +
                isLastText + " --- HITS LEFT : " + str(playerHitCount))

    def dumpHitStatusInHitRoute(self, playerHitCount, currDmg, hitIndex, isLast, bossHP):
        print(self.getInfoInHitRoute(playerHitCount, currDmg, hitIndex, isLast, bossHP))

    def getInfo(self):
        return (self.playerName + " hit against " + self.bossName + " : " + str(self.dmg) + " with comp : " + self.returnCompString() +
                " --- Player weight : " + str(round(self.playerWeight, 3)) + " --- Boss weight : " + str(round(self.bossWeight, 3)))

    def dumpInfo(self):
        print(self.getInfo())

    def returnCompString(self):
        return self.p1 + "/" + self.p2 + "/" + self.p3 + "/" + self.p4 + "/" + self.p5

    def isUsingConflictualComp(self, otherHit):
        set_self = {self.p1, self.p2, self.p3, self.p4, self.p5}
        set_otherHit = {otherHit.p1, otherHit.p2, otherHit.p3, otherHit.p4, otherHit.p5}
        return not set_self.isdisjoint(set_otherHit)