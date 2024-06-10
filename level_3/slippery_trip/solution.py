from typing import List
# Write any import statements here

def getMaxCollectableCoins(R: int, C: int, G: List[List[str]]) -> int:
    # Write your code here

    def get_row_stats(row):
        contains_right = contains_down = contains_coin = False
        is_passable = False
        for x in G[row]:
            if x != '>':
                is_passable = True
            if x == '>':
                contains_right = True
            elif x == 'v':
                contains_down = True
            elif x == '*':
                contains_coin = True
        
        return contains_right, contains_down, contains_coin, is_passable

    def get_max_coins(row):
        max_coins = cur_coins = 0
        takeable = False
        for x in G[row] * 2:
            if x == '>':
                takeable = True
            if takeable:    
                if x == 'v':
                    max_coins = max(max_coins, cur_coins)
                    cur_coins = 0
                    takeable = False
                elif x == '*':
                    cur_coins += 1
        return max_coins

    res = 0
    for r in range(R - 1, -1, -1):
        contains_right, contains_down, contains_coin, is_passable = get_row_stats(r)
        if not is_passable:
            res = 0
        elif contains_right and contains_down:
            res += get_max_coins(r)
        elif contains_right:
            all_coins = sum(int(x == '*') for x in G[r])
            res = max(all_coins, int(contains_coin) + res)
        elif is_passable:
            res += int(contains_coin)
    
    return res


if __name__ == '__main__':

    R = 3
    C = 4
    G = [['.', '*', '*', '*'], ['*', '*', 'v', '>'], ['.', '*', '.', '.']]
    print(getMaxCollectableCoins(R, C, G))

    R = 3
    C = 3
    G = [['>', '*', '*'], ['*', '>', '*'], ['*', '*', '>']]
    print(getMaxCollectableCoins(R, C, G))

    R = 2
    C = 2
    G = [['>', '>'], ['*', '*']]
    print(getMaxCollectableCoins(R, C, G))

    R = 4
    C = 6
    G = [['>', '*', 'v', '*', '>', '*'], ['*', 'v', '*', 'v', '>', '*'], ['.', '*', '>', '.', '.', '*'], ['.', '*', '.', '.', '*', 'v']]
    print(getMaxCollectableCoins(R, C, G))
