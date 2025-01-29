import csv

def parseCSV(file_path):
    """Lit un fichier CSV et renvoie les données en excluant la première ligne."""
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Ignore la première ligne (en-tête)
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"Le fichier '{file_path}' est introuvable.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")