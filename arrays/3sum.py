# D = {}

# targetSum = 0

# array = [12,3,1,2,-6, 5, -8, 6]
# arrLen = len(array)
# array.sort()

# for i in range(arrLen):
#     D[int(i)] = array[i]

# for i in range(arrLen):
#     a = array[i]
#     for j in range(i+1, arrLen):
#         b = array[j]
#         c = - a - b
#         if c in D:
#             k = D[c]

# # -8, 2, 6 ==> 0
# -8 + 2 = 

# string = "abb"
# strLen = len(string)

# res = True

# for i in range((strLen//2)-1):
#     if string[strLen-i-1] != string[i]:
#         res = False
        
# print(res)
string = "AAAAAAAAAAAAABBCCCCDD"

d = {}
for character in string:
    if character in d:
        d[character] += 1
    else:
        d[character] = 1

dKeys = d.keys()

res = ""

# print(dKeys)
for key in d.keys():
		if d[key] < 9:
			res += str(d[key])
			res += str(key)
			
		else:
			count = d[key]
			while count > 0:
				if count - 9 > 0:
					res += "9"
					res += str(key)
					
					count -= 9
					
				else:
					res += str(count)
					res += str(key)
					count = 0

print(dKeys[2])