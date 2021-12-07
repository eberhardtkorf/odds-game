# odds-game

This script calculates the probability of a dare being executed in the "odds-on" game given the range of numbers both players can use.

## Theoretical Part

Formulas have been derived to calculate the probability given the range,

Even range: `p = (2*n-2)/(n*n)`

Odd range: `p = (2*n-1)/(n*n)`

## Simulation Part

We can simulate a number of random plays of the game and calculate the probability of a dare being executed given the range.

## Remarks

We can see that the simulated probability converges to the theoretical probability when thousands or millions of simulations are tested, indicating that the theoritcal formulas are correct.


