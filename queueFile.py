class passenger:
    def __init__(self, name, origin, destination, weight):
        self._name = name
        self._origin = origin
        self._destination = destination
        self._weight = weight

    def getOrigin(self):
        return self._origin
    def getName(self):
        return self._name
    def getDestination(self):
        return self._destination
    def getWeight(self):
        return self._weight
    
class queue:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.passengerList = []
    
    def isFull(self):
        if len(self.passengerList) == self.maxSize:
            return True
        else:
            return False
        
    def enqueue(self, list):
        if self.isFull() ==False:
            obj = passenger
            self.passengerList
