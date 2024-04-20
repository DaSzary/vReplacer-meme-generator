import time
import os
from dotenv import load_dotenv

from VReplacer_Meme_Generator.Generator import Generator

# Główna funkcja
def main():
    load_dotenv()
    params = {
            "dataFile": "./przyslowia.csv",
            "imageFolder": "./IMAGES",
            "fontFile": "./FONTS/impact.ttf",
            "aiModel": "bielik4",
            "aiURL": os.getenv("URL"),
            "aiPrompt": 'Popraw zdanie w nawiasach tylko przez odmianę słów [{text}]. Twoja odpowiedź musi zawierać tylko poprawione zdanie po polsku i nic więcej.'
            }
    generator = Generator(params)
    generator.loadRandomSentence()
    print(generator.currentBuffer)
    generator.changeRandomWord("pipi")
    print(generator.currentBuffer)
    start = time.time()
    #generator.checkSpelling()
    end = time.time()
    generator.generateImage("outputfile.jpg")
    print(f'Time of request: {end-start}')

if __name__ == "__main__":
    main()
