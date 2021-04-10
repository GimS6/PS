#2

from collections import deque

DIRECTION = [(0,1), (0, -1), (1, 0), (-1, 0)]

def is_game_clear(b):
    if b.count("0") == 16:
        return True
    return False

def move_with_ctrl(b, y, x, ty, tx):
    ny, nx = y + ty, x + tx
    # 한 방향으로 이동했을 때 0이면
    if ny >= 0 and ny < 4 and nx >= 0 and nx < 4 and b[4 * ny + nx] == "0":
        # 한 번 더 이동해본다.
       return move_with_ctrl(b, ny, nx, ty, tx)
    else:
        # 카드를 만났을 때
        if ny >= 0 and ny < 4 and nx >= 0 and nx < 4:
            return (ny, nx)
        # 이동을 할 수 없을 때
        else:
            return (y, x) 

def clear_cards(b, entered_card):
    b = b.replace(entered_card, "0")
    return b

def solution(board, r, c):
    # 방향키를 입력할 때

    # Ctrl + 방향키를 입력할 때

    # Enter키를 입력할 때
    #   - 앞면이 보이는 카드가 1장뿐이라면 그림을 맞출 수가 없으므로 
    #   두 번째 카드를 뒤집을 때까지 앞면을 유지
    #   - 앞면이 보이는 카드가 2장이 된 후, 두 개의 그림이 같으면
    #   화면에서 사라진다. 다르면 둘 다 다시 뒤집힌다.

    # 키 조작횟수의 최솟값을 알아야 한다.
    answer = 0
    board_str = ""

    for i in range(4):
        for j in range(4):
            board_str += str(board[i][j])

    count = 0
    entered_position = -1
    is_visited = set()

    q = deque()
    q.append((r, c, board_str, count, entered_position))

    # 4 * 4 크기의 보드
    while q:
        y, x, b, c, e = q.popleft()
        position = 4 * y + x

        # 방문했는지 확인
        if (y, x, b, e) in is_visited:
            continue
        is_visited.add((y, x, b, e))

        # 카드가 모두 제거 됐는지 확인
        if is_game_clear(b):
            return int(c)

        # 4방향 이동
        for (to_y, to_x) in DIRECTION:
            ny, nx = y + to_y, x + to_x     
            if ny >= 0 and ny < 4 and nx >= 0 and nx < 4:
                q.append((ny, nx, b, c+1, e))

        # Ctrl + 방향키 이동
        for (to_y, to_x) in DIRECTION:
            ny, nx = move_with_ctrl(b, y, x, to_y, to_x)
            if ny == y and nx == x:
                continue
            q.append((ny, nx, b, c+1, e))

        # Enter를 눌렀을 때
        if board_str[position] != 0:
            if e == -1:
                new_enter = position
                q.append((y, x, b, c+1, new_enter))
            else:
                if e != position and b[e] == b[position]:
                    b = clear_cards(b, b[e])
                    q.append((y, x, b, c+1, -1))

    return answer


board = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
r = 0
c = 1 

answer = solution(board, r, c)
print(answer)