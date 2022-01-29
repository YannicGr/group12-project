#Import the API objects

from api import State
from api import Deck
import random

class Bot:

    def __init__(self):
        pass
    
    def get_move(self, state):

        #All legal moves
        moves=state.moves()
        chosen_move=moves[0]
        trump_suit=[]


        marriage_move=[]

        #if the opponent has played a card
        if state.get_opponents_played_card() is not None:
        
        #Get the trump suit moves available
            for index, move in enumerate(moves):
                if move[0] is not None and Deck.get_suit(move[0]) == state.get_trump_suit():
                    trump_suit.append(move)
            if len(trump_suit) > 0:
                chosen_move = trump_suit[0]
                return chosen_move
            
            else:
                return random.choice(moves)

        
        else:
            for index, move in enumerate(moves):
                if move[0] is not None and Deck.get_possible_mariages(self, move[0]):
                    marriage_move.append(move)
            
            if len(marriage_move)>0:
                chosen_move=marriage_move[0]
                return chosen_move


            else:
                return random.choice(moves)

