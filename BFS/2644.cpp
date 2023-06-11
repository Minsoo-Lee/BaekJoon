#include <iostream>
#include <queue>
#define MAX 102

using namespace std;

int n, m;
vector<int> _vector[101];
int check[101];

int bfs(int x, int y) {
    queue<int> _queue;
    _queue.push(x);
    check[x] = 0;
    while (!_queue.empty()) {
        int next = _queue.front();
        if (next == y) {
            return check[y];
        }
        for (int i = 0; i < _vector[next].size(); i++) {
            if (!check[_vector[next][i]]){
                check[_vector[next][i]] = check[next] + 1;
                _queue.push(_vector[next][i]);
            }
        }
        _queue.pop();
    }
    return -1;
}

int main(void) {
    int x, y;
    cin >> n >> x >> y >> m;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        _vector[a].push_back(b);
        _vector[b].push_back(a);
    }
    cout << bfs(x, y) << endl;
}
