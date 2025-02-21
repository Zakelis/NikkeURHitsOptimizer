from itertools import combinations

import Utilities

class Boss:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.availableHits = []  # Sum of all hits against this boss
        self.finalHits = []

    def dumpHitRoute(self, players, errorMarginPercentage, maxOverkillPercentage):
        print("*** HIT ROUTE FOR", self.name, "***")
        print()
        print("Final target HP : " + str(self.hp) + " (+" + str(round((errorMarginPercentage * 100) - 100, 1)) + "% error margin from base MAX HP)")
        print("Max allowed overkill percentage : " + str(round((maxOverkillPercentage * 100) - 100, 1)) + "%")
        print()
        currDmg = 0
        isLast = False
        playerHitCount = 3
        for hitIndex, hit in enumerate(self.finalHits):
            if hitIndex is len(self.finalHits) - 1:
                isLast = True
            currDmg += hit.dmg
            for player in players:
                if player.name is hit.playerName:
                    playerHitCount = player.hitsLeft
            hit.dumpHitStatusInHitRoute(playerHitCount, currDmg, hitIndex + 1, isLast, self.hp)

        print()
        overkillDmg = abs(self.hp - currDmg)
        overkillDmgPercentage = round(overkillDmg / self.hp * 100, 3)
        print("Overkill damage : " + str(overkillDmg) + " (" + str(overkillDmgPercentage) + " %)")
        print()
        print("*******************************")
        return self.finalHits

    def getClosestValidHitFromAnotherPlayer(self, combinaison, hitsLeft, currHit, players):
        playerName = currHit.playerName
        for hitIndex, hit in enumerate(hitsLeft):
            if hit.playerName != playerName:
                if not self.canPlayerHit(hit, players):
                    continue
                if self.hasPlayerAlreadyHit(combinaison, hit):
                    continue
                return hitIndex, hit
        return None

    def canPlayerHit(self, hit, playerList):
        for player in playerList:
            if hit.playerName == player.name:
                return player.hitsLeft > 0

    def hasPlayerAlreadyHit(self, combinaison, currHit):
        for okHit in combinaison:
            if okHit.playerName == currHit.playerName:
                return True

        return False

    def determineLastHits(self, hitsLeft, HP):
        print("Starting LAST hits computation for boss :", self.name, "remaining HP :", HP, "remaining hits :")
        #for hit in hitsLeft:
        #    hit.dumpInfo()
        somme_actuelle = 0
        lastHits = []
        # First pass : Try to find a suitable hit

        for hit in hitsLeft:
        #    print("Somme actuelle :", somme_actuelle, "Scanning hit dmg :", hit.dmg, "HP :", HP)
            if somme_actuelle + hit.dmg <= HP * 1.5:
        #        print("Hit accepted, remaining dmg to reach target :", HP - (somme_actuelle + hit.dmg))
                lastHits.append(hit)
                somme_actuelle += hit.dmg
                if somme_actuelle > HP:
                    return lastHits
        #    else:
        #        print("Hit rejected, mult was :", (somme_actuelle + hit.dmg) / HP)
        return []

    def findClosestCombination(self, players, maxOverkillPercentage):
        print("Starting hits computation for boss :", self.name, "HP :", self.hp, "available hits :")
        #for hit in self.availableHits:
        #    hit.dumpInfo()

        nombres = []
        totalPossible = 0
        for hit in self.availableHits:
            nombres.append(hit.dmg)
            totalPossible += hit.dmg

        cible = self.hp
        #print(cible, totalPossible)

        if totalPossible < cible:
            print("Not reachable")
            return

        somme_actuelle = 0
        combinaison = []

        for hitIndex, hit in enumerate(self.availableHits):
            if not self.canPlayerHit(hit, players):
                continue
            if self.hasPlayerAlreadyHit(combinaison, hit):
                continue

            if somme_actuelle + hit.dmg <= cible:
                #  Current hit can not be used to finish the boss, explore further
                if hitIndex < len(self.availableHits) - 1:
                    if somme_actuelle + hit.dmg + self.availableHits[hitIndex+1].dmg > cible:

                        #  First pass : Check if current hit can be associated with the next strongest hit
                        overflow = (somme_actuelle + hit.dmg + self.availableHits[hitIndex+1].dmg) / cible

                        #  If the overkill damage is acceptable, accept both hits as finishers
                        print("Overflow of curr hit + next strongest hit is  :", overflow)
                        if overflow < maxOverkillPercentage:
                            print("Overflow of curr hit + next strongest hit is acceptable :", overflow, "%. Accept both hits")
                            combinaison.append(hit)
                            combinaison.append(self.availableHits[hitIndex+1])
                            self.finalHits = Utilities.getReversedList(combinaison)
                            return self.finalHits

                        #  Second pass : Current hit can not finish the boss but also using the next strongest hit
                        #  would make too much of an overflow, skip this hit
                        if overflow > maxOverkillPercentage:
                            continue

                        #  Second pass : We cannot use the next strongest hit, find the hit that rewards the player with the best attempt among the 5 bosses
                        # Curr and next hit would generate too much overkill damage, share the last hits...
                        # Remaining hits to be sorted by player weight to prioritize players on lower synchro with a good element
                        remainingHits = Utilities.filterSubList(self.availableHits, combinaison)
                        remainingHitsSortedByPlayerWeight = sorted(remainingHits, key=lambda obj: obj.playerWeight, reverse=True)
                        for remainingHit in remainingHits:
                            if not self.canPlayerHit(remainingHit, players):
                                remainingHits.remove(remainingHit)
                            if self.hasPlayerAlreadyHit(combinaison, remainingHit):
                                remainingHits.remove(remainingHit)
                        remainingHP = self.hp - somme_actuelle
                        print()
                        print("About to determine the last hits, current combination is :")
                        for hit in combinaison:
                            hit.dumpInfo()
                        print()
                        lastHits = self.determineLastHits(remainingHitsSortedByPlayerWeight, remainingHP)
                        for lastHit in lastHits:
                            combinaison.append(lastHit)
                        self.finalHits = Utilities.getReversedList(combinaison)
                        return self.finalHits
                if hit.playerWeight > 0.1:
                    combinaison.append(hit)
                    somme_actuelle += hit.dmg

            if somme_actuelle >= cible:
                self.finalHits = Utilities.getReversedList(combinaison)
                return self.finalHits

        print("Ended hits computation for boss :", self.name)

        #  TODO post-process to run 1 or 2 lowest hits to complete the boss ?
        #  TODO only take the biggest hit from a player, not multiple per boss
        #  TODO player/boss weight on an attempt
        #  TODO remove used hits from this boss and other hits on other boss using at least 1 nikke of the used comp
        self.finalHits = Utilities.getReversedList(combinaison)
        return self.finalHits

    def dumpAvailableHits(self):
        for hit in self.availableHits:
            hit.dumpInfo()

    def genHits(self, unsortedHits):
        self.availableHits = sorted(unsortedHits, key=lambda obj: obj.dmg, reverse=True)
