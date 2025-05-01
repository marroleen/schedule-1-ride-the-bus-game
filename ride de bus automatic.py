from random import randint
import matplotlib.pyplot as plt
ranks=["2","3","4","5","6","7","8","9","9+1","В","Д","К","Т"]
#hearts,diamonds,spades,clubs
suits={"ч","б","п","к"}
#create a deck
deck=[rank+suit for suit in suits for rank in ranks]
#random card, duh
def random_card(cur_deck):
    global card
    card=cur_deck.pop(randint(0,len(cur_deck)-1))
    return
#for defining amount of card between two drawn
def cards_range(card1,card2):
    rank1,rank2=card1[:-1],card2[:-1]
    i1,i2=ranks.index(rank1),ranks.index(rank2)
    return abs(i1-i2)
#the game itself
def ride_the_bus(balance,need_outputs):
    bet=round(balance*.043) if balance>235 else round(balance*.11)
    if balance>=235:
        bet=round(balance*.043)
        if bet>500:
            bet=500
        go_thru=True
    else:
        bet=round(balance*.11)
        if bet==0:
            return 0
        go_thru=False
    if need_outputs==True:
        print(f"ставка {bet}")
    # bet_history.append(bet)
    cur_deck=deck.copy()
    #round 1
    ans=("к","ч")[randint(0,1)]
    if need_outputs==True:
        print(f"round 1\nставка на {ans}")
    random_card(cur_deck)
    #game
    if need_outputs==True:
        print(card)
    if (ans=="к" and (card[-1]=="ч" or card[-1]=="б")) or (ans=="ч" and (card[-1]=="п" or card[-1]=="к")):
       if need_outputs==True:
        print("round 2")
    else:
        if need_outputs==True:
            print(f"{bet} lost")
        return balance-bet
    #round 2
    ans="в" if card[:1]<"9" else "н" if card[:1]>"9+1" else "ф"
    if need_outputs==True:
        print(f"ставка на {ans}")
    first_card=card
    random_card(cur_deck)
    if need_outputs==True:
        print(card)
    if ans=="ф":
        if need_outputs==True:
            print(f"{bet*2} win")
        return balance+bet
    #game
    if (ans=="в" and first_card[:1]<=card[:1]) or (ans=="н" and first_card[:1]>card[:1]):
        if need_outputs==True:
            print("round 3")
    else:
        if need_outputs==True:
            print(f"{bet} lost")
        return balance-bet
    #round 3
    cards_between=cards_range(first_card,card)
    ans="с" if cards_between<5 else "в" if cards_between>7 else "ф"
    if need_outputs==True:
        print(f"ставка на {ans}")
    second_card=card
    random_card(cur_deck)
    if need_outputs==True:
        print(card)
    if ans=="ф":
        if need_outputs==True:
            print(f"{bet*3} win")
        return balance+(bet*2)
    #game
    lower_card,higher_card=sorted([first_card,second_card])
    if (ans=="в" and (lower_card<=card and card<higher_card)) or (ans=="с" and (card>lower_card or higher_card<=card)):
        if need_outputs==True:
            print("round 4")
    else:
        if need_outputs==True:
            print(f"{bet} lost")
        return balance-bet
    #round 4
    suits_left=list(suits-{first_card[-1],second_card[-1],card[-1]})
    ans=suits_left[randint(0,len(suits_left)-1)] if go_thru==True else "ф"
    random_card(cur_deck)
    if need_outputs==True:
        print(card)
    #game
    if ans in card:
        if need_outputs==True:
            print(f"{bet*20} win")
        return balance+(bet*19)
    else:
        if need_outputs==True:
            print(f"{bet} lost")
        return balance-bet
for i in range(10):
    # balance=475 #first point in game when you have money
    balance=12000 #the first bet could be the highest possible
    need_output=False
    balance_history=[balance]
    # bet_history=[]
    starting_balance=balance
    for _ in range(1000):
        balance=ride_the_bus(balance,need_output)
        balance_history.append(balance)
        if balance<=0 or balance>=10000000:
            break
    # print(balance_history)
    # print(f"total balance: {balance}, profit: {balance-starting_balance}")
    plt.plot(balance_history)
    # plt.plot(bet_history)
plt.grid(True)
plt.show()