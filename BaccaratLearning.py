Jupyter Notebook
TestBaccarat
Last Checkpoint: 06/11/2020
(unsaved changes)
Current Kernel Logo
Python 3 
File
Edit
View
Insert
Cell
Kernel
Widgets
Help

Code
Baccarat Reinforcement Learning
from Baccarat import *
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
Create Baccarat game object and start the game.

​
win_proportions = []
​
for _ in range(100):
    # initialize Baccarat object
    baccarat = Baccarat()
    # start the game
    baccarat.start_game()
    # set the total number of rounds
    baccarat.set_rounds(10000)
    # play the game and get win proportion
    win_prop = baccarat.play_baccarat()
    print("")
    win_proportions.append(win_prop)
​
​
Baccarat Game Statistics for Agent
Total number of deals played: 9
Total number of deals won: 4
Percentage of deals won: 44.0 %
Largest amount won: 141.75
Largest amount lost: -330.75

Baccarat Game Statistics for Agent
Total number of deals played: 39
Total number of deals won: 16
Percentage of deals won: 41.0 %
Largest amount won: 20.25
Largest amount lost: -36

Baccarat Game Statistics for Agent
Total number of deals played: 12
Total number of deals won: 6
Percentage of deals won: 50.0 %
Largest amount won: 18.0
Largest amount lost: -48

Baccarat Game Statistics for Agent
Total number of deals played: 7
Total number of deals won: 4
Percentage of deals won: 56.99999999999999 %
Largest amount won: 36.0
Largest amount lost: -132.25

Baccarat Game Statistics for Agent
Total number of deals played: 218
Total number of deals won: 93
Percentage of deals won: 43.0 %
Largest amount won: 50.720947265625
Largest amount lost: -67.6279296875

Baccarat Game Statistics for Agent
Total number of deals played: 15
Total number of deals won: 9
Percentage of deals won: 60.0 %
Largest amount won: 72.0
Largest amount lost: -254.875

Baccarat Game Statistics for Agent
Total number of deals played: 40
Total number of deals won: 19
Percentage of deals won: 47.0 %
Largest amount won: 58.5
Largest amount lost: -136.5

Baccarat Game Statistics for Agent
Total number of deals played: 37
Total number of deals won: 12
Percentage of deals won: 32.0 %
Largest amount won: 13.125
Largest amount lost: -32

Baccarat Game Statistics for Agent
Total number of deals played: 35
Total number of deals won: 11
Percentage of deals won: 31.0 %
Largest amount won: 9.0
Largest amount lost: -24

Baccarat Game Statistics for Agent
Total number of deals played: 34
Total number of deals won: 11
Percentage of deals won: 32.0 %
Largest amount won: 9.0
Largest amount lost: -42.5

Baccarat Game Statistics for Agent
Total number of deals played: 25
Total number of deals won: 10
Percentage of deals won: 40.0 %
Largest amount won: 55.03125
Largest amount lost: -128.40625

Baccarat Game Statistics for Agent
Total number of deals played: 67
Total number of deals won: 29
Percentage of deals won: 43.0 %
Largest amount won: 39.75
Largest amount lost: -64

Baccarat Game Statistics for Agent
Total number of deals played: 107
Total number of deals won: 55
Percentage of deals won: 51.0 %
Largest amount won: 27.0
Largest amount lost: -72.5

Baccarat Game Statistics for Agent
Total number of deals played: 22
Total number of deals won: 10
Percentage of deals won: 45.0 %
Largest amount won: 71.625
Largest amount lost: -167.125

Baccarat Game Statistics for Agent
Total number of deals played: 8
Total number of deals won: 3
Percentage of deals won: 38.0 %
Largest amount won: 18.0
Largest amount lost: -96

Baccarat Game Statistics for Agent
Total number of deals played: 71
Total number of deals won: 31
Percentage of deals won: 44.0 %
Largest amount won: 70.875
Largest amount lost: -124.03125

Baccarat Game Statistics for Agent
Total number of deals played: 37
Total number of deals won: 14
Percentage of deals won: 38.0 %
Largest amount won: 87.9375
Largest amount lost: -91.4375

Baccarat Game Statistics for Agent
Total number of deals played: 187
Total number of deals won: 98
Percentage of deals won: 52.0 %
Largest amount won: 234.23382568359375
Largest amount lost: -546.5455932617188

