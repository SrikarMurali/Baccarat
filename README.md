# Baccarat


## Baccarat Overview

Baccarat is a popular card game played in casinos across the country. Baccarat's popularity has brought with it several variations such as punto bacno, baccarat chemin de fer, and baccarat banque.

The rules of baccarat are simple. Each coup (round of play) the player and banker are dealt cards which have different point values. Numeric cards 2-9 in each suit are worth their face value. Face cards like the jack, queen and king have no point value (worth 0 points), aces are worth 1 point, and the jokers are not used. The value of a hand depends on the units digit of the sum of the hand.

I.E

If the player has cards with the value 2 and 3, then the total value if 5. However if the player has cards with the value 6 and 8, then the total value is 4 since the units digit of the total, 14, is 4.

Each round the player must choose between three choices: player wins, banker wins, or tie and depending on the outcome the player is either rewarded a certain monetary amount or loses the betted amount.


For the sake of this game the amount returned will be mapped as follows:


x - x: Agent correctly bet on x (highest hand) and won the round.

The various choices are:

  agent - agent: 100% of amount returned
  
  agent - dealer: 75% of amount returned
  
  agent - tie: 800% of amount returned

This amounts were calculated based on the probability of each hand winning which converges to the given probabilties:

These probabilties were taken from https://wizardofodds.com/games/baccarat/basics/.

  Player wins: 0.446247
  
  Banker wins: 0.458597
  
  Neither/tie: 0.095156

## File Layout

This project is divided into several files.

[Baccart.py](https://github.com/SrikarMurali/Baccarat/blob/master/Baccarat.py) - contains functions for starting and running a game of baccarat.

BaccaratProcess.py 

