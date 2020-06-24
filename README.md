# Baccarat

![Image of Baccarat Board]
(https://cdn.chatsports.com/cache/3c/2f/3c2fc8415779bd3a34c625b955ac8df8-original.jpg)

## Baccarat Overview

Baccarat is a popular card game played in casinos across the country. Baccarat's popularity has brought with it several variations such as punto bacno, baccarat chemin de fer, and baccarat banque.

The rules of baccarat are simple. Each coup (round of play) the player and banker are dealt cards which have different point values. Numeric cards 2-9 in each suit are worth their face value. Face cards like the jack, queen and king have no point value (worth 0 points), aces are worth 1 point, and the jokers are not used. The value of a hand depends on the units digit of the sum of the hand.

For example:

If the player has cards with the value 2 and 3, then the total value if 5. However if the player has cards with the value 6 and 8, then the total value is 4 since the units digit of the total, 14, is 4.

Each round the player must choose between three choices: player wins, banker wins, or tie and depending on the outcome the player is either rewarded a certain monetary amount or loses the betted amount.


For the sake of this game the amount returned will be mapped as follows:


x - x: Agent correctly bet on x (highest hand) and won the round.

The various choices are:

  agent - agent: 100% of amount returned
  
  agent - dealer: 75% of amount returned
  
  agent - tie: 800% of amount returned

This amounts were calculated based on the probability of each hand winning which converges to the given probabilties:

These probabilties were taken from this [website](https://wizardofodds.com/games/baccarat/basics/).

  Player wins: 0.446247
  
  Banker wins: 0.458597
  
  Neither/tie: 0.095156

## File Layout

This project is divided into several files.

[Baccart.py](https://github.com/SrikarMurali/Baccarat/blob/master/Baccarat.py) - contains functions for starting and running a game of baccarat.

[BaccaratProcess.py](https://github.com/SrikarMurali/Baccarat/blob/master/BaccaratProcess.py) - class to deal with the baccarat processes. This class deals the cards, calculates the return amounts, updates states and values, etc.

[BaccaratLearning.py](https://github.com/SrikarMurali/Baccarat/blob/master/BaccaratLearning.py) - this is the class where the reinforcement learning occurs. Here the agent explores the states, bets, and determines the best methodology to win each round.

[TestBaccarat.ipynb](https://github.com/SrikarMurali/Baccarat/blob/master/TestBaccarat.ipynb) - this python notebook contains a test simulation of the agent and plots the proportion of wins the agent had. This notebook also contains an interpretation of the results as well as an analysis of why certain things did or did not work. Potential future improvements are also discussed in this notebook.

## Reinforcement Framerwork

Baccarat can easily be framed as a reinforcement learning problem.

Sequential: This simulation can be run indefinitely, however it will most likely take several thousand iterations for the agent to learn the optimal strategy.

Environment: The environment is the Baccarat game. A simulation of the game will be created in which there will be a player and a banker. Each turn one deal is dealt and the player gets to choose which hand has a higher point value or if a tie exists. The deals will be simulated based on the actual probabilities for each choice.

Agent: The agent is the player in a Baccarat game. Each turn they have three choices; they can bet on the player, on the banker, or bet on a tie. These three choices will be given each round. The agent will be rewarded the units bet if correct and would lose said units if incorrect; the reward in this context is a monetary amount.

Example State: One example state is that the agent is deciding between the three choices and picks that the banker will win. The cards are revealed and it is shown that the banker did indeed win. Thus the agent is in the state where it chose correctly and will hence be rewarded.

Example Reward: An example of a reward would occur if the agent chose the action that coincides with the highest value. In this case they would be rewarded the total monetary units that were at play at the time. If the agent chose incorrectly then they would lose the amount of units that the agent bet.

##Prior Work

There have been several pieces of work related to reinforcement learning and Baccarat.

Modeling, Simulation, and Analysis of Baccarat: A Critical View of Card Counting, Odds, and Bets by D.Madewell.

This paper discusses how the game of Baccarat can be turned into a reinforcement learning problem and how an optimal strategy can be found.

The House Always Wins: Simulating 5,000,000 Games of Baccarat a.k.a Punto Banco by Paul Vanderlanken

This article discusses a simulation for Baccarat on how to find the optimal strategy. This article showcases how Baccarat could be simulated to find the optimal strategy.
