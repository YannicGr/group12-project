#Import the API objects

from api import State
from api import Deck
import random

class Bot:

    def __init__(self):
        pass
    
    def get_move(self, state):
        moves=state.moves()
        chosen_move=moves[0]
        trump_card=[]
        ex_move=[]
        opponents_played_card=[]
        