# Battleship

You're playing Battleship on a grid of cells with $R$ rows and $C$ columns. There are $0$ or more battleships on the grid, $i$-th row from the top and $j$-th column from the left either contains a battleship ($G_{i,j} = 1$) or doesn't ($G_{i,j} = 0$).

You're going to fire a single shot at a random cell in the grid. You'll choose this cell uniformly at random from the $R\cdot C$ possible cells. You're interested in the probability that the cell hit by your shot contains a battleship.

Your task is to implement the function getHitProbability($R$, $C$, $G$) which returns this probability.
Note: Your return value must have an absolute or relative error of at most $10^{-6}$ to be considered correct.

## Constraints
$1 \leq R, C \leq 100$\
$0 \leq G_{i,j} \leq 1$

## Solution
<details>
  <summary>Spoiler</summary>
  ...
</details>