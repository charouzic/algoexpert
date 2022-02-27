array =[5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

def isValidSubsequence(array, sequence):
    # Write your code here.
    position = 0
    for i in range(len(array)):
        x = array[i]
        y = sequence[position]
        if x == y:
            position += 1
            if position == len(sequence):
                return True
    return False

x = isValidSubsequence(array, sequence)

print(x)