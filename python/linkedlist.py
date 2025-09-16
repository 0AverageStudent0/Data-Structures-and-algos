class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,head=None):
        self.head = head
    
    def insertinstart(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        self.head = node
        self.head.next = temp
    
    def insertinend(self,data):
        temp = self.head
        if self.head is None:
            self.head = Node(data)
            return
        while temp.next:
            temp = temp.next
        temp.next = Node(data)
    
    def printll(self):
        temp = self.head
        while temp:
            print(temp.data,end="-->")
            temp = temp.next
        print()
    
    def removefromstart(self):
        if self.head is None:
            print("list is empty")
            return
        self.head = self.head.next
    
    def removefromend(self):
        if self.head is None:
            print("empty srting")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head.next
        while temp.next.next:
            temp = temp.next
        temp.next = None
    
    def removeposition(self,position):
        if self.head is None:
            print("empty list")
            return
        if position == 0:
            self.head = self.head.next
            return
        count = 0
        temp = self.head
        while count < position-1 and temp is not None:
            temp = temp.next
            count += 1
        if temp is None or temp.next is None:
            print("invalid posistion")
            return
        temp.next = temp.next.next
    def countnode(self):
        count = 0
        temp = self.head
        while temp:
            temp = temp.next
            count += 1
        print(count)
    
    def searchelement(self,ele):
        position  = 0
        temp = self.head
        while temp:
            if temp.data == ele:
                print(position)
                return
            temp = temp.next
            position += 1
        print("element not found")


l1 = LinkedList()
l1.insertinend(10)
l1.insertinend(20)
l1.insertinend(30)
l1.insertinend(40)
l1.printll()            # 10 --> 20 --> 30 --> 40 -->

l1.removeposition(2)
l1.printll() 
l1.countnode()    
