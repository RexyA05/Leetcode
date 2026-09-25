class MyQueue(object):

    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self, x):
        #copying elements from s1 to s2
        while self.s1:
            self.s2.append(self.s1.pop())
        #push the new element into s1
        self.s1.append(x)
        #copy all the elements of s2 into s1
        while self.s2:
            self.s1.append(self.s2.pop())
        

    def pop(self):
        return self.s1.pop()

    def peek(self):
        return self.s1[-1]
        

    def empty(self):
        return len(self.s1)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()