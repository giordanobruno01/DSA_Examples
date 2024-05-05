class Item:
    def __init__(self,data):
        self.next = None
        self.data = data
        


obj1 = Item("hello")
head = obj1
currentItem = head

obj2 = Item("holla")
currentItem.next = obj2 #this line is linking to next 
currentItem = currentItem.next #this line is setting the current from previous to the new item
cat = "cat name"
catCopy = cat
catCopy += " plus"
print(catCopy)
obj3 = Item("namaste")
currentItem.next = obj3
currentItem = obj3

disp = head
while(disp != None):
    print("Item " ,disp.data )
    disp = disp.next

    

