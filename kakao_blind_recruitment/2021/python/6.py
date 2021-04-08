# 1
from collections import deque

DIRECTION = [(0,1), (0, -1), (1, 0), (-1, 0)]

def is_clear(b):
    if b.count("0") == 16:
        return True

    return False

def move_at_a_time(b, y, x, dy, dx):
    ny, nx = y + dy, x + dx
    if ny >= 0 and ny < 4 and nx >= 0 and nx < 4 and b[4 * ny + nx] == "0":
        return move_at_a_time(b, ny, nx, dy, dx) 
    else:
        if ny >= 0 and ny < 4 and nx >= 0 and nx < 4:
            return (ny, nx)
        else:
            return (y, x)

def remove_cards(b, card):
    b = b.replace(card, "0")
    return b

def solution(board, r, c):
    answer = 0

    board_str = ""

    for i in range(4):
        for j in range(4):
            board_str += str(board[i][j])

    cnt = 0
    enter = -1
    q = deque()
    q.append((r, c, board_str, cnt, enter))
    is_visited = set()

    while q:
        y, x, b, c, e = q.popleft()
        position = 4 * y + x
        
        if (y, x, b, e) in is_visited:
            continue
        is_visited.add((y, x, b, e))

        if is_clear(b):
            return c
        
        # 4 방향 이동
        for (Dy, Dx) in DIRECTION:
            ny, nx = y + Dy, x + Dx
            if ny >= 0 and ny < 4 and nx >= 0 and nx < 4:
                q.append((ny, nx, b, c+1, e))
            
        # Ctrl + 4 방향 이동
        for (Dy, Dx) in DIRECTION:
            ny, nx = move_at_a_time(b, y, x, Dy, Dx)
            if ny == y and nx == x:
                continue
            q.append((ny, nx, b, c+1, e))


        # Enter를 누르는 경우
        if board_str[position] != 0:
            if e == -1:
                new_enter = position
                q.append((y, x, b, c+1, new_enter))
            else:
                if e != position and b[e] == b[position]:
                    b = remove_cards(b, b[e])
                    q.append((y, x, b, c+1, -1))

    return answer

board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0

answer = solution(board, r, c)
print(answer)
