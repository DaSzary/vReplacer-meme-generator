import random
import requests
import Helpers

class Generator():
    def __init__(self, params = {}) -> None:
        self.dataFile = None
        self.imageFolder = None
        self.fontFile = None
        self.aiURL = None
        self.aiPrompt = None
        self.currentBuffer = {"text": None,
                              "nounIndex": []}
        self.setParams(params)

    def setParams(self, params = {}):
        if 'dataFile' in params.keys(): self.setDataFilePath(params['dataFile'])
        if 'imageFolder' in params.keys(): self.setImageFolderPath(params['imageFolder'])
        if 'fontFile' in params.keys(): self.setFontFilePath(params['fontFile'])
        if 'aiURL' in params.keys(): self.setAiURL(params['aiURL'])
        if 'aiPrompt' in params.keys(): self.setAiPrompt(params['aiPrompt'])

    def getCurrentText(self): return self.currentBuffer["text"]
    
    def setDataFilePath(self, pathToFile : str): self.dataFile = pathToFile
    
    def setImageFolderPath(self, pathToFolder : str): self.imageFolder = pathToFolder

    def setFontFilePath(self, pathToFile : str): self.fontFile = pathToFile

    def setAiURL(self, URL : str): self.aiURL = URL

    def setAiPrompt(self, prompt : str):
        if "{text}" not in prompt:
            raise Exception("Prompt should contain '{text}'")
        self.aiPrompt = prompt

    def loadRandomSentence(self):
        self.currentBuffer["text"], self.currentBuffer["nounIndex"] = Helpers.randomSentence(self.dataFile)
    
    def changeRandomNoun(self, wordToChange):
        wordNumber = int(random.choice(self.currentBuffer["nounIndex"].pop()))
        self.currentBuffer["text"] = Helpers.replaceWordAtIndex(self.currentBuffer["text"], wordNumber, wordToChange)

    def checkSpelling(self):
        data = {
            "model": "bielik4",
            "prompt": self.aiPrompt.format(text = self.currentBuffer["text"]),
            "stream": False
        }

        response = requests.post(self.aiURL, json=data)
        self.currentBuffer["nounIndex"] = None
        self.currentBuffer["text"] = response.json()['response']

    def generateImage(self, outputFile = "output.jpg"):
        firstHalfOfSentence, secondHalfOfSentence = Helpers.splitStringInHalf(self.currentBuffer["text"])
        Helpers.makeMeme(firstHalfOfSentence, secondHalfOfSentence, Helpers.obtainRandomImage(self.imageFolder), self.fontFile, "output.jpg")  