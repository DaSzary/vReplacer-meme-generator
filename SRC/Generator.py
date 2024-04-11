import random
import requests
from Helpers import randomSentence, replaceWordAtIndex, splitStringInHalf, makeMeme, obtainRandomImage

class Generator():
    def __init__(self, params={}) -> None:
        self.dataFile = "../przyslowia.csv" if 'dataFile' not in params.keys() else params['dataFile']
        self.imageFolder = "../IMAGES" if 'imageFolder' not in params.keys() else params['imageFolder']
        self.fontFile = "../FONTS/Impact.ttf" if 'fontFile' not in params.keys() else params['fontFile']
        self.aiURL = "Not set!" if 'aiURL' not in params.keys() else params['aiURL']
        #self.aiPrompt = "Not set!" if 'aiPrompt' not in params.keys() else params['aiPrompt']
        self.currentBuffer = {"text": None,
                              "nounIndex": []}

    def loadRandomSentence(self):
        self.currentBuffer["text"], self.currentBuffer["nounIndex"] = randomSentence(self.dataFile)
    
    def changeRandomNoun(self, wordToChange):
        wordNumber = int(random.choice(self.currentBuffer["nounIndex"].pop()))
        self.currentBuffer["text"] = replaceWordAtIndex(self.currentBuffer["text"], wordNumber, wordToChange)

    def checkSpelling(self):
        data = {
            "model": "bielik4",
            "prompt": f'Popraw zdanie w nawiasach tylko przez odmianę słów [{self.currentBuffer["text"]}]. Twoja odpowiedź musi zawierać tylko poprawione zdanie po polsku i nic więcej.',
            "stream": False
        }

        response = requests.post(self.aiURL, json=data)
        self.currentBuffer["nounIndex"] = None
        return response.json()['response']

    def generateImage(self):
        firstHalfOfSentence, secondHalfOfSentence = splitStringInHalf(self.currentBuffer["text"])
        makeMeme(firstHalfOfSentence, secondHalfOfSentence, obtainRandomImage(self.imageFolder), "output.jpg")  