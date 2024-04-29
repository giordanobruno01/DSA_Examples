class item:
    def __init__(self): 
        self.name = ""
        self.prev = None
        self.next = None

    def linkPrev(self, obj):
        self.prev = obj

    def linkNext(self, obj):
        self.next = obj


class linkedList:
    def __init__(self) -> None:
        pass