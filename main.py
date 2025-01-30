from itertools import combinations
import SheetParser
from Computations import Computations

def main():
    print("Print the result of sheet parsing :")
    parsedSheetData = SheetParser.parseCSV("./sheetData.csv")
    for row in parsedSheetData:
        print(row)

    computations = Computations()
    computations.feedBossesList()
    computations.feedPlayerHits(parsedSheetData)
    computations.genSolutions()

# Appel de la fonction main
if __name__ == "__main__":
    main()