Baccarat Game Statistics for Agent
Total number of deals played: 15
Total number of deals won: 5
Percentage of deals won: 33.0 %
Largest amount won: 24.0
Largest amount lost: -32

Baccarat Game Statistics for Agent
Total number of deals played: 29
Total number of deals won: 14
Percentage of deals won: 48.0 %
Largest amount won: 96.0
Largest amount lost: -135.5

Baccarat Game Statistics for Agent
Total number of deals played: 17
Total number of deals won: 6
Percentage of deals won: 35.0 %
Largest amount won: 12.0
Largest amount lost: -42.75

Baccarat Game Statistics for Agent
Total number of deals played: 56
Total number of deals won: 34
Percentage of deals won: 61.0 %
Largest amount won: 192.0
Largest amount lost: -256

Baccarat Game Statistics for Agent
Total number of deals played: 16
Total number of deals won: 7
Percentage of deals won: 44.0 %
Largest amount won: 24.0
Largest amount lost: -128

Baccarat Game Statistics for Agent
Total number of deals played: 20
Total number of deals won: 8
Percentage of deals won: 40.0 %
Largest amount won: 72.0
Largest amount lost: -174.25

Baccarat Game Statistics for Agent
Total number of deals played: 36
Total number of deals won: 14
Percentage of deals won: 39.0 %
Largest amount won: 18.0
Largest amount lost: -48

Baccarat Game Statistics for Agent
Total number of deals played: 54
Total number of deals won: 31
Percentage of deals won: 56.99999999999999 %
Largest amount won: 30.9375
Largest amount lost: -72.1875

Baccarat Game Statistics for Agent
Total number of deals played: 4
Total number of deals won: 1
Percentage of deals won: 25.0 %
Largest amount won: 3.0
Largest amount lost: -48

Baccarat Game Statistics for Agent
Total number of deals played: 40
Total number of deals won: 23
Percentage of deals won: 56.99999999999999 %
Largest amount won: 24.0
Largest amount lost: -86.5

Baccarat Game Statistics for Agent
Total number of deals played: 71
Total number of deals won: 31
Percentage of deals won: 44.0 %
Largest amount won: 48.0
Largest amount lost: -96

Baccarat Game Statistics for Agent
Total number of deals played: 40
Total number of deals won: 20
Percentage of deals won: 50.0 %
Largest amount won: 24.28125
Largest amount lost: -56.65625

Baccarat Game Statistics for Agent
Total number of deals played: 36
Total number of deals won: 19
Percentage of deals won: 53.0 %
Largest amount won: 112.125
Largest amount lost: -256

Baccarat Game Statistics for Agent
Total number of deals played: 21
Total number of deals won: 9
Percentage of deals won: 43.0 %
Largest amount won: 10.3125
Largest amount lost: -36

Baccarat Game Statistics for Agent
Total number of deals played: 55
Total number of deals won: 19
Percentage of deals won: 35.0 %
Largest amount won: 40.60546875
Largest amount lost: -94.74609375

Baccarat Game Statistics for Agent
Total number of deals played: 70
Total number of deals won: 27
Percentage of deals won: 39.0 %
Largest amount won: 24.0
Largest amount lost: -64

Baccarat Game Statistics for Agent
Total number of deals played: 34
Total number of deals won: 14
Percentage of deals won: 41.0 %
Largest amount won: 78.375
Largest amount lost: -137.15625

Baccarat Game Statistics for Agent
Total number of deals played: 118
Total number of deals won: 50
Percentage of deals won: 42.0 %
Largest amount won: 48.0
Largest amount lost: -36

Baccarat Game Statistics for Agent
Total number of deals played: 53
Total number of deals won: 20
Percentage of deals won: 38.0 %
Largest amount won: 87.132568359375
Largest amount lost: -128

Baccarat Game Statistics for Agent
Total number of deals played: 8
Total number of deals won: 4
Percentage of deals won: 50.0 %
Largest amount won: 18.0
Largest amount lost: -96

Baccarat Game Statistics for Agent
Total number of deals played: 5
Total number of deals won: 1
Percentage of deals won: 20.0 %
Largest amount won: 24.0
Largest amount lost: -123.0

Baccarat Game Statistics for Agent
Total number of deals played: 54
Total number of deals won: 25
Percentage of deals won: 46.0 %
Largest amount won: 506.4609375
Largest amount lost: -1350.5625

