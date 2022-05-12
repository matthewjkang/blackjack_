class Hand:
    def __init__(self,draw):
        self.first = draw[0]
        self.second = draw[1]
        self.firstval = self.first[1]
        self.secondval = self.second[1]

    def total(self):
        if type(self.firstval) == tuple:
            if self.secondval + 11 <= 21:
                self.firstval = 11
            else:
                self.firstval == 1
        if type(self.secondval) == tuple:
            if self.firstval + 11 <= 21:
                self.secondval = 11
            else:
                self.secondval == 1
        return self.firstval+self.secondval

    #TODO : IMPLEMENT A HIT METHOD

    #TODO : IMPLEMENT WIN CHECKER
    