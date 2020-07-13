'''

CARD OBJECT FOR INTERACTING WITH THE PLAYING DECK

'''

import random
from card import Card

class Deck:
    

    def __init__(self, suits, ranks, values):
        self.suits = suits
        self.ranks = ranks
        self.values = values

        self.deck = [] # Start with an empty deck
        for suit in self.suits:
            for rank in self.ranks:
                card = Card(suit,rank,self.values[rank])
                self.deck.append(card)

    def shuffle(self):
        print('Shuffling deck...')
        random.shuffle(self.deck)
        print('Deck shuffled\n')

    def deal(self):
        return self.deck.pop(0)
    
    def __str__(self):
        return 'There are {0} cards in this deck.'.format(str(len(self.deck)))


    