Baccarat Game Statistics for Agent
Total number of deals played: 84
Total number of deals won: 40
Percentage of deals won: 48.0 %
Largest amount won: 118.78125
Largest amount lost: -144

Baccarat Game Statistics for Agent
Total number of deals played: 118
Total number of deals won: 47
Percentage of deals won: 40.0 %
Largest amount won: 21.0
Largest amount lost: -32

Baccarat Game Statistics for Agent
Total number of deals played: 57
Total number of deals won: 32
Percentage of deals won: 56.00000000000001 %
Largest amount won: 27.0
Largest amount lost: -72

Baccarat Game Statistics for Agent
Total number of deals played: 10
Total number of deals won: 4
Percentage of deals won: 40.0 %
Largest amount won: 46.125
Largest amount lost: -107.625

Baccarat Game Statistics for Agent
Total number of deals played: 211
Total number of deals won: 86
Percentage of deals won: 41.0 %
Largest amount won: 93.9375
Largest amount lost: -144

Baccarat Game Statistics for Agent
Total number of deals played: 7
Total number of deals won: 1
Percentage of deals won: 14.000000000000002 %
Largest amount won: 12.0
Largest amount lost: -56.0

Baccarat Game Statistics for Agent
Total number of deals played: 56
Total number of deals won: 25
Percentage of deals won: 45.0 %
Largest amount won: 36.0
Largest amount lost: -96

Baccarat Game Statistics for Agent
Total number of deals played: 86
Total number of deals won: 42
Percentage of deals won: 49.0 %
Largest amount won: 81.0
Largest amount lost: -216

Baccarat Game Statistics for Agent
Total number of deals played: 36
Total number of deals won: 13
Percentage of deals won: 36.0 %
Largest amount won: 18.0
Largest amount lost: -43.0

Baccarat Game Statistics for Agent
Total number of deals played: 5
Total number of deals won: 2
Percentage of deals won: 40.0 %
Largest amount won: 20.25
Largest amount lost: -108

Baccarat Game Statistics for Agent
Total number of deals played: 57
Total number of deals won: 34
Percentage of deals won: 60.0 %
Largest amount won: 162.0
Largest amount lost: -470.5

Baccarat Game Statistics for Agent
Total number of deals played: 19
Total number of deals won: 13
Percentage of deals won: 68.0 %
Largest amount won: 81.0
Largest amount lost: -215.5

Baccarat Game Statistics for Agent
Total number of deals played: 156
Total number of deals won: 81
Percentage of deals won: 52.0 %
Largest amount won: 95.578125
Largest amount lost: -128

Baccarat Game Statistics for Agent
Total number of deals played: 113
Total number of deals won: 52
Percentage of deals won: 46.0 %
Largest amount won: 98.4375
Largest amount lost: -56.6875

Baccarat Game Statistics for Agent
Total number of deals played: 410
Total number of deals won: 191
Percentage of deals won: 47.0 %
Largest amount won: 182.25
Largest amount lost: -72

Baccarat Game Statistics for Agent
Total number of deals played: 14
Total number of deals won: 5
Percentage of deals won: 36.0 %
Largest amount won: 27.0
Largest amount lost: -125.5

Baccarat Game Statistics for Agent
Total number of deals played: 115
Total number of deals won: 56
Percentage of deals won: 49.0 %
Largest amount won: 72.0
Largest amount lost: -179.5

Baccarat Game Statistics for Agent
Total number of deals played: 31
Total number of deals won: 10
Percentage of deals won: 32.0 %
Largest amount won: 13.5
Largest amount lost: -72

Baccarat Game Statistics for Agent
Total number of deals played: 19
Total number of deals won: 7
Percentage of deals won: 37.0 %
Largest amount won: 54.0
Largest amount lost: -144

Baccarat Game Statistics for Agent
Total number of deals played: 12
Total number of deals won: 3
Percentage of deals won: 25.0 %
Largest amount won: 4.5
Largest amount lost: -48

Baccarat Game Statistics for Agent
Total number of deals played: 10
Total number of deals won: 5
Percentage of deals won: 50.0 %
Largest amount won: 51.1875
Largest amount lost: -119.4375

Baccarat Game Statistics for Agent
Total number of deals played: 10
Total number of deals won: 5
Percentage of deals won: 50.0 %
Largest amount won: 6.0
Largest amount lost: -62.75

