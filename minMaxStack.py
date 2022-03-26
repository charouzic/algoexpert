# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minMaxStack = []
        
    def peek(self):
        # Write your code here.
        return self.stack[-1]


    def pop(self):
        # Write your code here.
        self.minMaxStack.pop()
        return self.stack.pop()


    def push(self, number):
        # Write your code here.
        if len(self.minMaxStack) > 0:
            minMax = self.minMaxStack[-1]
            minimum = minMax[0]
            maximum = minMax[1]
            
            if number < minimum:
                self.minMaxStack.append((number, maximum))
            elif number > maximum:
                self.minMaxStack.append((minimum, number))
            else:
                self.minMaxStack.append(minMax)
        
        else:
            self.minMaxStack.append((number, number))
        
        self.stack.append(number)
        

    def getMin(self):
        # Write your code here.
        if len(self.stack) == 1:
            return self.peek()
        
        return self.minMaxStack[-1][0]
        


    def getMax(self):
        # Write your code here.
        if len(self.stack) == 1:
            return self.peek()

        return self.minMaxStack[-1][1]