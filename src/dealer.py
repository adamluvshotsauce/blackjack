''' 

DEALER OBJECT FOR MANAGING DEALER ACTIONS

'''

from hand import Hand

class Dealer(Hand):

    def __init__(self):
        Hand.__init__(self)

    def hit(self, deck):
        print('\nDealer hits...')
        # take a card from the deck
        new_card = deck.deal()
        self.add_card(new_card)
    
    def show_some(self):
        print('\nDealer\'s hand is: \n   ' + '\n   '.join(map(str, [str(card) + ' ('+ str(card.value) + ')' for card in self.cards[1:]])))
        print('   <Card Hidden>')

    ### Method Overrides ###

    def clear_hand(self):
        self.cards = []
        self.value = 0
        self.aces = 0

        print('\nDealer\'s hand was emptied.')

    def handle_aces(self):
        ace_value = 11
        # Allow the dealer to avoid a bust on Aces
        if (self.value > 10):
            ace_value = 1
        # print('\nThe dealer chose the Ace value: ' + str(ace_value))
        return ace_value

    def show_all(self):
        print('\nDealer\'s hand is: \n   ' + '\n   '.join(map(str, [str(card) + ' ('+ str(card.value) + ')' for card in self.cards])))
