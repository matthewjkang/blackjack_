import random
from deck import cards
from classes import Hand
from time import sleep

def play():
    print("""
888888b.   888                   888       d8b                   888      
888  "88b  888                   888       Y8P                   888      
888  .88P  888                   888                             888      
8888888K.  888  8888b.   .d8888b 888  888 8888  8888b.   .d8888b 888  888 
888  "Y88b 888     "88b d88P"    888 .88P "888     "88b d88P"    888 .88P 
888    888 888 .d888888 888      888888K   888 .d888888 888      888888K  
888   d88P 888 888  888 Y88b.    888 "88b  888 888  888 Y88b.    888 "88b 
8888888P"  888 "Y888888  "Y8888P 888  888  888 "Y888888  "Y8888P 888  888 
                                           888                            
                                          d88P                            
                                        888P""")
    draw = random.sample(cards,4)
    player = Hand(draw[::2])
    dealer = Hand(draw[1::2])
    sleep(1)
    print('Drawing your cards ... \n \n')
    sleep(1.5)
    print(player.myhand[0][0],"\n"+player.myhand[1][0])
    print('TOTAL - ',player.total,'\n')
    stand = False
    while stand == False:
        response = input('Hit or Stand? ')
        print()
        sleep(0.75)
        if response.lower() == 'stand':
            while dealer.total < 16:
                dealer.hit()  
            print('The dealer has',dealer.total,'and you have',player.total,'\n')
            sleep(1)
            if dealer.total > 21:
                print('The Dealer busted. You win!!!')
            elif dealer.total>player.total: 
                print('You Lose')
            elif dealer.total == player.total:
                print('Push')
            else:
                print('You Win!!!')
            stand = True
        elif response.lower() == 'hit':
            player.hit()
            print('you drew',player.myhand[-1][0])
            print('TOTAL - ',player.total,'\n')
            if player.total > 21:
                print('You BUSTED! The Dealer Wins!!!')
                break
        else:
            print('invalid option')
    sleep(1)
    print("\n")

if __name__ == '__main__':
    play()

