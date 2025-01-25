def find_smallest_sublist(nums, X):
    n = len(nums)
    min_length = float('inf')  # Pour enregistrer la longueur minimale
    min_start = -1
    min_end = -1
    current_sum = 0  # Somme actuelle de la fenêtre
    start = 0  # Début de la fenêtre

    for end in range(n):
        current_sum += nums[end]  # Ajouter l'élément à la somme

        # Dès que la somme est suffisante, essayer de réduire la fenêtre
        while current_sum >= X:
            current_length = end - start + 1
            if current_length < min_length:
                min_length = current_length
                min_start = start
                min_end = end
            current_sum -= nums[start]  # Retirer l'élément de la somme
            start += 1  # Réduire la fenêtre par la gauche

    # Si une sous-liste a été trouvée, retourner cette sous-liste
    if min_start != -1 and min_end != -1:
        return nums[min_start:min_end + 1]

    # Si aucune sous-liste n'a été trouvée
    return []

# Exemple d'utilisation
nums = [1, 2, 3, 4, 5, 6]
X = 11

result = find_smallest_sublist(nums, X)

if result:
    print("La sous-liste la plus petite est :", result)
else:
    print("Aucune sous-liste trouvée.")


def main():
    # Exemple d'utilisation
    nums = [1, 2, 3, 4, 5, 6]
    X = 11

    result = find_smallest_sublist(nums, X)

    if result:
        print("La sous-liste la plus petite est :", result)
    else:
        print("Aucune sous-liste trouvée.")

# Appel de la fonction main
if __name__ == "__main__":
    main()