Baccarat Game Statistics for Agent
Total number of deals played: 109
Total number of deals won: 56
Percentage of deals won: 51.0 %
Largest amount won: 24.0
Largest amount lost: -66.75

Baccarat Game Statistics for Agent
Total number of deals played: 27
Total number of deals won: 15
Percentage of deals won: 56.00000000000001 %
Largest amount won: 24.0
Largest amount lost: -95.75

Baccarat Game Statistics for Agent
Total number of deals played: 40
Total number of deals won: 21
Percentage of deals won: 53.0 %
Largest amount won: 168.0
Largest amount lost: -239.75

Baccarat Game Statistics for Agent
Total number of deals played: 31
Total number of deals won: 10
Percentage of deals won: 32.0 %
Largest amount won: 6.0
Largest amount lost: -32

Baccarat Game Statistics for Agent
Total number of deals played: 13
Total number of deals won: 3
Percentage of deals won: 23.0 %
Largest amount won: 3.0
Largest amount lost: -37.75

Baccarat Game Statistics for Agent
Total number of deals played: 20
Total number of deals won: 8
Percentage of deals won: 40.0 %
Largest amount won: 18.0
Largest amount lost: -64

Baccarat Game Statistics for Agent
Total number of deals played: 98
Total number of deals won: 48
Percentage of deals won: 49.0 %
Largest amount won: 81.0
Largest amount lost: -289.75

Baccarat Game Statistics for Agent
Total number of deals played: 49
Total number of deals won: 24
Percentage of deals won: 49.0 %
Largest amount won: 12.0
Largest amount lost: -64

Baccarat Game Statistics for Agent
Total number of deals played: 52
Total number of deals won: 23
Percentage of deals won: 44.0 %
Largest amount won: 12.0
Largest amount lost: -48

Baccarat Game Statistics for Agent
Total number of deals played: 14
Total number of deals won: 6
Percentage of deals won: 43.0 %
Largest amount won: 100.6875
Largest amount lost: -134.25

Baccarat Game Statistics for Agent
Total number of deals played: 66
Total number of deals won: 30
Percentage of deals won: 45.0 %
Largest amount won: 54.0
Largest amount lost: -144

Baccarat Game Statistics for Agent
Total number of deals played: 7
Total number of deals won: 4
Percentage of deals won: 56.99999999999999 %
Largest amount won: 98.4375
Largest amount lost: -229.6875

Baccarat Game Statistics for Agent
Total number of deals played: 22
Total number of deals won: 8
Percentage of deals won: 36.0 %
Largest amount won: 18.0
Largest amount lost: -54

Baccarat Game Statistics for Agent
Total number of deals played: 5
Total number of deals won: 3
Percentage of deals won: 60.0 %
Largest amount won: 18.0
Largest amount lost: -72

Baccarat Game Statistics for Agent
Total number of deals played: 12
Total number of deals won: 11
Percentage of deals won: 92.0 %
Largest amount won: 162.0
Largest amount lost: -435.25

Baccarat Game Statistics for Agent
Total number of deals played: 13
Total number of deals won: 3
Percentage of deals won: 23.0 %
Largest amount won: 36.0
Largest amount lost: -97.0

Baccarat Game Statistics for Agent
Total number of deals played: 77
Total number of deals won: 28
Percentage of deals won: 36.0 %
Largest amount won: 44.953125
Largest amount lost: -119.875

Baccarat Game Statistics for Agent
Total number of deals played: 40
Total number of deals won: 13
Percentage of deals won: 33.0 %
Largest amount won: 18.0
Largest amount lost: -72

Baccarat Game Statistics for Agent
Total number of deals played: 103
Total number of deals won: 41
Percentage of deals won: 40.0 %
Largest amount won: 72.0
Largest amount lost: -48

Baccarat Game Statistics for Agent
Total number of deals played: 22
Total number of deals won: 9
Percentage of deals won: 41.0 %
Largest amount won: 92.4375
Largest amount lost: -98.9375

Baccarat Game Statistics for Agent
Total number of deals played: 31
Total number of deals won: 16
Percentage of deals won: 52.0 %
Largest amount won: 72.0
Largest amount lost: -174.25

Baccarat Game Statistics for Agent
Total number of deals played: 295
Total number of deals won: 140
Percentage of deals won: 47.0 %
Largest amount won: 118.875
Largest amount lost: -192

