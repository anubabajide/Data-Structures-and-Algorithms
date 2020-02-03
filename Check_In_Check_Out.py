class Subway:
    def __init__(self):
        #data stores customer ID as key and array of trips as value
        #trip contains (route, duration, complete_check) : complete_check =1 for complete and 0 for incomplete 
        self.data={}
        #location stores route as key and trip info tuple as value
        #trip info tuple contains (total duration, number of trips)
        self.Location={}

    def swipeIn(self, time, ID, loc)-> bool:
        #initialize non-existent customer and update existent customer
        if ID in self.data:
            #check if last trip has been completed
            if self.data[ID][-1][2] !=1: 
                return False
            self.data[ID].append([loc+'-', time, 0])
            return True
        else:
            self.data[ID]=[[loc+'-', time, 0]]
            return True

    def swipeOut(self, time, ID, loc)-> bool:
        #check if ID exists
        if ID not in self.data:
            return False
        #check if trip is already completed
        if self.data[ID][-1][2] !=0:
            return False
        #update trip route, duration and complete_check
        self.data[ID][-1][0]= self.data[ID][-1][0] + loc
        self.data[ID][-1][1]= time - self.data[ID][-1][1]
        self.data[ID][-1][2]= 1

        self.updateLocation(self.data[ID][-1][0], self.data[ID][-1][1])
        return True
    
    def updateLocation(self, route, duration):
        #initialize non-existent route or update existent route
        if route in self.Location:
            self.Location[route][0] += duration
            self.Location[route][1] += 1
        else:
            self.Location[route] = [duration, 1]

    def Avg(self, loc, dest):
        route=loc + '-' + dest
        #error for non-existent trip average for existent trip
        if route in self.Location:
            return((self.Location[route][0])/(self.Location[route][1]))
        else:
            return False
#sub= subway()
#sub.swipein(0,'a1','a')
#sub.swipeout(2,'a1','b')
#sub.avg('a','b')
#sub.swipein(0,'a2','a')
#sub.swipeout(4,'a2','b')
#sub.avg('a','b')