class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Dlinkedlist:
    def __init__(self):
        self.head = None
    
    def insert_node_instart(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        
    def print_forward(self):
        temp = self.head
        while temp:
            print(temp.data,end="<->")
            temp= temp.next
        print()

    def print_backward(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data,end="<->")
            temp = temp.prev
        print()
    
    def del_head(self):
        if not self.head:
            return None
        temp = self.head
        if not temp.next:
            temp = None
            return None
        newhead = temp.next
        newhead.prev = None
        temp.next = None
        self.head = newhead
        return newhead
    
    def del_last(self):
        if not self.head:
            return None
        temp = self.head
        if not temp.next:
            self.head = None
            return None
        while temp.next:
            temp = temp.next
        back = temp.prev
        back.next = None
        temp.prev = None
        return self.head
    
    def del_kth(self,k):
        temp = self.head
        if not temp:
            temp = None
            return None
        cnt = 1
        while temp.next:
            cnt += 1
            if cnt == k:
                break
            temp = temp.next
        back = temp.prev
        front = temp.next
        if back == None:
            front.prev = None
            temp.next = None
            self.head  = front
            return self.head
        if front == None:
            back.next = None
            temp.prev = None
            return self.head
        back.next = front
        front.prev = back
        temp.next = None
        temp.prev = None
        return self.head


dll = Dlinkedlist()
dll.insert_node_instart(3)
dll.insert_node_instart(2)
dll.insert_node_instart(1)
dll.insert_at_end(4)
dll.insert_at_end(5)
dll.insert_at_end(6)
dll.print_forward()
dll.print_backward()
