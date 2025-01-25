from itertools import combinations
import SheetParser

def find_closest_combination(numbers, target):
    closest_combination = None
    closest_sum = None
    min_difference = float('inf')

    # Boucle sur toutes les tailles de combinaisons possibles
    for r in range(1, len(numbers) + 1):
        for combination in combinations(numbers, r):
            # Calcule la somme des dégâts pour cette combinaison
            current_sum = sum(num[1] for num in combination)
            # Calcule la différence avec la cible
            difference = abs(target - current_sum)
            # Si cette combinaison est meilleure, on la garde
            if difference < min_difference:
                min_difference = difference
                closest_combination = combination
                closest_sum = current_sum

    return closest_combination, closest_sum

def main():
    numbers = [
        ("union member 1", 50),
        ("union member 2", 70),
        ("union member 3", 30),
        ("union member 4", 90)
    ]
    target = 100

    best_combination, best_sum = find_closest_combination(numbers, target)
    print("Meilleure combinaison :", best_combination)
    print("Somme des dégâts :", best_sum)

    rows = SheetParser.parse_tsv("C:/Users/stany/Downloads/SOLACE UNION RAID AVAILABILITY v - MOCK HARD BOSSES HERE.tsv")
    for row, value in rows.items():
        print(row, value)

# Appel de la fonction main
if __name__ == "__main__":
    main()
