class ProductOfNumbers:

    def __init__(self):
        self.a = []

    def add(self, num: int) -> None:
        self.a.append(num)

    def getProduct(self, k: int) -> int:
        prod = 1
        for x in self.a[-k:]:
            prod *= x
        return prod
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)