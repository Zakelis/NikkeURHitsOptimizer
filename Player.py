from Hit import Hit
import Utilities


class Player:
    def __init__(self, name, b1Name, b2Name, b3Name, b4Name, b5Name):
        # Définition des variables membres
        self.name = name
        self.synchro = 0  # Variable membre avec une valeur initiale
        self.hits = []
        self.bossesNames = [b1Name, b2Name, b3Name, b4Name, b5Name]
        self.meanOfHitsWeights = 1

    def feedAllHits(self, hitLines):
        self.hits.append([self.bossesNames[0], []])
        self.hits.append([self.bossesNames[1], []])
        self.hits.append([self.bossesNames[2], []])
        self.hits.append([self.bossesNames[3], []])
        self.hits.append([self.bossesNames[4], []])
        for parsedHit in hitLines:
            if self.name == Utilities.getFirstListItem(parsedHit):
                self.feedHit(parsedHit)

    def feedHit(self, hitLine):
        dmg = int(Utilities.getNthListItem(hitLine, 1)) * 1000000  #  Dmg is parsed in millions
        p1 = Utilities.getNthListItem(hitLine, 2)
        p2 = Utilities.getNthListItem(hitLine, 3)
        p3 = Utilities.getNthListItem(hitLine, 4)
        p4 = Utilities.getNthListItem(hitLine, 5)
        p5 = Utilities.getNthListItem(hitLine, 6)
        bossName = Utilities.getLastListItem(hitLine)
        hit = Hit(self.name, dmg, p1, p2, p3, p4, p5, bossName)

        if bossName == self.bossesNames[0]:
            self.hits[0][1].append(hit)
        if bossName == self.bossesNames[1]:
            self.hits[1][1].append(hit)
        if bossName == self.bossesNames[2]:
            self.hits[2][1].append(hit)
        if bossName == self.bossesNames[3]:
            self.hits[3][1].append(hit)
        if bossName == self.bossesNames[4]:
            self.hits[4][1].append(hit)


    def dumpAllHitsByStrongestHit(self):
        allHitsList = self.getAllHits()

        sortedHitsByStrongest = sorted(allHitsList, key=lambda obj: obj.dmg, reverse=True)
        self.dumpAllHitsFromList(sortedHitsByStrongest)

    def dumpBossHitsByStrongestHit(self, bossName):
        bossHits = []
        if bossName == self.bossesNames[0]:
            bossHits = self.hits[0][1]
        if bossName == self.bossesNames[1]:
            bossHits = self.hits[1][1]
        if bossName == self.bossesNames[2]:
            bossHits = self.hits[2][1]
        if bossName == self.bossesNames[3]:
            bossHits = self.hits[3][1]
        if bossName == self.bossesNames[4]:
            bossHits = self.hits[4][1]

        sortedHitsByStrongest = sorted(bossHits, key=lambda obj: obj.dmg, reverse=True)

        print("Dumping strongest hits for player on boss", bossName)
        for hit in sortedHitsByStrongest:
            hit.dumpInfo()

    def dumpBossHits(self, bossName):
        bossHits = []
        if bossName == self.bossesNames[0]:
            bossHits = self.hits[0][1]
        if bossName == self.bossesNames[1]:
            bossHits = self.hits[1][1]
        if bossName == self.bossesNames[2]:
            bossHits = self.hits[2][1]
        if bossName == self.bossesNames[3]:
            bossHits = self.hits[3][1]
        if bossName == self.bossesNames[4]:
            bossHits = self.hits[4][1]

        print("Dumping hits for player on boss", bossName)
        for hit in bossHits:
            hit.dumpInfo()

    def dumpAllHitsFromList(self, hitList):
        print("Dumping all hits from list for player", self.name)
        for hit in hitList:
            hit.dumpInfo()

    def dumpAllHits(self):
        print("Dumping all hits for player", self.name)
        for boss in self.hits:
            self.dumpBossHits(boss[0])

        print("Adjusted mean of hits weights is", self.meanOfHitsWeights)

    def getNumberOfBossHits(self, bossName):
        if bossName == self.bossesNames[0]:
            return self.hits[0][1].__len__()
        if bossName == self.bossesNames[1]:
            return self.hits[1][1].__len__()
        if bossName == self.bossesNames[2]:
            return self.hits[2][1].__len__()
        if bossName == self.bossesNames[3]:
            return self.hits[3][1].__len__()
        if bossName == self.bossesNames[4]:
            return self.hits[4][1].__len__()
        return 0

    def getNumberOfAllHits(self):
        return self.getAllHits().__len__()

    def getBossHits(self, bossName):
        if bossName == self.bossesNames[0]:
            return self.hits[0][1]
        if bossName == self.bossesNames[1]:
            return self.hits[1][1]
        if bossName == self.bossesNames[2]:
            return self.hits[2][1]
        if bossName == self.bossesNames[3]:
            return self.hits[3][1]
        if bossName == self.bossesNames[4]:
            return self.hits[4][1]
        return []

    def getAllHits(self):
        allHitsList = []
        for bosses in self.hits:
            for hit in bosses[1]:
                allHitsList.append(hit)

        return allHitsList

    def adjustMeanOfHitsWeights(self):
        total = 0
        allHits = self.getAllHits()
        for hit in allHits:
            total += hit.playerWeight

        self.meanOfHitsWeights = total / self.getNumberOfAllHits()

    def adjustHitsWeights(self):
        highestHit = 0
        for boss in self.hits:
            for hit in boss[1]:
                if hit.dmg > highestHit:
                    highestHit = hit.dmg

        for boss in self.hits:
            for hit in boss[1]:
                hit.playerWeight = hit.dmg / highestHit

        self.adjustMeanOfHitsWeights()
