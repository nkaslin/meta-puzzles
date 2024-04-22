#include <bits/stdc++.h>
using namespace std;
// Write any include statements here

int find_cycle(int node, vector<int>& L, vector<bool>& visited) {
    int turtoise = L[node];
    int hare = L[L[node]];
    while (turtoise != hare) {
        if (visited[turtoise]) {
            return -1;
        }
        visited[turtoise] = true;
        turtoise = L[turtoise];
        hare = L[L[hare]];
    }
    return turtoise;
}

void mark_cycle(int start, vector<int>& L, vector<bool>& visited, vector<int>& cycle_size) {
    int node = L[start];
    int size = 1;
    while (node != start) {
        visited[node] = true;
        size++;
        node = L[node];
    }
    cycle_size[start] = size;
    node = L[start];
    while (node != start) {
        cycle_size[node] = size;
        node = L[node];
    }
    return;    
}

int getMaxVisitableWebpages(int N, vector<int> L) {
    // Write your code here
    for (int i = 0; i < N; i++) L[i]--;

    vector<int> cycle_size(N, 1);
    vector<bool> sources(N, true);
    vector<bool> visited(N, false);
    int start;
    for (int node = 0; node < N; node++) {
        sources[L[node]] = false;
        if (visited[node]) {
            continue;
        }
        start = find_cycle(node, L, visited);
        if (start != -1) {
            mark_cycle(start, L, visited, cycle_size);
        }
        visited[node] = true;
    }

    int sol = 0;
    int cur, cur_len;
    for (int i = 0; i < N; i++) sol = max(sol, cycle_size[i]);
    for (int node = 0; node < N; node++) {
        if (!sources[node]) {
            continue;
        }
        cur = node;
        cur_len = 0;
        while (cycle_size[cur] == 1) {
            cur = L[cur];
            cur_len++;
        }
        cur_len += cycle_size[cur];
        sol = max(sol, cur_len);
    }
    return sol;
}