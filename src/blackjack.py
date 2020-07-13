''' 

GAME LOGIC FOR BLACKJACK

'''

from card import suits, ranks, values
from deck import Deck
from dealer import Dealer
from player import Player
from endgame import *

playing = True

while True:
    # Print an opening statement
    print('\n**********************************************')
    print('****** WELCOME TO THE GAME OF BLACKJACK ******')
    print('**********************************************')
    print('\nHere are the rules:\n\
    Get as close to 21 as you can without going over\n\
    Dealer hits until they reach 17 \n\
    Aces count as 1 or 11\n')

    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck(suits, ranks, values)
    deck.shuffle()

    player = Player()
    player.add_card(deck.deal())
    player.add_card(deck.deal())

    dealer = Dealer()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())
    
        
    # Set up the Player's chips (this occurs when the player is initialized.. not needed)
    
    
    # Prompt the Player for their bet
    player.ask_for_bet()

    
    # Show cards (but keep one dealer card hidden)
    player.show_all()
    dealer.show_some()

    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        playing = player.hit_or_stand(deck)
        
        
        # Show cards (but keep one dealer card hidden)
        player.show_all()
        dealer.show_some()
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if (player.busted()):
            player_busts(player)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if (player.busted() == False):

        while dealer.value < 17 and player.has_twenty_one() == False:
            dealer.hit(deck)
    
        # Show all cards
        player.show_all()
        dealer.show_all()
    
        # Run different winning scenarios
        dealer_busts(player, dealer)
        dealer_wins(player, dealer)
        player_wins(player, dealer)
        push(player, dealer)
        
    
    # Inform Player of their chips total
    # print('\nPlayer\'s winnings stand at', player.chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break