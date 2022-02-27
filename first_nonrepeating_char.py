string = "faadabcbbebdf"

d = {}
idx = 0
	
for char in string:
		if char not in d:
			d[char] = [1, idx]
			idx += 1
		else:
			d[char][0] += 1
			idx += 1
        
keys = d.keys()

idx = 0
        
# for i in keys:
#     if d[i] == 1:
#         print(idx)
#         break
#     idx += 1

print(keys)
print(d)
