distances = [5,25,15,10,15]
fuel = [1,2,1,0,3]
mpg = 10

def validStartingCity(distances, fuel, mpg):
    # Write your code here.
	for i in range(len(distances)):
		complete = simulateRun(i ,distances, fuel, mpg)
		if complete == True:
			return i
	
def simulateRun(startCityIndex, distances, fuel, mpg):
	
	milesAvailable = mpg * fuel[startCityIndex]
	
	citiesLength = len(distances)
	
	currentIndex = startCityIndex
	backAtStartCity = False
	firstRound = True
	
	res = False
	
	while (backAtStartCity == False):
		if currentIndex == startCityIndex and firstRound != True:
			backAtStartCity = True
			res = True
		else:	
			firstRound = False
		
			milesAvailable -= distances[currentIndex]
		
			if milesAvailable >= 0:
				if currentIndex+1 == citiesLength:
					currentIndex = 0
				else: currentIndex += 1
			
				milesAvailable += fuel[currentIndex] * mpg
			else:
				backAtStartCity = True
				
	return res
		

result = validStartingCity(distances, fuel, mpg)
print(result)