Baccarat Game Statistics for Agent
Total number of deals played: 40
Total number of deals won: 11
Percentage of deals won: 28.000000000000004 %
Largest amount won: 3.0
Largest amount lost: -17.25

Baccarat Game Statistics for Agent
Total number of deals played: 99
Total number of deals won: 47
Percentage of deals won: 47.0 %
Largest amount won: 67.875
Largest amount lost: -48

Baccarat Game Statistics for Agent
Total number of deals played: 45
Total number of deals won: 16
Percentage of deals won: 36.0 %
Largest amount won: 24.0
Largest amount lost: -32

Baccarat Game Statistics for Agent
Total number of deals played: 99
Total number of deals won: 38
Percentage of deals won: 38.0 %
Largest amount won: 6.0
Largest amount lost: -12

Baccarat Game Statistics for Agent
Total number of deals played: 32
Total number of deals won: 11
Percentage of deals won: 34.0 %
Largest amount won: 34.3125
Largest amount lost: -80.0625

Baccarat Game Statistics for Agent
Total number of deals played: 15
Total number of deals won: 10
Percentage of deals won: 67.0 %
Largest amount won: 36.0
Largest amount lost: -144

Baccarat Game Statistics for Agent
Total number of deals played: 16
Total number of deals won: 7
Percentage of deals won: 44.0 %
Largest amount won: 36.0
Largest amount lost: -72

Baccarat Game Statistics for Agent
Total number of deals played: 27
Total number of deals won: 11
Percentage of deals won: 41.0 %
Largest amount won: 32.0625
Largest amount lost: -73.5625

Baccarat Game Statistics for Agent
Total number of deals played: 32
Total number of deals won: 13
Percentage of deals won: 41.0 %
Largest amount won: 36.0
Largest amount lost: -109.0

Baccarat Game Statistics for Agent
Total number of deals played: 227
Total number of deals won: 110
Percentage of deals won: 48.0 %
Largest amount won: 548.37890625
Largest amount lost: -1462.34375

Baccarat Game Statistics for Agent
Total number of deals played: 20
Total number of deals won: 9
Percentage of deals won: 45.0 %
Largest amount won: 12.0
Largest amount lost: -64

Baccarat Game Statistics for Agent
Total number of deals played: 45
Total number of deals won: 16
Percentage of deals won: 36.0 %
Largest amount won: 22.125
Largest amount lost: -32

Baccarat Game Statistics for Agent
Total number of deals played: 22
Total number of deals won: 9
Percentage of deals won: 41.0 %
Largest amount won: 24.0
Largest amount lost: -96

Baccarat Game Statistics for Agent
Total number of deals played: 59
Total number of deals won: 29
Percentage of deals won: 49.0 %
Largest amount won: 48.0
Largest amount lost: -96

Baccarat Game Statistics for Agent
Total number of deals played: 34
Total number of deals won: 13
Percentage of deals won: 38.0 %
Largest amount won: 18.0
Largest amount lost: -72

Baccarat Game Statistics for Agent
Total number of deals played: 17
Total number of deals won: 5
Percentage of deals won: 28.999999999999996 %
Largest amount won: 12.75
Largest amount lost: -48

An agent which guesses randomly will choose the correct choice 33% of the time, therfore the goal is to have the agent choose the correct hand more often than random.

ax = sns.distplot(win_proportions)
ax.set(xlabel='Win Proportion', ylabel='Count', title="Win Proportions for Agent")
ax.axvline(np.mean(win_proportions), color="red")
ax.text(np.mean(win_proportions) + 0.01, 4, round(np.mean(win_proportions), 2), fontsize=12, color="red")
​
Text(0.4453000000000001, 4, '0.44')

The agent seems to perform better than random, however the behavior could still be improved.

realizing
## Results
​
​
Based on the plot the agents win proportion has a roughly normal distribution. The agent does better than randomly guessing but cannot seem to guess the correct hand each time. The proportion is similar to the proportion of choosing the banker each time, meaning that the agent is most likely choosing the banker as the winner; though there are probably some loses before the agent learns that choosing banker is the optimal strategy. For this version of baccarat the banker has the highest chance of winning, therefore it is safest to choose the banker each time. 
​
​
The roughly normal distribution along with the outliers most likely occur from the agent picking randomly before realizing that choosing the banker gives the highest returns.
## Future Steps
​
​
Several different modifications could potentially be made to improve this model. The most obvious next step would be to try different reinforcement learning approaches. For example a deep-Q learning model would probably learn the optimal strategy of choosing the banker faster than the value-iteration approach. This would reduce the number of incorrect choices in the beginning, and therefore would probably improve the win rate. In addition using a different set of reward values may improve the rate at which the agent finds the optimal strategy.
import random
​
​
class BaccaratLearning():
    def __init__(self, gamma=0.4):
        """Initialize the agent."""
