import morfeusz2
import csv
import random

def extractVerbsFromPolishStatements(statement):
    morfeuszObject = morfeusz2.Morfeusz()
    analysisObject = morfeuszObject.analyse(statement)

    verbsPositionList = []
    for currentToken in analysisObject:
        if currentToken[2][2].startswith("subst"):
            verbsPositionList.append(currentToken[0])

    verbsPositionList = list(dict.fromkeys(verbsPositionList))

    return verbsPositionList

def extractVerbsFromTextFile(filePath):
    readStatement = []

    with open(filePath, 'r', encoding='utf-8') as file:
        for line in file:
            readStatement.append(line.strip())

    return readStatement

def saveToCSV(data, filePath):

    with open(filePath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Statement', 'Verbs'])

        for statement, verbs in data.items():
            statement.strip()
            verbStrings = [str(verb) for verb in verbs] 
            writer.writerow([statement, ', '.join(verbStrings)])

def readCSV(file_path):
    data = []

    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:
            statement, verbs = row
            verbsList = verbs.split(', ')
            data.append((statement, verbsList))

    return data

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

def replaceWordAtIndex(inputString, index, newWord):
    words = inputString.split()

    if 0 <= index < len(words):
        words[index] = newWord
        return ' '.join(words)
    else:
        return inputString 

def randomSentenceSubstitution(wordToInsert = "pipi"):
    data = readCSV("przyslowia.csv")
    statementNumber = random.randint(0, len(data))
    wordNumber = int(random.choice(data[statementNumber][1]))
    replacedSentence = replaceWordAtIndex(data[statementNumber][0], wordNumber, wordToInsert)
    print(replacedSentence)

def main():
    randomSentenceSubstitution()

if __name__ == "__main__":
    main()
