import time
import threading


def printEven(upTo):
    if upTo > 0:
        for i in range(upTo):
            if i % 2 == 0:
                print(i)
            time.sleep(0.1)

def printOdd(upTo):
    if upTo > 0:
        for i in range(upTo):
            if i % 2 != 0:
                print(i)
            time.sleep(0.1)

even = threading.Thread(target=printEven, args=(20,))
even.start()

odd  = threading.Thread(target=printOdd, args=(20,))
odd.start()

even.join()
odd.join()


print("done")