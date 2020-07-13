''' 

PLAYER OBJECT FOR MANAGING PLAYER ACTIONS

'''

from hand import Hand
from chip import Chip

class Player(Hand):

    def __init__(self):
        Hand.__init__(self)
        self.chips = Chip()
        self.bet = 0 # default bet amount
    
    def ask_for_bet(self):
        print(f'Player\'s current chip amount is: {self.chips.total}\n')

        # ask the player how much they would like to bet
        try:
            amount = int(input("How much would you like to bet?\n"))
            self.place_bet(amount)

        except:
            print('Whoops! Could not place your bet. Please try again')
            self.ask_for_bet()
    
    def place_bet(self, amount):
        # check to make sure the bet amount is valid
        if (self.chips.total >= amount and amount > 0):
            # set the bet and subtract the amount from the player's chip total
            self.bet = amount
            self.chips.subtract(amount)

        elif (self.chips.total >= amount):
            print("Whoops! You can not place a bet that exceeeds your chip amount. Please place a new bet.")
            self.ask_for_bet()

        elif (amount <= 0):
            print("Whoops! You can not place a bet less than or eqal to zero. Please place a new bet.")
            self.ask_for_bet()

        else:
            print("Whoops! Something is wrong with your bet. Please place a new bet.")
            self.ask_for_bet()

    def hit(self, deck):
        print('Player hits.')
        # take a card from the deck
        new_card = deck.deal()
        self.add_card(new_card)

    def hit_or_stand(self, deck):
        playing = True

        while True:
            # ask the player if they want to hit or stand
            resp = input("\nDo you want to hit or stand? Enter 'h' or 's'").lower()
            
            # if player chose hit draw a card from the deck
            if (resp.startswith('h')):
                self.hit(deck)
            
            elif (resp.startswith('s')):
                print("Player stands. Dealer is playing.")
                playing = False

            else: 
                print('Sorry, please try again.')
                continue

            break
        
        return playing
    
    def clear_hand(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.bet = 0

        print('Player\'s hand was cleared.')