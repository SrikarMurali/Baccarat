import random

class BaccaratLearning():
    def __init__(self, gamma = 0.4):
        """Initialize the agent."""
        
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

      

    def round_values(self, value, base, digits=2):
        """Round a value to a given base"""
        val = round(float(value)/float(base), digits)
        return val*10
   
    def amount_update(self, value):
        """Increment the amount by the value won."""
        self.total_amount += value

    def count_val(self, val, lst):
        """
            Count the occurences of a value in a list.
            Used to calculate the number of wins, losses, etc.
        """
        return lst.count(val)
    
    def get_current_state(self):
        """Return the current state as a tuple."""
        return (self.last_win, self.consecutive_wins, self.current_bet)

    def get_win_proportion(self):
        """Get the proportion of games won."""
        return round(self.games_won/self.total_rounds,2)

    def explore_next_state(self, state_value):
        """
            Explore a new state in the values table.
            The agent searches for the next state in the values table.
        """
        # next state and next state value
        next_round = {}
        next_state_value = 0
        # iterate through index and states
        for index,state in enumerate(state_value):
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

    def value_update(self, state_rep, value):
        """
            Update the state with a new value.
            Search for the state and update the value.
        """
  
        # next round value
        next_round = {}
        # for each index and state in the state
        for index,state in enumerate(state_rep):
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


    def win_amount(self, bet):
        """Get the amount won for choosing the correct hand."""
        # last win is 0 away as the agent one
        # increment consecutive wins
        # add new bet
        return self.explore_next_state((0, self.consecutive_wins + 1, bet))

    def loss_amount(self, bet):
        """Get the amount lost if the agent chooses the wrong hand. """

        # wins since last win is incremented
        # consective wins goes to 0
        # new bet is passed in
        return self.explore_next_state((self.last_win+1, 0, bet))

    def baccarat_bet_price(self, bet):
        """
            Return how much the agent bets.
            There are 8 different bets the agent can make.
            
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
                4: 4*current_bet, 5: 1, 6: 2, 7:4, 8:8}
        return bets[bet]


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
            
            Function uses the Bellman equation to update the state
            with a provided gamma value.
        """
        
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

        # update the state value for the best move
        # using the max total and the gamme constant
        self.value_update(self.get_current_state(), self.gamma * max_total)
        # return the best move
        return best_move
 
    def agent_bet_choice(self):
        """
            Agent chooses the optimal amount to bet
            as well as chooses sends out a default guess
            for the winning hand.
        """
        
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
        
        # set current bet to the bet amount
        self.current_bet = bet_amount
        # reduce the total amount by the amount bet
        self.total_amount -= bet_amount
        # return the bet amount as well as a default guess of the dealer
        return 1, bet_amount
    
    def class_attribute_update(self, value):
        """
            General update based on previous game.
            The attributes of the instance are updated
            depending on the outcome of the previous game.        
        """
        # increase the total number of rounds
        self.total_rounds += 1
        # check the result of the game
        if value == 0: result = 'lose'
        elif value == self.current_bet: result = 'tie'
        else: result = 'win'
        # add the result to the rest of the games
        self.total_games.append(result)
        # get current bet
        current_bet = self.current_bet
        # tie - nothing is changed
        if value == current_bet:
            return

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

    def print_game_statistics(self):
        """Prints game statistics for agent."""

        print("Total number of deals played: " + str(self.total_rounds))
        print("Total number of deals won: " + str(self.games_won))
        print("Percentage of deals won: " + str(self.get_win_proportion()*100) + " %") 
        print("Largest amount won: " + str(self.largest_win))
        print("Largest amount lost: " + str(self.largest_loss))
