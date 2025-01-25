import csv

def parse_tsv(file_path):
    result = {}
    delimiter = '\t'
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                stripped_line = line.strip()
                if stripped_line:  # Ignore les lignes vides
                    # Découpe la ligne selon le délimiteur spécifié
                    result[line_number] = stripped_line.split(delimiter)
    except FileNotFoundError:
        print(f"Le fichier '{file_path}' est introuvable.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

    return result