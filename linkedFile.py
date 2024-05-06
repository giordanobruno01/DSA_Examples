class item:
    def __init__(self,name): 
        self.name = name
        self.prev = None
        self.next = None

    def linkPrev(self, obj):
        self.prev = obj

    def linkNext(self, obj):
        self.next = obj


class linkedList:
    
    def __init__(self):
        self.head = None
        self.message = ""
    
    def add(self, data):
        pass
    
    def addBefore(self, data, nextData):
        pass
    
    def addAfter(self, data, prevData):
        pass

    def delete(self):
        pass

    def deleteData(self, data):
        pass

    def getItems(self):
        return ["ff"]