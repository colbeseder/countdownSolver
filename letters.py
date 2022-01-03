from resources.dictionaryHelper import *
import sys, time

if __name__ == "__main__":
    start_time = time.time()
    pool = sys.argv[1]
    words = findAllFromDefaultDictionary(pool)
    if len(words) == 0:
        print("None found")
    else:
        best = max(words, key=len)
        print("%s (%s)"%(best, len(best)))
    print("Completed in %.2f seconds" % (time.time() - start_time))