import concurrent.futures
import time

def printEven(upTo):
    if upTo > 0:
        for i in range(upTo+1):
            if i % 2 == 0:
                print(i)
            time.sleep(0.1)
    return "even done"

def printOdd(upTo):
    if upTo > 0:
        for i in range(upTo+1):
            if i % 2 != 0:
                print(i)
            time.sleep(0.1)
    return "odd done"

with concurrent.futures.ThreadPoolExecutor() as executor:
    even = executor.submit(printEven, 20)
    odd = executor.submit(printOdd, 20)

    print(even.result())
    print(odd.result())
    
    