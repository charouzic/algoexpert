import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def formSquare(A, B, C, D):
    distanceAtoB = countDistance(A,B)
    distanceAtoC = countDistance(A,C)
    distanceAtoD = countDistance(A,D)

    if distanceAtoB == 0 or distanceAtoC == 0 or distanceAtoD == 0:
        return False

    if distanceAtoB == distanceAtoC and 2 * distanceAtoB == distanceAtoD and countDistance(D, B) == countDistance(D,C):
        return True
        
    elif distanceAtoB == distanceAtoD and 2 * distanceAtoB == distanceAtoC and countDistance(C, B) == countDistance(C, D):
        return True

    elif distanceAtoC == distanceAtoD and 2 * distanceAtoC == distanceAtoB and countDistance(B, C) == countDistance(B, D):
        return True

    else:
        return False

def countDistance(A,B):
    return ((A.x-B.x)**2 + (A.y-B.y)**2)


a,b,c,d = Point(10,20), Point(20,10), Point(10,10), Point(-20,-20)

print(formSquare(a,b,c,d))