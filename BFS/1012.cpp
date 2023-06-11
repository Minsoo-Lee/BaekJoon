#include <iostream>
#include <queue>
#define MAX 50

using namespace std;

int r, c;
int field[MAX][MAX];
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void bfs(int m, int n) {
    queue<pair<int, int>> _queue;
    _queue.push(make_pair(m, n));
    field[m][n] = 0;
    while (!_queue.empty()) {
        int x = _queue.front().first;
        int y = _queue.front().second;
        
        _queue.pop();
        
        for (int i = 0; i < 4; i++) {
            int newX = x + dx[i];
            int newY = y + dy[i];
            if (newX >= 0 && newX < r && newY >= 0 && newY < c) {
                if (field[newX][newY] == 1) {
                    field[newX][newY] = 0;
                    _queue.push(make_pair(newX, newY));
                }
            }
        }
    }
    
}

int main(void) {
    int testCase;
    int cabbage;
    int x, y;
    
    cin >> testCase;
    
    for (int i = 0; i < testCase; i++) {
        cin >> r >> c >> cabbage;
        for (int j = 0; j < cabbage; j++) {
            cin >> x >> y;
            field[x][y] = 1;
        }
        int worm = 0;
        for (int m = 0; m < r; m++) {
            for (int n = 0; n < c; n++) {
                if (field[m][n] == 1) {
                    bfs(m, n);
                    worm++;
                }
            }
        }
        cout << worm << endl;
    }
}
