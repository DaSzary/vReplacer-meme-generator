import time
import os
from dotenv import load_dotenv

from Generator import Generator

# Główna funkcja
def main():
    load_dotenv()
    currentSentence = randomSentenceSubstitution("pipi")
    print("sentence to check: ")
    print(currentSentence)
    start = time.time()
    generator.checkSpelling()
    end = time.time()
    generator.generateImage()
    print(f'Time of request: {end-start}')

if __name__ == "__main__":
    main()
