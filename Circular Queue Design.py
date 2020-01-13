class MyCircularQueue:
    
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.data = [None]*k
        self.front=0
        self.back=0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        try:
            if self.isFull() is True:
                return False
            
            self.data[self.back]=value
            
            if self.back >= (len(self.data)-1):
                self.back = 0
            elif self.back >= 0 and self.back < (len(self.data)-1):
                self.back += 1
            else:
                return False
            return True
        except:
            return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        try:
            if self.isEmpty() is True:
                return False
            
            self.data[self.front]=None
            
            if self.front >= (len(self.data)-1):
                self.front = 0
            elif self.front >= 0 and self.front < (len(self.data)-1):
                self.front+=1
            else:
                return False
            
            return True
        except:
            return False

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty() is True:
            return (-1)
        else:
            return self.data[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty() is True:
            return (-1)
        else:
            return self.data[self.back-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.data[self.front]  or self.data[self.back]:
            return False
        elif self.front == self.back:
            return True
        elif (self.data[self.front] is None) and (self.data[self.back] is None):
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if (self.data[self.front] is None) or (self.data[self.back] is None):
            return False
        elif self.front == self.back:
            return True
        else:
            return False



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()