import csv
import morfeusz2

# Wyciągnięcie rzeczowników z polskich zdań, posiadają one prefix subst:  wg. Morfeusza
def extractVerbsFromPolishStatements(statement):
    # Inicjalizacja obiektów
    morfeuszObject = morfeusz2.Morfeusz()
    analysisObject = morfeuszObject.analyse(statement)

    # Prealokacja listy
    verbsPositionList = []
    # Iteracja po tokenach w naszych zdaniach, jeżeli token jest rzeczownikiem to dodajemy jego pozycję do listy
    for currentToken in analysisObject:
        if currentToken[2][2].startswith("subst"):
            verbsPositionList.append(currentToken[0])

    return list(dict.fromkeys(verbsPositionList))

# Wyciągnięcie zdań z pliku tekstowego linia po linii
def extractVerbsFromTextFile(filePath):
    readStatement = []

    with open(filePath, 'r', encoding='utf-8') as file:
        for line in file:
            readStatement.append(line.strip())

    return readStatement

# Zapisanie danych do pliku CSV
def saveToCSV(data, filePath):
    with open(filePath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Statement', 'Verbs'])

        for statement, verbs in data.items():
            statement.strip()
            verbStrings = [str(verb) for verb in verbs] 
            writer.writerow([statement, ', '.join(verbStrings)])

# Przetwarzanie danych, wyciągnięcie rzeczowników z plików tekstowych i zapisanie ich do pliku CSV
def dataPreprocessing():
    inputFile = "przyslowia.txt"
    outputFile = "przyslowia.csv"
    data = {} 

    statements = extractVerbsFromTextFile(inputFile)

    for i, statement in enumerate(statements):
        verbs = extractVerbsFromPolishStatements(statement)
        data[statement.strip()] = verbs
        print(f"Przetworzono {i+1}/{len(statements)} zdań")
    print("Koniec przetwarzania zdań")

    saveToCSV(data, outputFile)
    print(f"Dane zapisano w {outputFile}")

def main():
    dataPreprocessing()

if __name__ == "__main__":
    main()