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
            # Sélection gloutonne des nombres les plus grands possibles
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
        return combinaison

    def dumpHits(self):
        for hit in self.hits:
            hit.dumpInfo()

    def genHits(self, unsortedHits):
        self.hits = sorted(unsortedHits, key=lambda obj: obj.dmg, reverse=True)