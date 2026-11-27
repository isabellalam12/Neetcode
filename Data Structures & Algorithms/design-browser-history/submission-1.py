class Tab: 
    def __init__(self, url: str):
        self.val = url 
        self.next = None 
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = Tab(homepage)
        self.head = Tab("")
        self.tail = Tab("")
        self.home.prev = self.head
        self.home.next = self.tail
        self.head.next = self.home 
        self.tail.prev = self.home 
        self.curr = self.home
        
    def visit(self, url: str) -> None:
        temp = Tab(url)
        self.curr.next = temp 
        self.tail.prev = temp 
        temp.next = self.tail 
        temp.prev = self.curr
        self.curr = temp 

    def back(self, steps: int) -> str:
        while self.curr.prev != self.head: 
            if steps == 0:
                return self.curr.val
            self.curr = self.curr.prev 
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while self.curr.next != self.tail: 
            if steps == 0:
                return self.curr.val
            self.curr = self.curr.next 
            steps -= 1
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)