​
        # the current amount being bet
        # starts at 1
        self.current_bet = 1
        # largest amount won so far
        self.largest_win = 0
        # largest amount lost so far
        self.largest_loss = 0
        # number of consecutive wins the agent has
        self.consecutive_wins = 0
        # record of each game
        # records losses and wins
        self.total_games = []
        # gamma constant for use in value iteration
        self.gamma = gamma
        # dictionary to hold tuple of (state, action) and value
        self.value_dict = {}
        # total rounds
        self.total_rounds = 0
        # total amount the player has
        self.total_amount = 100
        # game won
        self.games_won = 0
        # total win money
        self.net_gain = 0
        # the amount of games since the last win
        self.last_win = 0
​
    def round_values(self, value, base, digits=2):
        """Round a value to a given base"""
        val = round(float(value)/float(base), digits)
        return val*10
​
    def amount_update(self, value):
        """Increment the amount by the value won."""
        self.total_amount += value
​
    def count_val(self, val, lst):
        """
            Count the occurences of a value in a list.
            Used to calculate the number of wins, losses, etc.
        """
        return lst.count(val)
​
    def get_current_state(self):
        """Return the current state as a tuple."""
        return (self.last_win, self.consecutive_wins, self.current_bet)
​
    def get_win_proportion(self):
        """Get the proportion of games won."""
        return round(self.games_won/self.total_rounds, 2)
​
    def explore_next_state(self, state_value):
        """
            Explore a new state in the values table.
            The agent searches for the next state in the values table.
        """
        # next state and next state value
        next_round = {}
        next_state_value = 0
        # iterate through index and states
        for index, state in enumerate(state_value):
            # if index is 0 get value at state
            # if it does not exist create new key
            if index == 0:
                try:
                    next_round = self.value_dict[str(state)]
                except:
                    self.value_dict[str(state)] = {}
                    next_round = self.value_dict[str(state)]
            # if index is at the end
            # get the next state value
            # if value does not exists
            # return random
            elif index == len(state_value)-1:
                try:
                    next_state_value = next_round[str(state)]
                except:
                    next_state_value = 10*random.random()
                    next_round[str(state)] = next_state_value
            # if index is between beginning and end
            # get the next round state
            # else initialize a new round state
            else:
                try:
                    next_round = next_round[str(state)]
                except:
                    next_round[str(state)] = {}
                    next_round = next_round[str(state)]
        # return the next state value
        return next_state_value
​
    def value_update(self, state_rep, value):
        """
            Update the state with a new value.
            Search for the state and update the value.
        """
​
        # next round value
        next_round = {}
        # for each index and state in the state
        for index, state in enumerate(state_rep):
            # if index is 0 get the next round value
            # if it does not exists create new key
            if index == 0:
                try:
                    next_round = self.value_dict[str(state)]
                except:
                    self.value_dict[str(state)] = {}
                    next_round = self.value_dict[str(state)]
            # if index is the last value in state_rep
            # set the value
            elif index == len(state_rep)-1:
                next_round[str(state)] = value
            # else get the next round
            # if it does not exists create a new state
            else:
                try:
                    next_round = next_round[str(state)]
                except:
                    next_round[str(state)] = {}
                    next_round = next_round[str(state)]
​
    def win_amount(self, bet):
        """Get the amount won for choosing the correct hand."""
        # last win is 0 away as the agent one
        # increment consecutive wins
        # add new bet
        return self.explore_next_state((0, self.consecutive_wins + 1, bet))
​
    def loss_amount(self, bet):
        """Get the amount lost if the agent chooses the wrong hand. """
​
        # wins since last win is incremented
        # consective wins goes to 0
        # new bet is passed in
        return self.explore_next_state((self.last_win+1, 0, bet))
