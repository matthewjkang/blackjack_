face = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
suits = ['Hearts','Diamonds','Clubs','Spades']
cardNames = [i+' of '+j for j in suits for i in face]
cards =  list(zip(cardNames,[11,2,3,4,5,6,7,8,9,10,10,10,10]*4))
