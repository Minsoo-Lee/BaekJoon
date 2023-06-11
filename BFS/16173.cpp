#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int N;
int map[4][4];
bool visited[4][4];
pair<int, int> dir[2] = {{1, 0}, {0, 1}};

bool bfs() {
    queue<pair<int, int>> q;
    visited[1][1] = true;
    q.push({1, 1});
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        if (map[x][y] == -1)
            return true;
        for (int i = 0; i < 2; i++) {
            int dx = x + dir[i].first * map[x][y];
            int dy = y + dir[i].second * map[x][y];
            if (dx >= 1 && dx <= N && dy >= 1 && dy <= N) {
                if (visited[dx][dy] == true)
                    continue;
                visited[dx][dy] = true;
                q.push({dx, dy});
            }
        }
    }
    return false;
}

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> map[i][j];
            visited[i][j] = false;
        }
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << map[i][j] << "[" << visited[i][j] << "] ";
        }
        cout << endl;
    }
    if (bfs() == true)
        cout << "HaruHaru" << endl;
    else
        cout << "Hing" << endl;
}
