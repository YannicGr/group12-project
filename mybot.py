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
            
        # If the opponent has played a card
        if state.get_opponents_played_card() is not None:
            
            #Get all trump suit moves available
            for index, move in enumerate(moves):
                if move[0] is not None and Deck.get_suit(move[0]) == state.get_trump_suit():
                    moves_trump_suit.append(move)
            
            if len(moves_trump_suit) > 0:
                chosen_move = moves_trump_suit[0] #if mybot has a trump card he chooses that card
                return chosen_move
            
            # Get move with highest rank available, of any suit
            #for index, move in enumerate(moves):
                #if move[0] is not None and move[0] % 5 <= chosen_move[0] % 5:
                    #chosen_move = move #mybot tries to always choose the move with the highest rank of any suit
            
            #if the chosen card is smaller than the card of the opponent, choose the card with rdeep algorithm
            for move in moves:
                for s in range(self.__num_samples):
                    # If we are in an imperfect information state, make an assumption.
                    sample_state = state.make_assumption() if state.get_phase() == 1 else state
                    score = self.evaluate(sample_state.next(move), player)
                    
                    if score > best_score:
                        best_score = score
                        best_move = move
            return best_move # Return the best scoring move
            return chosen_move
        
        else: #if mybot starts with the first card, use the rdeep algorithm
            for move in moves:
                for s in range(self.__num_samples):
                    # If we are in an imperfect information state, make an assumption.
                    sample_state = state.make_assumption() if state.get_phase() == 1 else state
                    score = self.evaluate(sample_state.next(move), player)
                    
                    if score > best_score:
                        best_score = score
                        best_move = move
            return best_move # Return the best scoring move
            return chosen_move
                
        
        
        return chosen_move
    
    def evaluate(self, state, player):
        score = 0.0
        
        for _ in range(self.__num_samples):
            st = state.clone()
            
            # Do some random moves
            for i in range(self.__depth):
                if st.finished():
                    break
                    
                
                st = st.next(random.choice(st.moves()))

            score += self.heuristic(st, player)
                    
        return score/float(self.__num_samples)
    
    def heuristic(self, state, player):
        return util.ratio_points(state, player) 