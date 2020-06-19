from BaccaratProcess import *

class Baccarat():  
    def __init__(self):
        """Initialize BaccaratGame object."""
        self.rounds = 1000
        
    def set_rounds(self, rounds):
        """Manually set a number of rounds."""
        self.rounds = rounds
        
    def update_Value_table(self, value_table):
        """Set value in the value table."""
        self.state.set_value_table_pair(value_table)
        
    def play_baccarat(self):
        """
            Play a game of Baccarat for the given number of rounds.
            Print out the statistics after the rounds have finished.
        """
        # for each round update the state
        rounds = self.rounds
        for i in range(rounds):
            self.state.state_update()       
        # get agent and print statistics
        agent = self.state.total_agents[0]
        print('Baccarat Game Statistics for Agent')
        agent.print_game_statistics()
        return agent.get_win_proportion()

    def start_game(self):
        """Method to create a initial state for the game to start."""
        self.state = BaccaratProcess()
