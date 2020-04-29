import random

player1balance = 20
player2balance = 20
anothergame = "Yes"
while anothergame == "Yes" and (player1balance and player2balance > 0):

    deck = {1: {"card": "Ace",
                "suit": "Hearts",
                "value": 11},
            2: {"card": "Two",
                "suit": "Hearts",
                "value": 2},
            3: {"card": "Three",
                "suit": "Hearts",
                "value": 3},
            4: {"card": "Four",
                "suit": "Hearts",
                "value": 4},
            5: {"card": "Five",
                "suit": "Hearts",
                "value": 5},
            6: {"card": "Six",
                "suit": "Hearts",
                "value": 6},
            7: {"card": "Seven",
                "suit": "Hearts",
                "value": 7},
            8: {"card": "Eight",
                "suit": "Hearts",
                "value": 8},
            9: {"card": "Nine",
                "suit": "Hearts",
                "value": 9},
            10: {"card": "Ten",
                 "suit": "Hearts",
                 "value": 10},
            11: {"card": "Jack",
                 "suit": "Hearts",
                 "value": 10},
            12: {"card": "Queen",
                 "suit": "Hearts",
                 "value": 10},
            13: {"card": "King",
                 "suit": "Hearts",
                 "value": 10},
            14: {"card": "Ace",
                 "suit": "Diamonds",
                 "value": 11},
            15: {"card": "Two",
                 "suit": "Diamonds",
                 "value": 2},
            16: {"card": "Three",
                 "suit": "Diamonds",
                 "value": 3},
            17: {"card": "Four",
                 "suit": "Diamonds",
                 "value": 4},
            18: {"card": "Five",
                 "suit": "Diamonds",
                 "value": 5},
            19: {"card": "Six",
                 "suit": "Diamonds",
                 "value": 6},
            20: {"card": "Seven",
                 "suit": "Diamonds",
                 "value": 7},
            21: {"card": "Eight",
                 "suit": "Diamonds",
                 "value": 8},
            22: {"card": "Nine",
                 "suit": "Diamonds",
                 "value": 9},
            23: {"card": "Ten",
                 "suit": "Diamonds",
                 "value": 10},
            24: {"card": "Jack",
                 "suit": "Diamonds",
                 "value": 10},
            25: {"card": "Queen",
                 "suit": "Diamonds",
                 "value": 10},
            26: {"card": "King",
                 "suit": "Diamonds",
                 "value": 10},
            27: {"card": "Ace",
                 "suit": "Spades",
                 "value": 11},
            28: {"card": "Two",
                 "suit": "Spades",
                 "value": 2},
            29: {"card": "Three",
                 "suit": "Spades",
                 "value": 3},
            30: {"card": "Four",
                 "suit": "Spades",
                 "value": 4},
            31: {"card": "Five",
                 "suit": "Spades",
                 "value": 5},
            32: {"card": "Six",
                 "suit": "Spades",
                 "value": 6},
            33: {"card": "Seven",
                 "suit": "Spades",
                 "value": 7},
            34: {"card": "Eight",
                 "suit": "Spades",
                 "value": 8},
            35: {"card": "Nine",
                 "suit": "Spades",
                 "value": 9},
            36: {"card": "Ten",
                 "suit": "Spades",
                 "value": 10},
            37: {"card": "Jack",
                 "suit": "Spades",
                 "value": 10},
            38: {"card": "Queen",
                 "suit": "Spades",
                 "value": 10},
            39: {"card": "King",
                 "suit": "Spades",
                 "value": 10},
            40: {"card": "Ace",
                 "suit": "Clubs",
                 "value": 11},
            41: {"card": "Two",
                 "suit": "Clubs",
                 "value": 2},
            42: {"card": "Three",
                 "suit": "Clubs",
                 "value": 3},
            43: {"card": "Four",
                 "suit": "Clubs",
                 "value": 4},
            44: {"card": "Five",
                 "suit": "Clubs",
                 "value": 5},
            45: {"card": "Six",
                 "suit": "Clubs",
                 "value": 6},
            46: {"card": "Seven",
                 "suit": "Clubs",
                 "value": 7},
            47: {"card": "Eight",
                 "suit": "Clubs",
                 "value": 8},
            48: {"card": "Nine",
                 "suit": "Clubs",
                 "value": 9},
            49: {"card": "Ten",
                 "suit": "Clubs",
                 "value": 10},
            50: {"card": "Jack",
                 "suit": "Clubs",
                 "value": 10},
            51: {"card": "Queen",
                 "suit": "Clubs",
                 "value": 10},
            52: {"card": "King",
                 "suit": "Clubs",
                 "value": 10}}

    cardk1 = ''
    cardk2 = ''
    cardk3 = ''
    cardk4 = ''
    cardk5 = ''
    cardk6 = ''
    cardk7 = ''
    cardk8 = ''
    cardk9 = ''
    cardk10 = ''
    cardk11 = ''
    cardk12 = ''
    totalround2 = ''
    totalround3 = ''
    totalround4 = ''
    totalround5 = ''
    totalround6 = ''
    totalround7 = ''
    totalround8 = ''
    totalround9 = ''
    totalround10 = ''
    totalround11 = ''

    player1 = input("Hello!, What is your name?: ")
    print("Welcome {}! Now find a friend to play with!".format(player1))
    player2 = input("Hello!, What is your name?: ")
    print("Welcome {}! Let's play blackjack!".format(player1))

    rules = input("Do you know how to play? (Yes/No): ")
    if rules == "No":
        print("-"*40)
        print("Okay! The rules are simple. You'll receive two cards in your hand, as will {}, and the dealer. \n"
              "Your goal is to beat the dealer by getting closer to 21 or gettting 21 which is a blackjack.  \n"
              "Cards 2 - 10 counts as it's own number nd the face cards jacks, queens, and kings counts as 10 each, and aces can count\n"
              " as either 1 or 11. Each player can draw up to four cards at this table. House wins on a tie.".format(
            player1))
        print("-" * 40)
        print("Let's begin blackjack!")
        print("-" * 40)
    else:
        print("-"* 40)
        print("Let's begin blackjack!")
        print("-" * 40)
    firstseat = input("Who's up first? {} or {}? ".format(player1, player2))
    if firstseat == player1:
        secondseat = player2
    else:
        secondseat = player1

    # player1's turn
    wager = int(
        input("Would you like to bet 5 or 10 dollars? Your balance is {} dollars. (5/10): ".format(player1balance)))
    print("Good luck, {}. You place {} dollars on the table. You have a {} dollar remaining.\n"
          "Here are your two cards: ".format(firstseat, wager, player1balance - wager))
    cardk1 = random.choice(deck)
    for k, v in deck.items():
        if cardk1 == k:
            del deck[k]
    cardk2 = random.choice(deck)
    for k, v in deck.items():
        if cardk2 == k:
            del deck[k]
    round2 = (cardk1["value"]) + (cardk2["value"])
    # Ace needs to be checked
    if round2 == 22:
        round2 = 12

    print("{} of {} and a {} of {}. \n"
          "You're at: {}".format(cardk1["card"], cardk1["suit"], cardk2["card"], cardk3["suit"], totalround2))
    print("-" * 40)
    hit_stay = input("Hit or Stay? (Hit/Stay)")
    if hit_stay == "Hit":
        cardk3 = random.choice(deck)
        for k, v in deck.items():
            if cardk3 == k:
                del deck[k]
        totalround3 = (cardk1["value"]) + (cardk2["value"]) + (cardk3["value"])
        #ace can be 1 or 11 so need a check for that
        if int(totalround3) > 21 and cardk1["card"] == "Ace":
            int(totalround3) - 10
        if int(totalround3) > 21 and cardk2["card"] == "Ace":
            int(totalround3) - 10
        if int(totalround3) > 21 and cardk3["card"] == "Ace":
            int(totalround3) - 10

        print("{} of {}, {} of {}, and {} of {}.\n"
              "Total: {}".format(cardk1["card"], cardk1["suit"], cardk2["card"], cardk2["suit"],
                                 cardk3["card"], cardk3["suit"], totalround3))
        if totalround3 > 21:
            print("You have busted. Good luck next time :(.")
        if totalround3 < 21:
            hit_stay = input("Hit or Stay? (Hit/Stay)")
            if hit_stay == "Hit":
                cardk4 = random.choice(deck)
                for k, v in deck.items():
                    if cardk4 == k:
                        del deck[k]
                round4 = (cardk1["value"]) + (cardk2["value"]) + (cardk3["value"]) + (cardk4["value"])
                # Over 21 because of a 11 Ace? Let's make that ace into a 1 and update the total.
                if int(totalround4) > 21 and cardk1["card"] == "Ace":
                    int(totalround4) - 10
                if int(totalround4) > 21 and cardk2["card"] == "Ace":
                    int(totalround4) - 10
                if int(totalround4) > 21 and cardk3["card"] == "Ace":
                    int(totalround4) - 10
                if int(totalround4) > 21 and cardk4["card"] == "Ace":
                    int(totalround4) - 10
                print("{} of {}, {} of {}, {} of {} and {} of {}.\n"
                      "Total: {}".format(cardk1["card"], cardk1["suit"], cardk2["card"], cardk2["suit"],
                                         cardk3["card"], cardk3["suit"], cardk4["card"], cardk4["suit"],
                                         totalround4))
                if totalround4 > 21:
                    print("You have busted. May luck be with you next time :(.")
            else:
                print("-" * 40)
                print("It is now {}'s turn.\n"
                      "Good luck {}! ".format(secondseat, secondseat))
                print("-" * 40)
        else:
            print("It is now {}'s turn.\n"
                  "Good luck {}! ".format(secondseat, secondseat))
            print("-" * 40)
    else:
        print("It is now {}'s turn.\n"
              "Good luck {}! ".format(secondseat, secondseat))
        print("-" * 40)

    # PLAYER2 TURN
    wager2 = int(input(
        "Would you like to bet 5 or 10 dollars, {}? Your balance is {} dollars. (5/10): ".format(secondseat,
                                                                                                player2balance)))
    print("Good luck, {}. You place {} dollars on the table. You have a {} dollar remaining balance.\n"
          "Here are your two cards: ".format(secondseat, wager2, player2balance - wager2))
    cardk5 = random.choice(deck)
    for k, v in deck.items():
        if cardk5 == k:
            del deck[k]
    cardk6 = random.choice(deck)
    for k, v in deck.items():
        if cardk6 == k:
            del deck[k]

    totalround5 = (cardk5["value"]) + (cardk6["value"])
    # Double Ace Check
    if totalround5 == 22:
        totalround5 = 12

    print("{} of {} and a {} of {}. \n"
          "You're at: {}".format(cardk5["card"], cardk5["suit"], cardk6["card"], cardk6["suit"], totalround5))
    print("-" * 40)
    hit_stay = input("Hit or Stay? (Hit/Stay)")

    if hit_stay == "Hit":
        cardk7 = random.choice(deck)
        for k, v in deck.items():
            if cardk7 == k:
                del deck[k]
        totalround6 = (cardk5["value"]) + (cardk6["value"]) + (cardk7["value"])
        if int(totalround6) > 21 and cardk5["card"] == "Ace":
            int(totalround6) - 10
        if int(totalround6) > 21 and card6key["card"] == "Ace":
            int(totalround6) - 10
        if int(totalround6) > 21 and card7key["card"] == "Ace":
            int(totalround6) - 10
        print("{} of {}, {} of {}, and {} of {}.\n"
              "Total: {}".format(cardk5["card"], cardk5["suit"], cardk6["card"], cardk6["suit"],
                                 cardk7["card"], cardk7["suit"], totalround6))
        if totalround6 > 21:
            print("! Good luck next time :(.")
        if totalround6 < 21:
            hit_stay = input("Hit or Stay? (Hit/Stay)")

            if hit_stay == "Hit":
                cardk8 = random.choice(deck)
                for k, v in deck.items():
                    if cardk8 == k:
                        del deck[k]
                totalround7 = (cardk5["value"]) + (cardk6["value"]) + (cardk7["value"]) + (cardk8["value"])
                if int(totalround7) > 21 and cardk5["card"] == "Ace":
                    int(totalround7) - 10
                if int(totalround7) > 21 and cardk6["card"] == "Ace":
                    int(totalround7) - 10
                if int(totalround7) > 21 and cardk7["card"] == "Ace":
                    int(totalround7) - 10
                if int(totalround7) > 21 and cardk8["card"] == "Ace":
                    int(totalround7) - 10
            print("{} of {}, {} of {}, {} of {} and {} of {}.\n"
                  "Total: {}".format(cardk5["card"], cardk5["suit"], cardk6["card"], cardk6["suit"],
                                     cardk7["card"], cardk7["suit"], cardk8["card"], cardk8["suit"],
                                     int(totalround7)))
            if totalround7 > 21:
                print("You have bust. Good luck next time :(.")
            else:
                print("-" * 40)
                print("It is the dealer's turn now . Good luck everyone! ")
                print("-" * 40)
        else:
            print("It is the dealer's turn now. Good luck everyone! ")
            print("-" * 40)
    else:
        print("It is the dealer's turn now. Good luck everyone! ")
        print("-" * 40)

    # DEALER DRAWS TWO CARDS
    cardk9 = random.choice(deck)
    for k, v in deck.items():
        if cardk9 == k:
            del deck[k]
    cardk10 = random.choice(deck)
    for k, v in deck.items():
        if cardk10 == k:
            del deck[k]
    totalround8 = (cardk9["value"]) + (cardk10["value"])
    # DOUBLE ACE CHECK
    if toatalround8 == 22:
        totalround8 = 12
    print("{} of {} and a {} of {}.\n"
          "Total: {}".format(cardk9["card"], cardk9["suit"], cardk10["card"], cardk10["suit"], round8))

    if totalround8 < 16:  # and another card if less than 16
        cardk11 = random.choice(deck)
        for k, v in deck.items():
            if cardk11 == k:
                del deck[k]
        totalround9 = (cardk9["value"]) + (cardk10["value"]) + (cardk11["value"])

        if int(round9) > 21:
            if cardk9["card"] == "Ace":
                int(round9) - 10
            if cardk10["card"] == "Ace":
                int(round9) - 10
            if cardk11["card"] == "Ace":
                int(round9) - 10
        print("{} of {}, {} of {}, and {} of {}.\n"
              "Total: {}".format(cardk9["card"], cardk9["suit"], cardk10["card"], cardk10["suit"],
                                 cardk11["card"], cardk11["suit"], round9))

        if totalround9 < 16:
            cardk12 = random.choice(deck)
            for k, v in deck.items():
                if cardk12 == k:
                    del deck[k]
            totalround10 = (cardk9["value"]) + (cardk10["value"]) + (cardk11["value"] + (cardk12["value"]))

            if int(totalround10) > 21:
                if cardk9["card"] == "Ace":
                    int(totalround10) - 10
                if cardk10["card"] == "Ace":
                    int(totalround10) - 10
                if cardk11["card"] == "Ace":
                    int(totalround10) - 10
                if cardk12["card"] == "Ace":
                    int(round10) - 10
            print("{} of {}, {} of {}, {} of {}, and {} of {}.\n"
                  "Total: {}".format(cardk9["card"], cardk9["suit"], cardk10["card"], cardk10["suit"],
                                     cardk11["card"], cardk11["suit"], cardk12["card"], cardk12["suit"],
                                     totalround10))

            if totalround10 > 21:  # BUST
                print("Dealer has bust!")
            if totalround10 < 21:
                print("The dealer stays at {}.".format(totalround10))

        if totalround9 > 21:  # BUST
            print("Dealer has bust!")

        else:
            print("The dealer stays at {}.".format(totalround9))
            print("-" * 40)

    else:
        print("The dealer stays at {}.".format(totalround8))
        print("-" * 40)

    # RESULTS OF ROUND
    print("-" * 40)
    print("----------RESULTS----------")

    # player1 results
    if int(totalround2 or totalround3 or totalround4) > 21:  # BUST
        print("The dealer wins against {}! You lost money. :(.".format(firstseat))
        player1balance -= wager
    if int(totalround8 or totalround9 or totalround10) >= int(
            totalround4 or totalround3 or totalround2):
        print("The dealer wins against {}! You lost your bet.".format(firstseat))
        player1balance -= wager
    else:
        print("{} won against the dealer, and won {} dollars!".format(firstseat, wager * 2))
        player1balance += wager * 2

    # player2 results
    if int(totalround5 or totalround6 or totalround7) > 21:
        print("The dealer wins against {}!  Sorry, you lost your bet.".format(secondseat))
        player2balance -= wager2
    if int(totalround8 or totalround9 or totalround10) >= int(
            totalround7 or totalround6 or totalround5):
        print("The dealer wins against {}! Sorry, you lost your bet.".format(secondseat))
        player2balance -= wager2
    else:
        print("{} won against the dealer, and won {} dollars!".format(secondseat, wager2 * 2))
        player2balance += wager2 * 2

    print("-" * 40)
    anothergame = input(
        "Would you like to play another round? {}'s remaining balance is {} and {}'s remaning balance is {}. (Yes/No) ".format(
            firstseat, player1balance, secondseat, player2balance))
    if anothergame == "No":
        print("Thanks for playing! Stay safe out there!")