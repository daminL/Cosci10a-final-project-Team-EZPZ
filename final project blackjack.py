import random
def checkyn(string):
    if string=='Yes' or "yes" or "No" or "no":
        return True
    else:
        return False
def checkhs(string):
    if string=='Hit' or string=='Stay' or string=="hit" or string=="stay":
        return True
    else:
        return False
def check510(integer):
    if integer=="5" or integer=="10":
        return False
    return True
def check1stseat(firstseat, player, player2):
    if firstseat==player or firstseat==player2:
        return True
    else:
        return False
player1balance = 20
player2balance = 20
anothergame = "Yes"
player1 = input("Hello!, What is your name?: ")
print("Welcome {}! Now find a friend to play with!".format(player1))
player2 = input("Hello!, What is your name?: ")
print("Welcome {}! Let's play blackjack!".format(player2))
check=True
while check:
    rules = input("Do you know how to play? (Yes/No): ")
    if checkyn(rules):
        check=False
    else:
        check=True
    if rules == "No" or rules=="no":
        print("-"*40)
        print("Okay! The rules are simple. You'll receive two cards in your hand, as will {}, and the dealer. \n"
              "Your goal is to beat the dealer by getting as close to 21 as possible without going over it.  \n"
              "Cards 2 - 10 counts as it's own number and the face cards jacks, queens, and kings counts as 10 each, and aces can count\n"
              " as either 1 or 11. A tie is a push, Getting a Blackjack a Ten or other facecard and an Ace earns you twice your bet\n"
              "The dealer must hit on any number below 17 and stick to all numbers greater than or equal to it\n"
              "if you have two of the same card in your opening hand you may split, that is create two hands with your starting hand"
              "but to do this you must place double your wager, and each hand is now worth half of your total wager".format(player2))
        print("-" * 40)
        print("Let's begin blackjack!")
        print("-" * 40)
    else:
        print("-"* 40)
        print("Let's begin blackjack!")
        print("-" * 40)
    check=True
    while check:
        firstseat = input("Who's up first? {} or {}? ".format(player1, player2))
        if check1stseat(firstseat, player1, player2):
            check=False
        else:
            print("invalid entry")
            check=True
    if firstseat == player1:
        secondseat = player2
    else:
        secondseat = player1
