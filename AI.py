# for stack
class Stack():
    def __init__(self,initial):
        self.items=[initial]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

a=Stack(1)
print(a.isEmpty())
a.push(2)
a.push(3)
print(a.size())

# for queue
class Queue:
    def __init__(self,intial):
        self.items=[intial]

    def isEmpty(self):
        return self.items==[]
    
    def enqueue(self,item):
        self.items.append(item)
        return item
    
    def dequeue(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)

a=Queue(1)
a.enqueue(2)
a.enqueue(3)

print(a.dequeue())
print(a.dequeue())
print(a.dequeue())
