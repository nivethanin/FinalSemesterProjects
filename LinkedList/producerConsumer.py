import random
import threading
import time


class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None


class SLinkedList:
    def __init__(self, maxSize):
        self.head = None
        self.MAX_SIZE = maxSize


    def size(self):
        count = 0
        val = self.head

        if self.head is not None:
            val = self.head
            count = 1
            val=val.next

        while(val):
            count +=1
            val = val.next
        
        return count


    def pop(self):
        val = self.head
        while val.next:
            if val.next.next == None:
                val.next = None
            else:
                val = val.next


    def printList(self):
      printval = self.head
      while (printval):
         print(printval.data),
         printval = printval.next


    def addHead(self, data_in):
        if self.size() < self.MAX_SIZE:
            NewNode = Node(data_in)
            NewNode.next = self.head
            self.head = NewNode
        else: 
            print("Too many nodes in the linked list")


    def add(self, data_in):
        if self.size() < self.MAX_SIZE:
            newNode = Node(data_in)
            val = self.head
            while (val):
                val = val.next
                if val.next == None:
                    val.next = newNode


    def isEmpty(self):
        if self.size() == 0:
            return True
        return False


    def isFull(self):
        if self.size() == self.MAX_SIZE:
            return True
        return False


llist = SLinkedList(3)
print(llist.isEmpty())
print(llist.size())
llist.addHead("Mon")
print(llist.size())
llist.addHead("Tue")
print(llist.size())

llist.printList()
llist.pop()
llist.printList()
print(llist.size())
print(llist.MAX_SIZE)


class Thread:
    def __init__(self, maxSize):
        self.llist = SLinkedList(maxSize)


class Producer(Thread):

    def run(self):
        event = threading.Event()
        while True:
            if llist.isFull():
                event.wait()
            else:
                llist.addHead(random.randint(1,9))
                print("pushed")
                
    

class Consumer(Thread):

    def run(self):
        event = threading.Event()
        while True:
            if llist.isEmpty():
                event.wait()
            else:
                llist.pop()
                print("popped")
        return
                


thread = Thread(123)

cons = Consumer(thread)

cons.run()
prod = Producer(thread)
prod.run()

