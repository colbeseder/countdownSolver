from lettersHelper import *
import sys

if __name__ == "__main__":
    pool = sys.argv[1]
    words = findAllFromDefaultDictionary(pool)
    if len(words) == 0:
        print("None found")
    else:
        best = max(words, key=len)
        print("%s (%s)"%(best, len(best)))