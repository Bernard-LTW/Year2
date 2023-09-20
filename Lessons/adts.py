import random

class collection:
    def __init__(self, items = []):
        self.items = items
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



class queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)
        return

    def dequeue(self):
        item = self.data[0]
        self.data = self.data[1:len(self.data)]
        return item

    def __repr__(self):
        return f"<Queue> {self.data}"


#test the queue
q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.dequeue())
print(q)
