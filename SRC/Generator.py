import random
import requests
import Helpers

class Generator():
    def __init__(self, params={}) -> None:
        self.dataFile = "./przyslowia.csv" if 'dataFile' not in params.keys() else params['dataFile']
        self.imageFolder = "./IMAGES" if 'imageFolder' not in params.keys() else params['imageFolder']
        self.fontFile = "./FONTS/impact.ttf" if 'fontFile' not in params.keys() else params['fontFile']
        self.aiURL = "Not set!" if 'aiURL' not in params.keys() else params['aiURL']
        self.aiPrompt = None if 'aiPrompt' not in params.keys() else params['aiPrompt']
        self.currentBuffer = {"text": None,
                              "nounIndex": []}

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

    def generateImage(self):
        firstHalfOfSentence, secondHalfOfSentence = Helpers.splitStringInHalf(self.currentBuffer["text"])
        Helpers.makeMeme(firstHalfOfSentence, secondHalfOfSentence, Helpers.obtainRandomImage(self.imageFolder), self.fontFile, "output.jpg")  