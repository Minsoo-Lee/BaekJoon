#include <iostream>
#include <queue>
#include <vector>

using namespace std;

bool check[100];
vector<int> _vector[101];

int bfs(int start) {
    queue<int> _queue;
    int count = 0;
    _queue.push(start);
    check[start] = true;
    while (!_queue.empty()) {
        int x = _queue.front();
        _queue.pop();
        count++;
        for (int i = 0; i < _vector[x].size(); i++) {
            int y = _vector[x][i];
            if (!check[y]) {
                _queue.push(y);
                check[y] = true;
            }
        }
    }
    return count - 1;
}

int main(void) {
    int node, edge;
    cin >> node >> edge;
    for (int i = 0; i < edge; i++) {
        int a, b;
        cin >> a >> b;
        _vector[a].push_back(b);
        _vector[b].push_back(a);
    }
    cout << bfs(1) << endl;
    return 0;
}
