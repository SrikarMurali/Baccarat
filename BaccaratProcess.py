from BaccaratLearning import *


class BaccaratProcess():
    def __init__(self):
        """Initialize a blank state."""
        self.total_agents = []  # total agents
        self.in_play = []  # number of agents in play
        self.starting_amount = 100  # basic starting amount
        self.in_play.append(BaccaratLearning())  # add single agent to inplay

    def return_value_table_pair(self):
        """Return a value pair from the player."""
        return self.total_agents[0].Value

    def set_value_table_pair(self, vtable):
        """Set a new value for a player"""
        self.total_agents[0].Value = vtable

    def deal_cards(self):
        """
            Deal cards for a round of Baccarat.
            Deals are simulated based on true odds of each hand winning.
            Odds were retreived from: https://wizardofodds.com/games/baccarat/basics/

            Player wins: 0.446247
            Dealer wins: 0.458597
            neither/tie: 0.095156
        """
        # use builtin random function to get probability
        deal_prob = random.uniform(0, 1)
        # player wins the round
        if deal_prob < .4462:
            return 0
        # dealer wins the round
        elif deal_prob < .9047:
            return 1
        # else game is a tie
        return 2

    def return_amounts(self, true_outcome, agent_guess, amount_bet):
        """
            Calculates how much needs to be returned to the player.
            Changes depending on if there was a win, loss or tie.

            x - x: Agent correctly bet on x (highest hand) and won the round.

            The various choices are:
                agent-agent: 100% of amount returend
                agent-dealer: 75% of amount returned
                agent-tie: 800% of amount returned
            Agent do not lose amount if there is a tie even if it did not bet on a tie.
            Otherwise if the agent chooses wrongly it loses the amount it bet. 
            Since the probability of getting a tie is very low,
            the reward is far greater if the agent chooses correctly.
            The other reward probabilities are also calculated based
            on likelihood of winning.
        """
        # tie game
        if true_outcome == 2:
            # guess correct, return 800% of amount bet (return 9x)
            if true_outcome == agent_guess:
                return 9*float(amount_bet)
            # since it is a tie, nothing is lost for guessing incorrectly
            else:
                return amount_bet
        # agent or dealer wins
        else:
            # agent guesses the correct hand
            if true_outcome == agent_guess:
                # agent hand wins, return 100% of amount bet (return 2x)
                if true_outcome == 0:
                    return 2*float(amount_bet)
                # dealer hand wins, return 75% of amount bet (return 1.95x)
                elif true_outcome == 1:
                    return 1.75*float(amount_bet)
        # if not tie and an incorrect guess
        # agent loses amount bet
        return 0

    def state_update(self):
        """
            Deal the cards (get the winning hand using probabilities).
            Calculate the agents guess and the amount bet.
            Enumerate through the guesses and calculate the amount to return.
            Update the agents state.
        """
        # get winning hand
        result = self.deal_cards()
        # get the agents guess
        guesses = []
        for p in self.in_play:
            guesses.append(p.agent_bet_choice())
        # calculate the amount to be returned
        for i, guess in enumerate(guesses):
            # get agent
            agent = self.in_play[i]
            # get and increment the return amount
            value = self.return_amounts(result, guess[0], guess[1])
            agent.amount_update(value)
            # update the agents state
            agent.class_attribute_update(value)
            # remove agent if amount drops to 0
            if agent.total_amount == 0:
                self.total_agents.append(agent)
                self.in_play.remove(agent)