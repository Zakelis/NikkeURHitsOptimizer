from itertools import combinations

class Boss:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.hits = []  # Sum of all hits against this boss

    def findClosestCombination(self):
        print("Starting hits computation for boss :", self.name)

        nombres = []
        totalPossible = 0
        for hit in self.hits:
            nombres.append(hit.dmg)
            totalPossible += hit.dmg

        print(nombres)
        cible = self.hp
        print(cible, totalPossible)

        if totalPossible < cible:
            print("Not reachable")
            return

        somme_actuelle = 0
        combinaison = []

        for nombre in nombres:
            if somme_actuelle + nombre <= cible:
                combinaison.append(nombre)
                somme_actuelle += nombre

                # Si on atteint la cible, on stoppe
            if somme_actuelle >= cible:
                return combinaison

        # Vérification finale
        print("Ended hits computation for boss :", self.name)
        print("Combinaison", combinaison, "total", sum(combinaison), "vs target", self.hp, ":", self.hp - sum(combinaison))

        #  TODO post-process to run 1 or 2 lowest hits to complete the boss ?
        #  TODO only take the biggest hit from a player, not multiple per boss
        #  TODO player/boss weight on an attempt
        #  TODO remove used hits from this boss and other hits on other boss using at least 1 nikke of the used comp
        return combinaison

    def dumpHits(self):
        for hit in self.hits:
            hit.dumpInfo()

    def genHits(self, unsortedHits):
        self.hits = sorted(unsortedHits, key=lambda obj: obj.dmg, reverse=True)