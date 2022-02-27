str1 = "abc"
str2 = "yabd"

str1Len = len(str1)
str2Len = len(str2)

firstLine = [x for x in range(str1Len+1)]
opt = []

opt.append(firstLine)



# initializing the matrix
for _ in range(str2Len):
    opt.append([x for x in range(str1Len+1)])

for i in range(1, str2Len+1):
    opt[i][0] = opt[i-1][0] + 1


for i in range(1, str1Len+1):
		for j in range(1, str2Len+1):
			if str1[i-1] == str2[j-1]:
				opt[j][i] = opt[j-1][i-1]
			else: 
				opt[j][i] = min(opt[j][i-1]+1, # insert
							    opt[j-1][i]+1,# substitute
								opt[j-1][i-1]+1)

print(opt[-1][-1])

