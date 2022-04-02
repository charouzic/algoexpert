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

    if distanceAtoB == distanceAtoC and 2 * distanceAtoB == distanceAtoD and 2 * countDistance(D, B) == countDistance(B,C) and countDistance(B,C) == distanceAtoD:
        return True
        
    elif distanceAtoB == distanceAtoD and 2 * distanceAtoB == distanceAtoC and 2 * countDistance(C, B) == countDistance(B, D) and countDistance(B, D) == distanceAtoC:
        return True

    elif distanceAtoC == distanceAtoD and 2 * distanceAtoC == distanceAtoB and 2 * countDistance(B, C) == countDistance(C, D) and countDistance(C, D) == distanceAtoB:
        return True

    else:
        return False

def countDistance(A,B):
    return ((A.x-B.x)*(A.x-B.x) + (A.y-B.y)*(A.y-B.y))


a,b,c,d = Point(10,20), Point(20,10), Point(10,10), Point(20,20)

print(formSquare(a,b,c,d))

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

ps = [Point(10,20), Point(20,10), Point(10,10), Point(20,20), Point(30,20), Point(30,10), Point(10,0), Point(30,0)]
print(countSquares(ps))