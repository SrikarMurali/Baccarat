# Baccarat

![Image of Baccarat Board](https://github.com/SrikarMurali/Baccarat/blob/master/Images/baccarat.jpg)

[![Baccarat Learning Video](https://img.youtube.com/vi/frpBkYLnSC8/0.jpg)](https://youtu.be/frpBkYLnSC8)

## Baccarat Overview

Baccarat is a popular card game played in casinos across the country. Baccarat's popularity has brought with it several variations such as punto banco, baccarat chemin de fer, and baccarat banque.

The rules of baccarat are simple. Each coup (round of play) the player and banker are dealt cards which have different point values. Numeric cards, 2-9, in each suit are worth their face value. Face cards like the jack, queen and king have no point value (worth 0 points), aces are worth 1 point, and the jokers are not used. The value of a hand depends on the units digit of the sum of the hand.

For example:

If the player has cards with values 2 and 3, then the total value of the hand is 5. However if the player has cards with values 6 and 8, then the total value is 4 since the units digit of the total, 14, is 4.

Each round the player must choose between three choices: player wins, banker wins, or tie and depending on the outcome the player is either rewarded a certain monetary amount or loses a certain monetary amount.

For the sake of this game the amount returned will be mapped as follows:

x - x: Agent correctly bet on x (highest hand) and won the round.

The various choices are:

  agent - agent: 100% of amount returned
  
  agent - dealer: 75% of amount returned
  
  agent - tie: 800% of amount returned

These amounts were calculated based on the probability of each hand winning.

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

Research Question: Can an agent be trained to play Baccarat without having any prior experience?

Sequential: This simulation can be run indefinitely, however it will most likely take several thousand iterations for the agent to learn the optimal strategy.

Environment: The environment is the Baccarat game. A simulation of the game will be created in which there will be a player and a banker. Each coup, cards are dealt and the player has to choose which hand has a higher point value or if a tie exists. The deals will be simulated based on the actual probabilities for each choice.

Agent: The agent is the player in a Baccarat game. Each turn they have three choices; they can bet on the player, on the banker, or bet on a tie. These three choices will be given each round. The agent will be rewarded units if correct and will lose units if incorrect; the reward in this context is a monetary amount.

Example State: One example state is that the agent is deciding between the three choices and picks that the banker will win. The cards are revealed and it is shown that the banker did indeed win. Thus the agent is in the state where it chose correctly and will hence be rewarded.

Example Reward: An example of a reward would occur if the agent chose the action that coincides with the highest value. In this case they would be rewarded  monetary units. If the agent chose incorrectly then they would lose the amount of units that the agent bet.

## Results

Based on the results from the simulation it appears that the agent was indeed able to learn the optimal strategy of choosing the banker. The overall proportion of wins in close to the proportion that the dealer wins. The difference is most likely due to the actions taken before the agent determines that the optimal strategy is to pick the banker each time.

![Graph of Results](https://github.com/SrikarMurali/Baccarat/blob/master/Images/results.png)

## Prior Work

There have been several pieces of work related to reinforcement learning and Baccarat.

[Modeling, Simulation, and Analysis of Baccarat: A Critical View of Card Counting, Odds, and Bets by D.Madewell](https://www.academia.edu/9891305/Modeling_Simulation_and_Analysis_of_Baccarat_A_Critical_View_of_Card_Counting_Odds_and_Bets)

This paper discusses how the game of Baccarat can be turned into a reinforcement learning problem and how an optimal strategy can be found.

[The House Always Wins: Simulating 5,000,000 Games of Baccarat a.k.a Punto Banco by Paul Vanderlanken](https://paulvanderlaken.com/2018/01/10/baccarat-simulation-payoff/)

This article discusses a simulation on how to find the optimal baccarat strategy. This article showcases how baccarat could be simulated to find the optimal strategy.



