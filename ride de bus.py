from random import randint
#random card, duh
def random_card(cur_deck):
    global card
    card=cur_deck.pop(randint(0,len(cur_deck)-1))
    return card
deck=["2ч","3ч","4ч","5ч","6ч","7ч","8ч","9ч","9+1ч","Вч","Дч","Кч","Тч",
      "2б","3б","4б","5б","6б","7б","8б","9б","9+1б","Вб","Дб","Кб","Тб",
      "2п","3п","4п","5п","6п","7п","8п","9п","9+1п","Вп","Дп","Кп","Тп",
      "2к","3к","4к","5к","6к","7к","8к","9к","9+1к","Вк","Дк","Кк","Тк"]
def ride_the_bus(balance):
    bet=int(input(f"balance is {balance}, enter bet amount: "))
    if bet>balance:
        print("who do you think you're trying to scam, scram smarty-pants")
        return balance
    cur_deck=deck.copy()
    #round 1
    ans=input("choose the color, к(расный) or ч(ёрный): ")
    random_card(cur_deck)
    #game
    print(card)
    if (ans=="к" and (card[1]=="ч" or card[1]=="б")) or (ans=="ч" and (card[1]=="п" or card[1]=="к")):
       pass
    else:
        print(f"{bet} lost")
        return balance-bet
    #round 2
    ans=input("choose, в(ыше) or н(иже), or you can ф(орфит): ")
    first_card=card
    random_card(cur_deck)
    print(card)
    if ans=="ф":
        print(f"{bet*2} win")
        return balance+bet
    #game
    if (ans=="в" and first_card[:1]<=card[:1]) or (ans=="н" and first_card[:1]>card[:1]):
        pass
    else:
        print(f"{bet} lost")
        return balance-bet
    #round 3
    ans=input("choose, в(нутри) or с(наружи), or you can ф(орфит): ")
    second_card=card
    random_card(cur_deck)
    print(card)
    if ans=="ф":
        print(f"{bet*3} win")
        return balance+(bet*2)
    #game
    lower_card,higher_card=sorted([first_card,second_card])
    if (ans=="в" and (lower_card<=card and card<higher_card)) or (ans=="с" and (card>lower_card or higher_card<=card)):
        pass
    else:
        print(f"{bet} lost")
        return balance-bet
    #round 4
    ans=input("choose the suit of the next card (ч,б,п,к) or ф(орфит): ")
    third_card=card
    random_card(cur_deck)
    print(card)
    if ans=="ф":
        print(f"{bet*4} win")
        return balance+(bet*3)
    #game
    if ans in card:
        print(f"{bet*20} win")
        return balance+(bet*19)
    else:
        print(f"{bet} lost")
        return balance-bet
balance=10000
starting_balance=balance
while True:
    balance=ride_the_bus(balance)
    if balance<=0:
        print("yeah, you're poor, skidadle")
        break
print(f"total balance: {balance}\nprofit: {balance-starting_balance}")