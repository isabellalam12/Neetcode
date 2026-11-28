class StockSpanner:

    def __init__(self):
        self.stack = [] # elements: (price, span)
        

    def next(self, price: int) -> int:
        # initialize span to 1
        span = 1
        # loop down stack until an element's price is > price 
        while self.stack and self.stack[-1][0] <= price: 
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
  

        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)