​
    def baccarat_bet_price(self, bet):
        """
            Return how much the agent bets.
            There are 8 different bets the agent can make.
​
            1: bet the same as the current bet
            2: 2x current bet
            3: 3x current bet
            4: 4x current bet
            5: 1 unit
            6: 2 units
            7: 4 units
            8: 8 units
        """
        current_bet = self.current_bet
        bets = {1: current_bet, 2: 2*current_bet, 3: 3*current_bet,
                4: 4*current_bet, 5: 1, 6: 2, 7: 4, 8: 8}
        return bets[bet]
​
    def value_function(self):
        """
            Value iteration function.
            Function iterates though the 8 possible moves one at a time.
            Agent then bets using the amount dictated by the move.
            The estimated amount won is then calculated
            using the probabilities of each side (dealer, agent, tie)
            given that the agent bet on the dealer
            since dealer has the highest probability of winning.
            The maximum earned amount is updated and the best move is updated.
​
            Function uses the Bellman equation to update the state
            with a provided gamma value.
        """
​
        # intialize max total and best move
        max_total = -999
        best_move = -999
        # iterate through moves
        for move in range(1, 9):
            # get current bet amount from move list
            current_bet = self.baccarat_bet_price(move)
            # calculate amounts for dealer, agent, and tie
            dealer_amt = 0.4585*self.win_amount(current_bet)
            agent_amt = 0.4462*self.loss_amount(current_bet)
            tie_amt = 0.0953*self.explore_next_state(self.get_current_state())
            # get total amount
            current_total = dealer_amt + agent_amt + tie_amt
            # check if current total is greater than max
            # if it is replace max with the current total
            # and set the best move to the current move
            if current_total > max_total:
                max_total = current_total
                best_move = move
​
        # update the state value for the best move
        # using the max total and the gamme constant
        self.value_update(self.get_current_state(), self.gamma * max_total)
        # return the best move
        return best_move
​
    def agent_bet_choice(self):
        """
            Agent chooses the optimal amount to bet
            as well as chooses sends out a default guess
            for the winning hand.
        """
​
        # if the total amount is 0 then the agent has lost
        if self.total_amount == 0:
            print("The agent lost the game.")
            return
        # get the amount to be bet
        bet_amount = self.baccarat_bet_price(self.value_function())
        # check if bet amount is greater than total amount
        # if so reduce the bet amount to the total amount
        if bet_amount > self.total_amount:
            bet_amount = self.total_amount
        # update current bet
​
        # set current bet to the bet amount
        self.current_bet = bet_amount
        # reduce the total amount by the amount bet
        self.total_amount -= bet_amount
        # return the bet amount as well as a default guess of the dealer
        return 1, bet_amount
​
    def class_attribute_update(self, value):
        """
            General update based on previous game.
            The attributes of the instance are updated
            depending on the outcome of the previous game.        
        """
        # increase the total number of rounds
        self.total_rounds += 1
        # check the result of the game
        if value == 0:
            result = 'lose'
        elif value == self.current_bet:
            result = 'tie'
        else:
            result = 'win'
        # add the result to the rest of the games
        self.total_games.append(result)
        # get current bet
        current_bet = self.current_bet
        # tie - nothing is changed
        if value == current_bet:
            return
​
        # previous game was a loss
        elif value == 0:
            # set consecutive wins to 0
            self.consecutive_wins = 0
            # add 1 to games since last win
            self.last_win += 1
            # remove bet from net gain
            self.net_gain -= self.current_bet
            # check to see if the current bet is less than the largest loss
            # if so replace the largest loss with the current bet
            if self.largest_loss > -self.current_bet:
                self.largest_loss = -(self.current_bet)
​
        # previous game was a win
        else:
            # increment games won
            self.games_won += 1
            # increase net gain by the value - current bet
            self.net_gain += (value - self.current_bet)
            # increase number of consecutive wins
            self.consecutive_wins += 1
            # reduce wins since last consecutive win to 0
            self.last_consecutive_wins = 0
            # check if value - current bet is more than largest win
            # if so replace largest win with the value - current bet
            if self.largest_win < (value - self.current_bet):
                self.largest_win = value - self.current_bet
​
    def print_game_statistics(self):
        """Prints game statistics for agent."""
​
        print("Total number of deals played: " + str(self.total_rounds))
        print("Total number of deals won: " + str(self.games_won))
        print("Percentage of deals won: " +
              str(self.get_win_proportion()*100) + " %")
        print("Largest amount won: " + str(self.largest_win))
        print("Largest amount lost: " + str(self.largest_loss))
