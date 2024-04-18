import time
import os
from dotenv import load_dotenv

from Generator import Generator

# Główna funkcja
def main():
    load_dotenv()
    params = {
            "dataFile": "./przyslowia.csv",
            "imageFolder": "./IMAGES",
            "fontFile": "./FONTS/impact.ttf",
            "aiURL": os.getenv("URL"),
            "aiPrompt": 'Popraw zdanie w nawiasach tylko przez odmianę słów [{text}]. Twoja odpowiedź musi zawierać tylko poprawione zdanie po polsku i nic więcej.'
            }
    generator = Generator(params)
    generator.loadRandomSentence()
    print(generator.currentBuffer)
    generator.changeRandomNoun("pipi")
    print(generator.currentBuffer)
    start = time.time()
    generator.checkSpelling()
    end = time.time()
    generator.generateImage()
    print(f'Time of request: {end-start}')

if __name__ == "__main__":
    main()
