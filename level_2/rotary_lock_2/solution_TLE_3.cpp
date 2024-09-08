#include <bits/stdc++.h>
using namespace std;
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <climits>

// TLE on 5/32 test cases

long long getMinCodeEntryTime(int N, int M, vector<int> C) {

    auto dist = [&](int x, int y) {
        return min((x + N - y) % N, (y + N - x) % N);
    };

    unordered_map<int, int> icm;
    vector<int> rev_icm;
    icm[1] = 0;
    rev_icm.push_back(1);
    int cur = 1;
    for (int c : C) {
        if (icm.find(c) == icm.end()) {
            icm[c] = cur++;
            rev_icm.push_back(c);
        }
    }

    vector<vector<int>> memo(M, vector<int>(rev_icm.size(), -1));

    function<int(int, int)> dp = [&](int i, int j) -> int {
        if (i == M) return 0;

        if (memo[i][j] != -1) return memo[i][j];

        int p = rev_icm[j];

        int dist1 = dist(p, C[i]);
        int dist2 = dist(C[i - 1], C[i]);

        memo[i][j] = min(
            dist1 + dp(i + 1, icm[C[i - 1]]), 
            dist2 + dp(i + 1, j)
        );

        return memo[i][j];
    };

    return dist(1, C[0]) + dp(1, 0);
}