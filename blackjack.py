import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True
# Card class
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

# Deck class
class Deck:
    def __init__(self):
        # Empty deck list
        self.deck = []
        for suit in suits:
            for rank in ranks:
                # Build card object and add to deck list
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        # "Pops" a card off the end of the list
        single_card = self.deck.pop()
        return single_card

'''
Testing full deck
test_deck = Deck()
print(test_deck)
'''

class Hand:
    def __init__(self):
        # Empty list similar to Deck class
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            # Add 1 to self.aces
            self.aces += 1

    def adjust_for_ace(self):
        # If total value > 21 and still have an ace
        # Then change Aceto 1 instead of an 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


'''
# Test to see if two card are being added to player's hand
test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())
print(test_player.value)

for card in test_player.cards:
    print(card)
'''

class Chips:
    def __init__(self):
        while True:
            try:
                self.total = int(input('Please enter how many chips would you like to begin with: '))
                break
            except ValueError:
                print('Invalid entry. Please enter an integer: ')
                self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

# Function for taking bets
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Please enter an integer: ')
        else:
            if chips.bet > chips.total:
                print(f"Sorry, your bet cannot exceed {chips.total}")
            else:
                break

# Hit function
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    # Control upcoming while loop
    global playing

    while True:
        x = input("\nHit or Stand? Enter H or S: ")

        if x[0].upper() == 'H':
            hit(deck,hand)
        elif x[0].upper() == 'S':
            print("Player stand. Dealer's turn.")
            playing = False
        else:
            print("Sorry invalid input. Please enter 'H' or 'S': ")
            continue
        break

def show_some(player,dealer):
    # Show one of dealer's cards
    print("\nDealer's Hand: ")
    print('Hidden card')
    # Essentiall showing second card
    print(dealer.cards[1])
    # Show both cards from player's hand
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    # Show dealer full hand
    print("\nDealer's Hand: ")
    for card in dealer.cards:
        print(card)
    # Display value of cards
    print(f"Value of Dealer's hand is: {dealer.value} ")
    # Show player full hand
    print(f"\nPlayer's hand: {player.value}")
    for card in player.cards:
        print(card)

def player_busts(player,dealer,chips):
    print("Player bust!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer bust! Player wins!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Push!")

# Full game logic
while True:
    print('Welcome to Python Blackjack!')
    # Instance of Deck class
    deck = Deck()
    # Shuffle deck
    deck.shuffle()

    # Player opening hand using Hand class
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    # Dealer opening hand using Hand class
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Instance of Chips class
    player_chips = Chips()
    # Promt player for bet
    take_bet(player_chips)
    # Show cards but keep dealer's at index 1 hidden
    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    print(f"\nPlayer's total chips are at: {player_chips.total}")
    new_game = input("Would you like to play again? Enter 'Y' or 'N': ")

    if new_game[0].upper() == 'Y':
        playing = True
        continue
    else:
        print('Thanks for playing!')
        break