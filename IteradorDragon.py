class Iterator:
    def getNext(self):
        pass
    def hasMore(self):
        pass

class IterableCollection:
    def createIterator(self):
        pass    

class ListIterator(Iterator):
    def __init__(self, list):
        self.list = list
        self.index = 0
    def getNext(self):
        if self.hasMore():
            item = self.list[self.index]
            self.index += 1
            return item
        return None
    def hasMore(self):
        if self.index < len(self.list):
            return True
        return False
    
class DictIterator(Iterator):
    def __init__(self, dict):
        self.dict = dict
        self.keys = list(dict.keys())
        self.index = 0
    def getNext(self):
        if self.hasMore():
            key = self.keys[self.index]
            item = self.dict[key]
            self.index += 1
            return item
        return None
    def hasMore(self):
        if self.index < len(self.keys):
            return True
        return False
    
class ListCollection(IterableCollection):
    def __init__(self, collection):
        self.collection = collection
    def createIterator(self):
        return ListIterator(self.collection)
    
class DictCollection(IterableCollection):
    def __init__(self, collection):
        self.collection = collection
    def createIterator(self):
        return DictIterator(self.collection)    

    
collection_list = ListCollection([1, 2, 3, 4, 5])
iterator = collection_list.createIterator()

while iterator.hasMore():
    print(iterator.getNext())