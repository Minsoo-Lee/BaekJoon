board = str(input())

def num_X(data):
    count = 0
    if data < len(board) - 1:
        while board[data] == 'X':
            count += 1
            data += 1
    return count

def polyomino_func():
    result = []
    index = 0
    while index < len(board):
        count = 0
        if board[index] == 'X':
            while index < len(board) and board[index] == 'X':
                count += 1
                index += 1
        elif board[index] == '.':
            result.append('.')
            index += 1
            continue
        if count % 2 != 0:
            print(-1)
            return
        count_A = (count // 4) * 4
        count %= 4
        count_B = (count // 2) * 2
        for _ in range(count_A):
            result.append('A')
        for _ in range(count_B):
            result.append('B')
    for i in range(len(result)):
        print(result[i], end = "")
        
polyomino_func()