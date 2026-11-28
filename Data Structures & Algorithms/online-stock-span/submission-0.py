class StockSpanner:

    def __init__(self):
        self.stack = [] # elements: (price)
        

    def next(self, price: int) -> int:
        # initialize counter to 1
        counter = 0
        self.stack.append(price)

        # iterate backwards to stack 
        for i in range(len(self.stack)): 
            temp = self.stack[-(i+1)]
            # increment counter if price >= current stack element 
            if price >= temp: 
                counter += 1
            else:  # break if price < current stack element 
                break
        return counter

        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)