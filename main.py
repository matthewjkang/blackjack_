import random
from time import sleep
from deck import cards
from classes import Hand

def play():
    print('Now playing Blackjack')
    sleep(0.5)
    print('Drawing cards')
    sleep(1.5)
    draw = random.sample(cards,4)
    player = Hand(draw[::2])
    dealer = Hand(draw[1::2])
    print('Your hand:\n'+player.first[0],"\n"+player.second[0])
    sleep(0.5)
    print('Your total: ',player.total())
    sleep(0.5)

    stand = False
    playertotal = player.total()
    dealertotal = dealer.total()
    while stand == False:
        response = input('Hit or Stand?')
        if response.lower() == 'stand':
            while dealertotal < 16:
                dealerhit = random.sample(cards,1)[0]
                if type(dealerhit[1]) == tuple:
                    if dealertotal + 11 <= 21:
                        dealertotal += 11
                    else:
                        dealertotal += 1
                else:
                    dealertotal += dealerhit[1]      

            print('The dealer had',dealertotal)
            sleep(0.5)
            print('You had',playertotal)
            sleep(0.5)
            if dealertotal > 21:
                print('The Dealer busted')
                sleep(0.5)
                print('You Win')
                sleep(0.5)
            elif dealertotal>playertotal: 
                print('You Lose')
            elif dealertotal == playertotal:
                print('Push')
            else:
                print('You Win')
            stand = True
        elif response.lower() == 'hit':
            hit = random.sample(cards,1)[0]
            print('you drew',hit[0])
            sleep(0.5)
            if type(hit[1]) == tuple:
                if playertotal + 11 <= 21:
                    playertotal += 11
                else:
                    playertotal += 1
            else:
                playertotal += hit[1]
            print('your total is now',playertotal)
            if playertotal > 21:
                print('you BUSTED!')
                sleep(1.5)
                print('Dealer Wins')
                break
        else:
            print('invalid option')

if __name__ == '__main__':
    play()
