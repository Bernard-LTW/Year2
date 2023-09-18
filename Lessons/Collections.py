import random

class collection:
    def __init__(self):
        self.items = []
        self.location = 0

    def addItem(self, item):
        self.items.append(item)

    def isEmpty(self) -> bool:
        return bool(self.items)

    def hasNext(self) -> bool:
        return self.location < len(self.items)

    def getNext(self):
        if self.hasNext():
            self.location += 1
            return self.items[self.location - 1]
        else:
            return None

    def resetNext(self):
        self.location = 0
        return

    def removeNext(self):
        if self.hasNext():
            self.items.pop(self.location)
        else:
            return None

    def removeLast(self):
        self.items.pop()
        return

    def addFirst(self, item):
        self.items.insert(0, item)
        return

    def NUKEMODE(self):
        self.items.clear()
        return

    def randomize(self):
        random.shuffle(self.items)
        return





#Imagining how the user would use the class
x = collection()
x.addItem('bob')
print(x.isEmpty())
print(x.hasNext())