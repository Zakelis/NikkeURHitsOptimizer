import Utilities
from Boss import Boss
from Player import Player
from Hit import Hit


class Computations:
    def __init__(self):
        #  Computation-related containers
        self.players = []  # List of players that mocked
        self.remainingValidHits = []
        self.bossesHits = []  # All final hits per boss

        #  Bosses data
        self.bossesHPMarginError = 1.0

        #  Bosses names
        self.B1Name = None
        self.B2Name = None
        self.B3Name = None
        self.B4Name = None
        self.B5Name = None

        #  Bosses HPs
        self.B1T1HP = None
        self.B2T1HP = None
        self.B3T1HP = None
        self.B4T1HP = None
        self.B5T1HP = None
        self.B1T2HP = None
        self.B2T2HP = None
        self.B3T2HP = None
        self.B4T2HP = None
        self.B5T2HP = None

        #  Bosses objects
        self.B1T1 = None
        self.B2T1 = None
        self.B3T1 = None
        self.B4T1 = None
        self.B5T1 = None
        self.B1T2 = None
        self.B2T2 = None
        self.B3T2 = None
        self.B4T2 = None
        self.B5T2 = None
        self.bosses = []

        self.hp_list_ref = [
            ("Laitance", 29225662800),
            ("Heavy Metal", 29225662800),
            ("Nihilister", 65385671800),
            ("Rb Obelisk", 29225662800),
            ("Gravedigger", 47553215600),
            ("Laitance", 137302384800),
            ("Heavy Metal", 137302384800),
            ("Nihilister", 207407492800),
            ("Rb Obelisk", 137302384800),
            ("Gravedigger", 140841813600)
        ]

    def feedPlayersArray(self, parsedHits):
        exploredPlayers = []
        for hit in parsedHits:
            playerName = Utilities.getFirstListItem(hit)
            if playerName not in exploredPlayers:
                exploredPlayers.append(playerName)
                player = Player(playerName, self.B1Name, self.B2Name, self.B3Name, self.B4Name, self.B5Name)
                self.players.append(player)

        print(self.players.__len__(), "players have mocked so far :")
        for player in self.players:
            print(player.name)

    def feedBossesNames(self):
        self.B1Name = "Laitance"
        self.B2Name = "Heavy Metal"
        self.B3Name = "Nihilister"
        self.B4Name = "Rb Obelisk"
        self.B5Name = "Gravedigger"

    def feedBossesHPs(self):
        self.B1T1HP = int(29225662800 * self.bossesHPMarginError)
        self.B2T1HP = int(29225662800 * self.bossesHPMarginError)
        self.B3T1HP = int(65385671800 * self.bossesHPMarginError)
        self.B4T1HP = int(29225662800 * self.bossesHPMarginError)
        self.B5T1HP = int(47553215600 * self.bossesHPMarginError)
        self.B1T2HP = int(137302384800 * self.bossesHPMarginError)
        self.B2T2HP = int(137302384800 * self.bossesHPMarginError)
        self.B3T2HP = int(207407492800 * self.bossesHPMarginError)
        self.B4T2HP = int(137302384800 * self.bossesHPMarginError)
        self.B5T2HP = int(140841813600 * self.bossesHPMarginError)

    def feedBossesList(self):
        self.feedBossesNames()
        self.feedBossesHPs()

        self.B1T1 = Boss(self.B1Name, self.B1T1HP)
        self.B2T1 = Boss(self.B2Name, self.B2T1HP)
        self.B3T1 = Boss(self.B3Name, self.B3T1HP)
        self.B4T1 = Boss(self.B4Name, self.B4T1HP)
        self.B5T1 = Boss(self.B5Name, self.B5T1HP)
        self.B1T2 = Boss(self.B1Name, self.B1T2HP)
        self.B2T2 = Boss(self.B2Name, self.B2T2HP)
        self.B3T2 = Boss(self.B3Name, self.B3T2HP)
        self.B4T2 = Boss(self.B4Name, self.B4T2HP)
        self.B5T2 = Boss(self.B5Name, self.B5T2HP)
        self.bosses.append(self.B1T1)
        self.bosses.append(self.B2T1)
        self.bosses.append(self.B3T1)
        self.bosses.append(self.B4T1)
        self.bosses.append(self.B5T1)
        self.bosses.append(self.B1T2)
        self.bosses.append(self.B2T2)
        self.bosses.append(self.B3T2)
        self.bosses.append(self.B4T2)
        self.bosses.append(self.B5T2)

        print("After feeding bosses list")
        for boss in self.bosses:
            print(boss.name, boss.hp)

    def feedAllStartingHits(self, parsedHits):
        print("feedAllStartingHits START")
        for player in self.players:
            player.feedAllHits(parsedHits)

        #for player in self.players:
        #    player.adjustHitsWeights()

        #for player in self.players:
        #    player.dumpAllHitsByStrongestHit()


    def feedPlayerHits(self, parsedHits):
        print("feedPlayerHits START")
        self.feedPlayersArray(parsedHits)
        self.feedAllStartingHits(parsedHits)

    def updateHitPlayerWeight(self):
        for player in self.players:
            lowestDmg = 9999999999999
            topDmg = 0
            hits = player.getHits()
            for hit in hits:
                if hit.dmg < lowestDmg:
                    lowestDmg = hit.dmg
                if hit.dmg > topDmg:
                    topDmg = hit.dmg

            for hit in hits:
                hit.playerWeight = (hit.dmg - lowestDmg) / (topDmg - lowestDmg)


    def updateHitBossWeight(self, bossName):
        lowestDmg = 9999999999999
        topDmg = 0
        for player in self.players:
            bossHits = player.getBossHits(bossName)
            for hit in bossHits:
                if hit.dmg < lowestDmg:
                    lowestDmg = hit.dmg
                if hit.dmg > topDmg:
                    topDmg = hit.dmg

        for player in self.players:
            bossHits = player.getBossHits(bossName)
            for hit in bossHits:
                hit.bossWeight = (hit.dmg - lowestDmg) / (topDmg - lowestDmg)

    def initBossHits(self, boss):
        print("Starting gen hits for boss :", boss.name)
        bossHits = []
        for player in self.players:
            hitList = player.getBossHits(boss.name)
            for hit in hitList:
                bossHits.append(hit)
        boss.genHits(bossHits)
        print("Correctly gen hits for boss :", boss.name)


    def computeOptimalHits(self, boss):
        best_combination = boss.findClosestCombination(self.players)
        print("Best combination for boss :", boss.name, "--- HP :", boss.hp)
        totalDmg = 0
        for hit in best_combination:
            hit.dumpInfo()
            totalDmg += hit.dmg

        print("Total dmg :", totalDmg)
        print("Overkill dmg :", totalDmg - boss.hp)
        print("Overkill percentage :", round((totalDmg - boss.hp) / boss.hp * 100, 3), "%")

    def genSolutions(self):
        for boss in self.bosses:
            if boss.hp < 137302384800: #  Failsafe, only treat T1 for now
                self.initBossHits(boss)
                self.updateHitPlayerWeight()
                self.updateHitBossWeight(boss.name)
                self.computeOptimalHits(boss)
                print()
                print()
                boss.dumpHitRoute()
                print()