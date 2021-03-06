# same as the one in the data_structures folder

class Stack :
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

    def top(self):
        if self.is_empty():
            return
        else:
            return self.items[-1:][0]

    def top(self):
        if self.is_empty():
            return
        return self.items[-1]

    def print_contents(self):
        temp = deepcopy(self.items)
        while (len(temp)!= 0):
            print temp.pop()
