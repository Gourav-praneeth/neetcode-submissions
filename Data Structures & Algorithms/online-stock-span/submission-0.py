class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        #self.stack.append(price)
        counter = 1

        while self.stack:
            previous_price = self.stack[-1][0]

            if previous_price <= price:
                previous_price, previous_counter = self.stack.pop()
                counter += previous_counter
            else:
                break

        self.stack.append((price, counter))

        return counter


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()  
# param_1 = obj.next(price)