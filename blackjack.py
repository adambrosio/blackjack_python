import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True
# Card class
class Card:

    def __init__(self,suit,rank):
        suit = self.suit
        rank = self.rank

    def __str__(self):
        return self.rank + 'of' + self.suit

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
            return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        # "Pops" a card off the end of the list
        single_card = self.deck.pop()
        return single_card