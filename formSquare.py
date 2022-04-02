import math

from numpy import square

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


# a,b,c,d = Point(10,20), Point(20,10), Point(10,10), Point(-20,-20)

#print(formSquare(a,b,c,d))

def countSquares(points):
    pointsLen = len(points)

    if pointsLen < 4:
        return 0

    if pointsLen == 4:
        if formSquare(points[0], points[1], points[2], points[3]):
            return 1
        else:
            return 0

    squares = 0
    
    
    for p1 in range(pointsLen):
        for p2 in range(p1 + 1, pointsLen):
            for p3 in range(p2 + 1, pointsLen):
                for p4 in range(p3 + 1, pointsLen):
                    if formSquare(points[p1], points[p2], points[p3], points[p4]):
                        squares += 1

    return squares

ps = [Point(10,20), Point(20,10), Point(10,10), Point(20,20), Point(30,20), Point(30,10), Point(0,20), Point(0,10)]
print(countSquares(ps))