class ListNode: 
    def __init__(self, val: int):
        self.val = val 
        self.next = None 
        self.prev = None 

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail 
        self.tail.prev = self.head 
        self.length = 0 
        
    def get(self, index: int) -> int: # 0 <--> 1 <--> 2
        if index >= self.length: 
            return -1 
        else: 
            curr = self.head.next
            while curr != None: 
                if index == 0: 
                    return curr.val 
                curr = curr.next
                index -= 1

        

    def addAtHead(self, val: int) -> None:
        temp = ListNode(val)
        post = self.head.next
        self.head.next = temp 
        post.prev = temp
        temp.prev = self.head
        temp.next = post 
        self.length += 1

    def addAtTail(self, val: int) -> None:
        temp = ListNode(val)
        tail_prev = self.tail.prev 
        self.tail.prev = temp 
        tail_prev.next = temp 
        temp.prev = tail_prev
        temp.next = self.tail
        self.length += 1 
    
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length: 
            return 
        curr = self.head.next
        while curr != None: 
            if index == 0: 
                temp = ListNode(val)
                curr_prev = curr.prev  
                curr_prev.next = temp 
                temp.next = curr
                temp.prev = curr_prev 
                curr.prev = temp 
                self.length += 1
            curr = curr.next
            index -= 1
    
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length: 
            return 
        elif index == self.length: 
            self.tail = self.tail.prev 
            self.tail.next = None 
            self.length -=1
        elif index == 0:
            self.head = self.head.next
        curr = self.head.next 
        while curr != None: 
            if index == 0: 
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                self.length -= 1
            curr = curr.next
            index -= 1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)