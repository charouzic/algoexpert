k = 3
tasks = [1,3,5,3,1,4]

task_positions = [] #tuple of (value, position)
for i in range(len(tasks)):
    task_positions.append((tasks[i],i))

sorted_tasks = sorted(task_positions, key=lambda x: x[0])

print(sorted_tasks)

res = []

for i in range(k):
    x = sorted_tasks[i]
    y = sorted_tasks[-1-i]
    res.append([x[1], y[1]])