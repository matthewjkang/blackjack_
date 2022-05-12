from random import sample
from deck import cards

class Hand:
    def __init__(self,draw):
        self.myhand = draw
        self.firstval = draw[0][1]
        self.secondval = draw[1][1]
        if self.firstval == 11 and self.secondval == 11:
            self.total = 12
        else:
            self.total = self.firstval+self.secondval


    def hit(self):
        mytotal = self.total
        hitMe = sample(cards,1)[0]
        self.myhand.append(hitMe)
        hitval = hitMe[1]
        if hitval == 11 and mytotal > 10:
            hitval = 1
        else:
            mytotal+=hitval
        self.total += hitval
        return mytotal

