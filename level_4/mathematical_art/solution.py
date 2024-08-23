from heapq import heappop, heappush
from typing import List


class FenwickTree:
    def __init__(self, arr: List[int]) -> None:
        """
        O(nlogn) construction of the Fenwick Tree from the input array.
        """
        self.n = len(arr)
        self.tree = [0] * (self.n + 1)
        for i, val in enumerate(arr):
            self.update(i, val)

    def update(self, i: int, val: int) -> None:
        """
        Adds the value val to the element at index i in the array in O(logn).
        """
        i += 1
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def query(self, i: int) -> int:
        """
        Returns the sum of the first i elements in the array in O(logn).
        """
        i += 1
        res = 0
        while i:
            res += self.tree[i]
            i -= i & -i
        return res
    
    def range_query(self, i: int, j: int) -> int:
        """
        Returns the sum of the elements in the range [i, j] in the array in O(logn).
        """
        if i > j:
            return 0
        return self.query(j) - self.query(i - 1)


# implementation from https://leetcode.com/problems/merge-intervals/submissions/1365896411/
def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
        
    merged = []

    xprev, yprev = None, None
    for x, y in sorted(intervals):
        
        if xprev is None and yprev is None:
            xprev, yprev = x, y
            continue
        
        if x > yprev:
            merged.append([xprev, yprev])
            xprev, yprev = x, y
        else:
            yprev = max(yprev, y)

    merged.append([xprev, yprev])

    return merged


def getPlusSignCount(N: int, L: List[int], D: str) -> int:
    
    ver, hor = {}, {}

    cur = [0, 0]
    for dr, steps in zip(D, L):
        if dr == "U":
            if cur[0] not in ver:
                ver[cur[0]] = []
            ver[cur[0]].append([cur[1], cur[1] + steps])
            cur[1] += steps
        elif dr == "D":
            if cur[0] not in ver:
                ver[cur[0]] = []
            ver[cur[0]].append([cur[1] - steps, cur[1]])
            cur[1] -= steps
        elif dr == "L":
            if cur[1] not in hor:
                hor[cur[1]] = []
            hor[cur[1]].append([cur[0] - steps, cur[0]])
            cur[0] -= steps
        else:
            if cur[1] not in hor:
                hor[cur[1]] = []
            hor[cur[1]].append([cur[0], cur[0] + steps])
            cur[0] += steps

    for y_pos, intervals in hor.items():
        hor[y_pos] = merge_intervals(intervals)

    for x_pos, intervals in ver.items():
        ver[x_pos] = merge_intervals(intervals)

    ver_intervals = []
    for x, l in ver.items():
        for y1, y2 in l:
            ver_intervals.append((x, y1, y2))
    ver_intervals.sort()

    hor_intervals = []
    for y, l in hor.items():
        for x1, x2 in l:
            hor_intervals.append((x1, x2, y))
    hor_intervals.sort()

    all_x_values = set()
    all_y_values = set()
    for x, y1, y2 in ver_intervals:
        all_x_values.add(x)
        all_y_values.add(y1)
        all_y_values.add(y2)

    for x1, x2, y in hor_intervals:
        all_x_values.add(x1)
        all_x_values.add(x2)
        all_y_values.add(y)

    all_x_values = sorted(list(all_x_values))
    all_y_values = sorted(list(all_y_values))

    idx_comp_map_y = {}
    for i, y in enumerate(all_y_values):
        idx_comp_map_y[y] = i

    fwt = FenwickTree([0 for _ in all_y_values])

    hq = []
    ptr_ver = ptr_hor = 0

    res = 0

    while ptr_ver < len(ver_intervals):
        x_ver = ver_intervals[ptr_ver][0] if ptr_ver < len(ver_intervals) else float("inf")
        x_hor_start = hor_intervals[ptr_hor][0] if ptr_hor < len(hor_intervals) else float("inf")
        x_hor_end = hq[0][0] if len(hq) > 0 else float("inf")

        if x_hor_start <= x_ver and x_hor_start <= x_hor_end:
            _, x2, y = hor_intervals[ptr_hor]
            heappush(hq, (x2, y))
            fwt.update(idx_comp_map_y[y], 1)
            ptr_hor += 1
        elif x_hor_end <= x_ver:
            _, y = heappop(hq)
            fwt.update(idx_comp_map_y[y], -1)
        else:
            _, y1, y2 = ver_intervals[ptr_ver]
            y1m, y2m = idx_comp_map_y[y1], idx_comp_map_y[y2]
            res += fwt.range_query(y1m + 1, y2m - 1)
            ptr_ver += 1

    return res


if __name__ == "__main__":

    N = 9
    L = [6, 3, 4, 5, 1, 6, 3, 3, 4]
    D = "ULDRULURD"
    print(getPlusSignCount(N, L, D), 4)  # Expected output: 4

    N = 8
    L = [1, 1, 1, 1, 1, 1, 1, 1]
    D = "RDLUULDR"
    print(getPlusSignCount(N, L, D), 1)  # Expected output: 1

    N = 8
    L = [1, 2, 2, 1, 1, 2, 2, 1]
    D = "UDUDLRLR"
    print(getPlusSignCount(N, L, D), 1)  # Expected output: 1

    N = 18
    L = [7, 5, 6, 9, 5, 8, 4, 7, 3, 6, 2, 5, 1, 8, 4, 4, 8, 10]
    D = "ULDRULDRULDRULURDU"
    print(getPlusSignCount(N, L, D), 16)  # Expected output: 16
