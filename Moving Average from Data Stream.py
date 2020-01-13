class MovingAverage:

    def __init__(self, size):
        self.data=[None]*size
        self.front=0
        self.back=-1
        self.s=0
        self.sizer=size
    
    def next(self, val):  
        #check if queue is full, if it is, subtract the oldest item from the sum and remove it from the queue
        if self.isFull():
            self.s -= self.data[self.front]
            self.data[self.front]=None
            self.front= (self.front+1) % self.sizer
        
        # add the item into the queue and add it to the sum    
        self.back= (self.back+1) % self.sizer 
        self.data[self.back] = val
        self.s += val
        
        if self.isFull():
            return (self.s/self.sizer)
        
        return (self.s/(self.back+1))
        
    def isEmpty(self) -> bool:
        if self.data[self.front] is not None or self.data[self.back] is not None:
            return False
        elif self.front - self.back == 0:
            return True
        else: 
            return False
    
    def isFull(self) -> bool:
        if self.data[self.front] is None or self.data[self.back] is None:
            return False
        elif self.front - self.back == 1 or self.front - self.back == -self.sizer+1:
            return True
        else: 
            return False 