while anothergame == "Yes" and (player1balance and player2balance > 0):
    deck = [ {"card": "Ace","suit": "Hearts","value": 11},  {"card": "Two","suit": "Hearts","value": 2}, {"card": "Three","suit": "Hearts","value": 3}, {"card": "Four","suit": "Hearts","value": 4}, {"card": "Five","suit": "Hearts","value": 5}, {"card": "Six","suit": "Hearts","value": 6}, {"card": "Seven","suit": "Hearts","value": 7}, {"card": "Eight","suit": "Hearts","value": 8}, {"card": "Nine","suit": "Hearts","value": 9}, {"card": "Ten","suit": "Hearts","value": 10}, {"card": "Jack","suit": "Hearts","value": 10}, {"card": "Queen","suit": "Hearts","value": 10}, {"card": "King","suit": "Hearts","value": 10}, {"card": "Ace","suit": "Diamonds", "value": 11}, {"card": "Two",                 "suit": "Diamonds",                 "value": 2},   {"card": "Three",                 "suit": "Diamonds",                 "value": 3}, {"card": "Four",                 "suit": "Diamonds",                 "value": 4},  {"card": "Five",                 "suit": "Diamonds",                 "value": 5},   {"card": "Six",                 "suit": "Diamonds",                 "value": 6},    {"card": "Seven",                 "suit": "Diamonds",                 "value": 7},    {"card": "Eight",                 "suit": "Diamonds",                 "value": 8},  {"card": "Nine",                 "suit": "Diamonds",                 "value": 9},  {"card": "Ten",                 "suit": "Diamonds",                 "value": 10},   {"card": "Jack",                 "suit": "Diamonds",                 "value": 10},          {"card": "Queen",                 "suit": "Diamonds",                 "value": 10},          {"card": "King",                 "suit": "Diamonds",                 "value": 10},      {"card": "Ace",                 "suit": "Spades",                 "value": 11},         {"card": "Two",                 "suit": "Spades",                 "value": 2},            {"card": "Three",                 "suit": "Spades",                 "value": 3},        {"card": "Four",                 "suit": "Spades",                 "value": 4},      {"card": "Five",                 "suit": "Spades",                 "value": 5},    {"card": "Six",                 "suit": "Spades",                 "value": 6},  {"card": "Seven",                 "suit": "Spades",                 "value": 7},   {"card": "Eight",                 "suit": "Spades",                 "value": 8},    {"card": "Nine",                 "suit": "Spades",                 "value": 9},  {"card": "Ten",                 "suit": "Spades",                 "value": 10},    {"card": "Jack",                 "suit": "Spades",                 "value": 10},    {"card": "Queen",                 "suit": "Spades",                 "value": 10}, {"card": "King",                 "suit": "Spades",                 "value": 10},  {"card": "Ace",                 "suit": "Clubs",                 "value": 11},     {"card": "Two",                 "suit": "Clubs",                 "value": 2},       {"card": "Three",                 "suit": "Clubs",                 "value": 3},       {"card": "Four",                 "suit": "Clubs",                 "value": 4},       {"card": "Five",                 "suit": "Clubs",                 "value": 5},      {"card": "Six",                 "suit": "Clubs",                 "value": 6},    {"card": "Seven",                 "suit": "Clubs",                 "value": 7},   {"card": "Eight",                 "suit": "Clubs",                 "value": 8},     {"card": "Nine",                 "suit": "Clubs",                 "value": 9},    {"card": "Ten",                 "suit": "Clubs",                 "value": 10},       {"card": "Jack",                 "suit": "Clubs",                 "value": 10},    {"card": "Queen",                 "suit": "Clubs",                 "value": 10},  {"card": "King",                 "suit": "Clubs",                 "value": 10}]
    "wager"
    stay=0
    hand=[]
    hand1=[]
    hand2=[]
    hand22=[]
    dhand=[]
    handsize1=1
    handsize2=1
    player1blackjack=0
    player1blackjack1=0
    player2blackjack=0
    player2blackjack2=0
    dealerblackjack=0
    bust=0
    bust1=0
    bust2=0
    bust22=0
    dbust=0
    split=0
    handtotal=0
    handtotal1=0
    handtotal2=0
    handtotal22=0
    dhandtotal=0
    check=True
    while check:
        wager =input(firstseat+" Would you like to bet 5 or 10 dollars? Your balance is {} dollars. (5/10): ".format(player1balance))
        print("---------------------------------------------------------")
        wager2 = input(secondseat+" Would you like to bet 5 or 10 dollars? Your balance is {} dollars. (5/10): ".format(player2balance))
        if check510(wager) or check510(wager2):
            check=True
            print("One of you entered an invalid wager please bet 5 or 10 dollars")
        else:
            check=False
    print("Good luck, {}. You place {} dollars on the table. You have a {} dollar remaining.\n"
          .format(firstseat, wager, player1balance - int(wager)))
    print("Good luck, {}. You place {} dollars on the table. You have a {} dollar remaining.\n"
          .format(secondseat, wager2, player2balance - int(wager2)))
    cardk1 = random.choice(deck)
    deck.remove(cardk1)
    cardk2 = random.choice(deck)
    deck.remove(cardk2)
    cardk3 = random.choice(deck)
    deck.remove(cardk3)
    dhand.append(cardk3)
    cardk4 = random.choice(deck)
    deck.remove(cardk4)
    cardk5 = random.choice(deck)
    deck.remove(cardk5)
    cardk6 = random.choice(deck)
    deck.remove(cardk6)
    dhand.append(cardk6)
    split="no"
    print("The dealer is showing a "+dhand[1]['card'] +" of " +dhand[1]['suit'])
    print(secondseat+" is showing a "+cardk2['card'] +" of " +cardk2['suit']+" and a "+cardk5['card'] +" of " +cardk5['suit'])
    if cardk1['card']==cardk4['card']:
        check=True
        print("Your cards are the " +cardk1['card'] +" of " +cardk1['suit']+" and the " +cardk4['card'] +" of " +cardk4['suit'])
    while check:
        split=input("Would you like to split?: (Yes/No): ")
        if checkyn(split):
            check=False
        else:
            print("invalid input")
            check=True
    if split=="Yes"or split=="yes":
        print("Good luck, {}. You place {} dollars on the table. You have a {} dollar remaining.\n" .format(firstseat, wager, player1balance - 2*int(wager)))
        handsize1=2
        cardk7 = random.choice(deck)
        deck.remove(cardk7)
        cardk8 = random.choice(deck)
        deck.remove(cardk8)
        hand.append(cardk1)
        hand.append(cardk7)
        hand1.append(cardk4)
        hand1.append(cardk8)
    else: 
        hand.append(cardk1)
        hand.append(cardk4)
        'print("bwah311")'
    ace=0
    face=0
    for card in hand1:
        if card['card']=="Ace":
            ace=1
        if card['card']=="King" or "Queen" or "Jack" or "Ten":
            face=1
    if ace==face==1: 
        player1blackjack1=1
    ace=0
    face=0
    for card in hand:
        if card['card']=="Ace":
            ace=1
        if card['card']=="King" or "Queen" or "Jack" or "Ten":
            face=1
    if ace==face==1: 
        player1blackjack=1
    ace=0
    face=0
    if player1blackjack==1:
        print(firstseat+" got a Blackjack")
    if player1blackjack1==1:
        print(firstseat+"'s second hand got a Blackjack")
    while (player1blackjack<1 and handsize1<2) or ((player1blackjack<1 or player1blackjack1<1) and handsize1>1):
        'print("bwah111")'
        hand_total=0
        hand_total1=0
        print(firstseat+" has...")
        for card in hand:
            print(" the " +card['card'] +" of "+ card['suit'])
        aces=0
        while hand_total<(21+aces*10):
            'print(str(aces))'
            print("--------------------------")
            hand_total=0
            aces=0
            for card in hand:
                if card['card']=="Ace":
                    aces+=1
                hand_total+=card['value']
            if hand_total>21 and aces>0:
                hand_total+=-10
            if hand_total>21 and aces>1:
                hand_total+=-10
            if hand_total>21 and aces>2:
                hand_total+=-10
            if hand_total>21 and aces>3:
                hand_total+=-10
            print(firstseat+" your total is " +str(hand_total))
            if hand_total==21:
                break
            if hand_total>21:
                break
            check=True
            while check:
                hit_stay = input(firstseat+", Hit or Stay? (Hit/Stay): ")
                if checkhs(hit_stay):
                    check=False
                else:
                    check=True
            if hit_stay == "Hit":
                cardk = random.choice(deck)
                deck.remove(cardk)
                hand.append(cardk)
                print(firstseat+" drew the " +cardk['card']+" of "+cardk['suit'])
            else:
                break
        if handsize1>1 and player1blackjack1==0:
            print(firstseat+" you have...")
            for card in hand1:
                print(" the " +card['card'] +" of "+ card['suit'])
            aces=0
            while hand_total1<(21+aces*10):
                hand_total1=0
                aces=0
                for card in hand1:
                    if card['card']=="Ace":
                        aces+=1
                    hand_total1+=card['value']
                if hand_total1>21 and aces>0:
                    hand_total1+=-10
                if hand_total1>21 and aces>1:
                    hand_total1+=-10
                if hand_total1>21 and aces>2:
                    hand_total1+=-10
                if hand_total1>21 and aces>3:
                    hand_total1+=-10
                print(firstseat+" Your total is " +str(hand_total1))
                if hand_total1==21:
                    break
                if hand_total1>21:
                    break
                check=True
                while check:
                    hit_stay = input(firstseat+", Hit or Stay? (Hit/Stay): ")
                    if checkhs(hit_stay):
                        check=False
                    else:
                        check=True
                if hit_stay == "Hit" or hit_stay == "hit":
                    cardk = random.choice(deck)
                    deck.remove(cardk)
                    hand1.append(cardk)
                    print(firstseat+" drew the " +cardk['card']+" of "+cardk['suit'])
                else:
                    break
        if handsize1 >1:
            print(firstseat+ " hand is worth "+str(hand_total1))
        break
    if handsize1==1:
        hand_total1=0
    if player1blackjack==1:
        hand_total=21
    if player1blackjack1==1:
        hand_total1=21
    if hand_total>21:
        print("You busted")
        bust=1
    if hand_total==21:
        print("Nice job "+firstseat+" you ended with 21 the best you can get!")
    elif hand_total<21:
        print(firstseat +" You stayed on "+str(hand_total))
    finalfirsthand=hand_total
    if hand_total1>21 and handsize1 >1:
        print("You busted"+ firstseat+"!")
        bust1=1
    if hand_total1==21 and handsize1>1:
        print("Nice job "+firstseat+", you ended with 21 the best you can get!")
    elif hand_total1<21 and handsize1>1:
        print("You stayed on "+str(hand_total1))
    finalfirsthand1=hand_total1
    print("---------------------------------------------")
    
    
    
    
    
    
    
    
    
    
    
    print(secondseat+"'s Turn")
    split="no"
    print("The dealer is showing a "+cardk6['card'] +" of " +cardk6['suit'])
    print(firstseat+" has...")
    for card in hand:
        print("the "+card['card']+" of "+card['suit'])
    if handsize1>1:
        for card in hand1:
            print("the "+card['card']+" of "+card['suit'])
    split="no"
    if cardk2['card']==cardk5['card']:
        print(secondseat +"Your cards are the " +cardk2['card'] +" of " +cardk2['suit']+" and the " +cardk5['card'] +" of " +cardk5['suit'])
        check=True
    while check:
        split=input(secondseat+" Would you like to split?: (Yes/No): ")
        if checkyn(split):
            check=False
        else:
            print("invalid input")
            check=True
    if split=="Yes" or "yes":
        print("Good luck, {}. You place {} dollars on the table. You have a {} dollar remaining.\n" .format(secondseat, wager2, player2balance - 2*int(wager2)))
        handsize2=2
        cardk9 = random.choice(deck)
        deck.remove(cardk9)
        cardk10 = random.choice(deck)
        deck.remove(cardk10)
        hand2.append(cardk2)
        hand2.append(cardk9)
        hand22.append(cardk5)
        hand22.append(cardk10)
    else: 
        hand2.append(cardk2)
        hand2.append(cardk5)
        'print("bwah311")'
    ace=0
    face=0
    for card in hand2:
        if card['card']=="Ace":
            ace=1
        if card['card']=="King" or "Queen" or "Jack" or "Ten":
            face=1
    if ace==face==1: 
        player2blackjack=1
    ace=0
    face=0
    for card in hand22:
        if card['card']=="Ace":
            ace=1
        if card['card']=="King" or "Queen" or "Jack" or "Ten":
            face=1
    if ace==face==1: 
        player2blackjack2=1
    if player2blackjack==1:
        print(secondseat+" got a Blackjack")
    if player2blackjack2==1:
        print(secondseat+"'s second hand got a Blackjack")
    while (player2blackjack<1 and handsize2<2) or ((player2blackjack<1 or player2blackjack2<1) and handsize2>1):
        'print("bwah111")'
        hand_total2=0
        hand_total22=0
        print(secondseat+" has...")
        for card in hand2:
            print(" the " +card['card'] +" of "+ card['suit'])
        aces=0
        while hand_total2<21+aces*10:
            print("-------------------------------")
            hand_total2=0
            aces=0
            for card in hand2:
                if card['card']=="Ace":
                    aces+=1
                hand_total2+=card['value']
            if hand_total2>21 and aces>0:
                hand_total2+=-10
            if hand_total2>21 and aces>1:
                hand_total2+=-10
            if hand_total2>21 and aces>2:
                hand_total2+=-10
            if hand_total2>21 and aces>3:
                hand_total2+=-10
            print(secondseat+" your total is " +str(hand_total2))
            if hand_total2==21:
                break
            if hand_total2>21:
                break
            check=True
            while check:
                hit_stay = input(secondseat+", Hit or Stay? (Hit/Stay): ")
                if checkhs(hit_stay):
                    check=False
                else:
                    check=True
            if hit_stay == "Hit":
                cardk = random.choice(deck)
                deck.remove(cardk)
                hand2.append(cardk)
                print(secondseat+" You drew the " +cardk['card']+" of "+cardk['suit'])
            else:
                break
        if handsize2>1:
            print(secondseat+" You have...")
            for card in hand22:
                print(" the " +card['card'] +" of "+ card['suit'])
            aces=0
            while hand_total22<21+aces*10:
                print("-------------------------------")
                hand_total22=0
                aces=0
                for card in hand22:
                    if card['card']=="Ace":
                        aces+=1
                    hand_total22+=card['value']
                if hand_total22>21 and aces>0:
                    hand_total22+=-10
                if hand_total22>21 and aces>1:
                    hand_total22+=-10
                if hand_total22>21 and aces>2:
                    hand_total22+=-10
                if hand_total22>21 and aces>3:
                    hand_total22+=-10
                print(secondseat+" Your total is " +str(hand_total22))
                if hand_total22==21:
                    break
                if hand_total22>21:
                    break
                check=True
                while check:
                    hit_stay = input(secondseat+", Hit or Stay? (Hit/Stay): ")
                    if checkhs(hit_stay):
                        check=False
                    else:
                        check=True
                if hit_stay == "Hit" or hit_stay=="hit":
                    cardk = random.choice(deck)
                    deck.remove(cardk)
                    hand22.append(cardk)
                    print(secondseat+" You drew the " +cardk['card']+" of "+cardk['suit'])
                else:
                    break
        if handsize2 >1:
            print(secondseat+" Your hand is worth "+str(hand_total1))
        break
    aces=0
    hand_total2=0
    for card in hand2:
        if card['card']=="Ace":
            aces+=1
        hand_total2+=card['value']
    if hand_total2>21 and aces>0:
        hand_total2+=-10
    if hand_total2>21 and aces>1:
        hand_total2+=-10
    if hand_total2>21 and aces>2:
        hand_total2+=-10
    if hand_total2>21 and aces>3:
        hand_total2+=-10
    aces=0
    hand_total22=0
    for card in hand22:
        if card['card']=="Ace":
            aces+=1
        hand_total22+=card['value']
    if hand_total22>21 and aces>0:
        hand_total22+=-10
    if hand_total22>21 and aces>1:
        hand_total22+=-10
    if hand_total22>21 and aces>2:
        hand_total22+=-10
    if hand_total22>21 and aces>3:
        hand_total22+=-10
    if player2blackjack==1:
        hand_total2=21
    if player2blackjack2==1:
        hand_total22=21
    if handsize2==1:
        hand_total22=0
    if hand_total2>21:
        print(secondseat+" You busted!")
        bust2=1
    if hand_total2==21:
        print("Nice job "+secondseat+" you ended with 21 the best you can get!")
    elif hand_total2<21:
        print(secondseat+" You stayed on "+str(hand_total2))
    if hand_total22>21 and handsize1 >1:
        print(secondseat+" You busted!")
        bust22=1
    if hand_total22==21 and handsize1>1:
        print("Nice job "+secondseat+" you ended with 21 the best you can get!")
    elif hand_total22<21 and handsize1>1:
        print(secondseat+" You stayed on "+str(hand_total22))
    finalhandtotal2=hand_total2
    finalhandtotal22=hand_total22
    "Dealers Turn"
    ace=0
    face=0
    for card in dhand:
        if card['card']=="Ace":
            ace=1
        if card['card']=="King" or "Queen" or "Jack" or "Ten":
            face=1
    if ace==1 and face==1: 
        dealerblackjack=1
    print("The Dealer has a " +cardk3['card']+" of "+cardk3['suit']+" and a " +cardk6['card']+" of "+cardk6['suit'])
    dhandtotal=0
    for card in dhand:
        dhandtotal+=card['value']
        
    while dhandtotal<17:
        dhandtotal=0
        aces=0
        for card in dhand:
            if card['card']=="Ace":
                aces+=1
            dhandtotal+=card['value']
        if dhandtotal>21 and aces>0:
            dhandtotal+=-10
        if dhandtotal>21 and aces>1:
            dhandtotal+=-10
        if dhandtotal>21 and aces>2:
            dhandtotal+=-10
        if dhandtotal>21 and aces>3:
            dhandtotal+=-10
        cardk = random.choice(deck)
        deck.remove(cardk)
        dhand.append(cardk)
        print("The Dealer drew a "+ cardk['card']+" of "+cardk['suit'])
        for card in dhand:
            dhandtotal+=card['value']
    for card in dhand:
        if card['card']=="Ace":
            aces+=1
    if dhandtotal>21 and aces>0:
        dhandtotal+=-10
    if dhandtotal>21 and aces>1:
        dhandtotal+=-10
    if dhandtotal>21 and aces>2:
        dhandtotal+=-10
    if dhandtotal>21 and aces>3:
        dhandtotal+=-10
    if dhandtotal>21:
        print("The Dealer Busted!")
        dbust=1
        dhandtotal=0
    print("The dealer ended on "+str(dhandtotal))
    print("-" * 40)
    "Results player 1"
    if bust==0:
        if player1blackjack==0 and dealerblackjack==0:
            if finalfirsthand > dhandtotal:
                player1balance+=int(wager)
                print(str(finalfirsthand)+" vs "+ str(dhandtotal))
                print("Congratulations "+firstseat+", you won "+wager+" dollars")
            elif finalfirsthand < dhandtotal and dbust==0:
                player1balance+=-int(wager)
                print(str(finalfirsthand)+" vs "+ str(dhandtotal))
                print("Unfortunately "+firstseat+", you lost "+wager+" dollars")
            elif finalfirsthand==dhandtotal:
                print(str(finalfirsthand)+" vs "+ str(dhandtotal))
                print(firstseat+", you and the dealer tied, you lost no money")
        if player1blackjack==1 and dealerblackjack==0:
            player1balance+=2*int(wager)
            print("Congratulations "+firstseat+", you won "+str(2*int(wager))+" dollars by getting a Blackjack")
        if player1blackjack==0 and dealerblackjack==1:
            player1balance+=-int(wager)
            print("Unfortunately "+firstseat+", you lost "+wager+" dollars, because of the dealers Blackjack")
    elif bust==1:
        player1balance+=-int(wager)
        print("Unfortunately "+firstseat+", you busted and lost "+wager+" dollars")
    if bust1==0 and handsize1>1:
        if player1blackjack1==0 and dealerblackjack==0 and handsize1>1:
            if finalfirsthand1 > dhandtotal or dbust==1:
                player1balance+=int(wager)
                print(str(finalfirsthand1)+" vs "+ str(dhandtotal))
                print("Congratulations "+firstseat+", you won "+wager+" dollars")
            elif finalfirsthand1 < dhandtotal and dbust==0:
                player1balance+=-int(wager)
                print(str(finalfirsthand1)+" vs "+ str(dhandtotal))
                print("Unfortunately "+firstseat+", you lost "+wager+" dollars")
            elif finalfirsthand1==dhandtotal:
                print(str(finalfirsthand1)+" vs "+ str(dhandtotal))
                print(firstseat+", you and the dealer tied, you lost no money")
        if player1blackjack1==1 and dealerblackjack==0 and handsize1>1:
            player1balance+=2*int(wager)
            print("Congratulations "+firstseat+", you won "+str(2*int(wager))+" dollars by getting a Blackjack")
        if player1blackjack1==0 and dealerblackjack==1 and handsize1>1:
            player1balance+=-int(wager)
            print("Unfortunately "+firstseat+", you lost "+wager+" dollars, because of the dealers Blackjack")
    elif bust1==1:
        player1balance+=-int(wager)
        print("Unfortunately "+firstseat+", you busted and lost "+wager+" dollars")
    print("----------------------------------------------------")
    "Results Player 2"
    if bust2==0:
        if player2blackjack==0 and dealerblackjack==0:
            if finalhandtotal2 > dhandtotal:
                player2balance+=int(wager2)
                print(str(finalhandtotal2)+" vs "+ str(dhandtotal))
                print("Congratulations "+secondseat+", you won "+wager2+" dollars")
            elif finalhandtotal2 < dhandtotal and dbust==0:
                player2balance+=-int(wager2)
                print(str(finalhandtotal2)+" vs "+ str(dhandtotal))
                print("Unfortunately "+secondseat+", you lost "+wager2+" dollars")
            elif finalhandtotal2==dhandtotal:
                print(str(finalhandtotal2)+" vs "+ str(dhandtotal))
                print(secondseat+", you and the dealer tied, you lost no money")
        if player2blackjack==1 and dealerblackjack==0:
            player2balance+=2*int(wager2)
            print("Congratulations "+secondseat+", you won "+str(2*int(wager2))+" dollars by getting a Blackjack")
        if player2blackjack==0 and dealerblackjack==1:
            player2balance+=-int(wager2)
            print("Unfortunately "+secondseat+", you lost "+wager2+" dollars, because of the dealers Blackjack")
    elif bust2==1: 
        player2balance+=-int(wager2)
        print("Unfortunately "+secondseat+", you busted and lost "+wager2+" dollars")
    if bust22==0 and handsize2>1:
        if player2blackjack2==0 and dealerblackjack==0 and handsize2>1:
            if finalhandtotal22 > dhandtotal or dbust==1:
                player2balance+=int(wager2)
                print(str(finalhandtotal22)+" vs "+ str(dhandtotal))
                print("Congratulations "+secondseat+", you won "+wager2+" dollars")
            elif finalhandtotal22 < dhandtotal and dbust==0:
                player2balance+=-int(wager2)
                print(str(finalhandtotal22)+" vs "+ str(dhandtotal))
                print("Unfortunately "+secondseat+", you lost "+wager2+" dollars")
            else:
                print(str(finalhandtotal22)+" vs "+ str(dhandtotal))
                print(secondseat+", you and the dealer tied, you lost no money")
        if player2blackjack2==1 and dealerblackjack==0 and handsize2>1:
            player2balance+=2*int(wager2)
            print("Congratulations "+secondseat+", you won "+str(2*int(wager2))+" dollars by getting a Blackjack")
        if player2blackjack2==0 and dealerblackjack==1 and handsize2>1:
            player2balance+=-int(wager2)
            print("Unfortunately "+secondseat+", you lost "+wager2+" dollars, because of the dealers Blackjack")
    elif bust22==1 and handsize2>1:
        player2balance+=-int(wager2)
        print("Unfortunately "+secondseat+", you busted and lost "+wager2+" dollars")
    elif bust1==1:
        player1balance+=-int(wager)
        print("Unfortunately "+firstseat+", you busted and lost "+wager+" dollars")
    check=True
    while check:
        anothergame = input(
                "Would you like to play another round? {}'s remaining balance is {} and {}'s remaning balance is {}. (Yes/No) ".format(
                        firstseat, player1balance, secondseat, player2balance))
        if checkyn(anothergame):
            check=False
        else:
            check=True
    if anothergame == "No" or anothergame=="no":
        print("Thanks for playing! Stay safe out there!")
    if anothergame == "yes":
        anothergame="Yes"
if player1balance<=0 or player2balance<=0:
    print("One of you lost, Thanks for playing! Stay safe out there!")
