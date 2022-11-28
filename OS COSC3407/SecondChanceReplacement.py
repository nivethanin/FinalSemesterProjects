import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self

class CLL:
    def __init__(self):
        self.head = None
        self.count = 0
     
    def __repr__(self):
        string = ""
          
        if(self.head == None):
            string += "Circular Linked List Empty"
            return string
          
        string += f"Circular Linked List:\n{self.head.data}"      
        temp = self.head.next
        while(temp != self.head):
            string += f" -> {temp.data}"
            temp = temp.next
        return string
     
    def append(self, data):
        self.insert(data, self.count)
        return
     
    def insert(self, data, index):
        if (index > self.count) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")
             
        if self.head == None:
            self.head = Node(data)
            self.count += 1
            return
         
        temp = self.head
        for _ in range(self.count - 1 if index - 1 == -1 else index - 1):
            temp = temp.next
             
        aftertemp = temp.next #New node goes between temp and aftertemp
        temp.next = Node(data)
        temp.next.next = aftertemp
        if(index == 0):
            self.head = temp.next
        self.count += 1
        return
     
    def remove(self, index):
        if (index >= self.count) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")
         
        if self.count == 1:
            self.head = None
            self.count = 0
            return
         
        before = self.head
        for _ in range(self.count - 1 if index - 1 == -1 else index - 1):
            before = before.next
        after = before.next.next
         
        before.next = after
        if(index == 0):
            self.head = after
        self.count -= 1
        return
     
    def index(self, node: Node):
        temp = self.head
        for i in range(self.count):
            if(temp == node):
                return i
            temp = temp.next
        return print("Index Failure")
     
    def size(self):
        return self.count
     
    def display(self):
        print(self)

    def pickVictim(self, index):
        curr = self.head
        i=0

        while i != index:
            curr = curr.next
            i+=1
        
        self.handleVictim(curr, index)

    def handleVictim(self, curr: Node, orig):
        
        #Orig is original chosen index to make sure we don't loop our traversal
        if curr.data == 1:
            if self.index(curr.next) != orig:
                curr.data = 0
                self.handleVictim(curr.next, orig)
            else:
                print("You've reached original point!!")
                #It will warn you if you've reached original point
        
        elif curr.data == 0:
            curr.data = 1
            print(f'The location of the eventual victim was {self.index(curr)} and your chosen index was {orig}')
            self.display()


def main():
    cll = CLL()
    for _ in range(30):
        cll.append(random.randint(0,1))
    #Creates the circular linked list of 30 randomly placed 1s or 0s
    
    cll.display()
    #Prints out the list for the user

    cll.pickVictim(int(input("Pick your first victim: ")))

    cll.pickVictim(int(input("Pick your second victim: ")))

    cll.pickVictim(int(input("Pick your third victim: ")))
    

if __name__ == '__main__':
    main()





            