''' 

HAND OBJECT FOR INTERACTING WITH A PLAYER'S HAND

'''

class Hand:

    def __init__(self):
        self.cards = [] # cards in a hand
        self.value = 0 # total value of a hand
        self.aces = 0 # number of aces in a hand

    def add_card(self, card):
        
        if (card.isAce()):
            self.aces += 1
            ace_value = self.handle_aces()
            card.value = ace_value
        
        self.cards.append(card)
        self.value += card.value

    def has_twenty_one(self):
        return self.value == 21

    def busted(self):
        return self.value > 21

    def clear_hand(self):
        self.cards = []
        self.value = 0
        self.aces = 0

        print('Your hand was cleared.')

    def handle_aces(self):
        self.show_all()
        return int(input("What do you like the value of your Ace to be? 1 or 11: \n"))

    def show_all(self):
        print('\nPlayer\'s cards in hand are: \n   ' + '\n   '.join(map(str, [str(card) + ' ('+ str(card.value) + ')' for card in self.cards])))