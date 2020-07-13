'''

STORES FUNCTIONS FOR END GAME SCENARIOS

'''

def player_busts(player):
    # Take the bet from the player's chip amount
    # Alert the player they busted
    if (player.busted()):
        print(f'\nOh No! You Busted! You lost {player.bet} chips.')
        print(f'You have {player.chips.total} remaining chips.')

def player_wins(player, dealer):
    # Double the player's bet and add it to their chip amount
    # Alert the player they won
    if (player.has_twenty_one() or player.value > dealer.value):
        player.chips.add_multiple(player.bet, 2)
        print(f'\nHell Yeah! You Won!! Your winnings are {player.bet} chips!')
        print(f'You now have {player.chips.total} chips.')

def dealer_busts(player, dealer):
    # When deal busts add the player's bet to thier chip amount
    # Alert the player the dealer busted
    if (dealer.busted()):
        player.chips.add_multiple(player.bet, 2)
        print(f'\nAhhh Yeah! The Dealer busted. You won! Your winnings are {player.bet} chips!')
        print(f'You now have {player.chips.total} chips.')
    
def dealer_wins(player, dealer):
    # When the dealer wins take the bet from the player's chip amount
    # Alert the player the dealer won
    if (dealer.has_twenty_one() 
        or (dealer.value > player.value 
            and dealer.busted() == False)):
        print(f'\nOh No! The Dealer won. You lost {player.bet} chips.')
        print(f'You have {player.chips.total} remaining chips.')
    
def push(player, dealer):
    # When there's a push return the player's bet to their chip amount
    # Alert the player there was a push
    if (player.value == dealer.value):
        player.chips.add(player.bet)
        print(f'\nEhh... It was a push. At least you didn\'t lose your bet of {player.bet} chips.')
        print(f'You now have {player.chips.total} chips.')