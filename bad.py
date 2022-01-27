# Import the API objects
from api import State, util
from api import Deck
#import utils
import random

class Bot:

     # How many samples to take per move
    __num_samples = -1
    # How deep to sample
    __depth = -1
    
    def __init__(self, num_samples=4, depth=8):
        self.__num_samples = num_samples
        self.__depth = depth
        
    def get_move(self, state):
        # type: (State) -> tuple[int, int]
        
        # All legal moves
        moves = state.moves()
        chosen_move = moves[0]
        # See if we're player 1 or 2
        player = state.whose_turn()
        
        random.shuffle(moves)
        
        best_score = float("-inf")
        best_move = None

        scores = [0.0] * len(moves)

        moves_trump_suit = []
            
        # If the current phase is 1
        if state.get_phase() == 1:
            
            # Get move with lowest rank available, of any suit
            for index, move in enumerate(moves):
                if move[0] is not None and move[0] % 5 >= chosen_move[0] % 5:
                    if Deck.get_suit(move[0]) == state.get_trump_suit(): 
                        continue
                    chosen_move = move #mybot tries to always choose the move with the lowest rank of any suit     

            return chosen_move
        
        else: # if the current phase is 2
             
             #Get all trump suit moves available
            for index, move in enumerate(moves):
                if move[0] is not None and Deck.get_suit(move[0]) == state.get_trump_suit():
                    moves_trump_suit.append(move)
            
            if len(moves_trump_suit) > 0:
                for index, move in enumerate(moves_trump_suit):
                    if move[0] is not None and move[0] % 5 <= chosen_move[0] % 5:
                        chosen_move = move #if mybot has one or more trump cards it chooses the highest trump card
            return chosen_move
                
        