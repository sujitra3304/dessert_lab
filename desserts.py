"""Dessert classes."""


class Cupcake:
    cache = {}
    """A cupcake."""
    def __init__(self, name, flavor, price):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0
        
        if self.name not in self.cache:
            self.cache[self.name] = self
        # self.cache = {'self.name' =[self.flavor, self.price, self.qty]}
    
    def add_stock(self,amount):
        return self.qty + amount
    
    def sell(self,amount):
        
        if self.qty == 0:
            print ("Sorry, these cupcakes are sold out")
            while True:
                if self.qty - amount < 0:
                    print("We can't sell that many cupcakes, please choose a smaller amount")
                    break

    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'

strawberry_cp = Cupcake("strawberry cp", "strawberry", 5)


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
