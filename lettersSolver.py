from resources.dictionaryHelper import *
import sys, time

def solve(cards):
    words = findAllFromDefaultDictionary(cards)
    if len(words) == 0:
        return ""
    else:
        return max(words, key=len)

if __name__ == "__main__":
    start_time = time.time()
    pool = sys.argv[1]
    print(solve(pool))
    print("Completed in %.2f seconds" % (time.time() - start_time))