# Rabbit Hole 2

You're having a grand old time clicking through the rabbit hole that is your favorite online encyclopedia. 

The encyclopedia consists of $N$ different web pages, numbered from $1$ to $N$. There are $M$ links present across the pages, the $i$th of which is present on page $A_i$ ​and links to a different page $B_i$. A page may include multiple links, including multiple leading to the same other page. 

A session spent on this website involves beginning on one of the $N$ pages, and then navigating around using the links until you decide to stop. That is, while on page $i$, you may either move to any of the pages linked to from it, or stop your browsing session. 

Assuming you can choose which page you begin the session on, what's the maximum number of different pages you can visit in a single session? Note that a page only counts once even if visited multiple times during the session.


## Constraints

$2 \leq  N \leq 500000$ \
$1 \leq  M \leq 500000$ \
$1 \leq  A_i, B_i \leq N$ \
$A_i \neq B_i$


## Solution
<details>
  <summary>Spoiler</summary>
  First, the graph is simplified by representing strongly connected components with a single node. This is done by applying the Kosaraju's algorithm.
  Then, we obtain a topological ordering of the graph. The topological ordering is used to find the longest path in the graph.
</details>