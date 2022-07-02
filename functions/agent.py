import random
from collections import deque

import torch

from functions.model import Linear_QNet, QTrainer

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:

    '''AI Agent to play the game'''
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0 # randomness
        self.gamma = 0.9 # discount rate
        self.memory = deque(maxlen=MAX_MEMORY) # popleft()
        self.model = Linear_QNet(6, 256, 3)
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)


    def get_action(self, state):
        '''
        Predicts the next action.

        Input:
            - state: current state of the game
        Output:
            - AI's next move
        '''
        self.epsilon = 80 - self.n_games
        next_move = [0,0,0]
        if random.randint(0, 200) < self.epsilon: #random moves: tradeoff exploration / exploitation
            move = random.randint(0, 2)
            next_move[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float) # pylint: disable=no-member
            prediction = self.model(state0)
            move = torch.argmax(prediction).item() # pylint: disable=no-member
            next_move[move] = 1

        return next_move

    def remember(self, state, action, reward, new_state, game_over):
        '''
        Add relevant values to self.memory deque
        '''
        self.memory.append((state, action, reward, new_state, game_over))

    def train_short_memory(self, state, action, reward, new_state, game_over):
        '''
        Train NN short memory
        '''
        self.trainer.train_step(state, action, reward, new_state, game_over)

    def train_long_memory(self):
        '''
        Train NN long memory
        '''
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE) # list of tuples
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)
