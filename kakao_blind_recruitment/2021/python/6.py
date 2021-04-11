# 3

from collections import deque
from typing import List

DIRECTION = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def is_game_clear(board: str):
    return True if board.count('0') == 16 else False

def move_with_ctrl(
        y: int, x: int, to_y: int, to_x: int, board: str,
    ):
    ny, nx = y + to_y, x + to_x
    if ny >= 0 and ny < 4 and nx >= 0 and nx < 4 and board[ny*4+nx] == '0':
        return move_with_ctrl(ny, nx, to_y, to_x, board)
    else:
        # 이동한 위치가 카드일 경우
        if ny >= 0 and ny < 4 and nx >= 0 and nx < 4:
            return ny, nx
        # 이동할 곳이 없는 경우
        else:
            return y, x

def remove_cards(board: str, entered_card: int):
    return board.replace(board[entered_card], '0') 


def solution(board: List[List[int]], r: int, c: int):
    answer = 0
    board_str = ''

    for i in range(len(board)):
        board_str += ''.join(map(str, board[i]))

    q = deque() # 탐색할 위치를 담는 큐
    count = 0 # 최소 조작 횟수를 담는 변수
    entered_position = -1 # 카드가 뒤집힌 곳의 위치
    is_visited = set() # 위치를 기억할 set() 변수
    
    q.append((r, c, board_str, count, entered_position))

    while q:
        # 현재 탐색하는 위치
        y, x, b, cnt, ep = q.popleft()
        position = 4 * y + x

        # 이미 탐색했던 위치인지 확인
        if (y, x, b, ep) in is_visited:
            continue
        is_visited.add((y, x, b, ep))

        # 카드를 모두 제거했는지 확인
        if is_game_clear(b):
            return cnt
    
        # 방향키 이동
        for to_y, to_x in DIRECTION:
            ny, nx = y + to_y, x + to_x
            controlled = cnt + 1
            if ny >= 0 and ny < 4 and nx >= 0 and nx < 4:
                q.append((ny, nx, b, controlled, ep))

        # Ctrl + 방향키 이동
        for to_y, to_x in DIRECTION:
            ny, nx = move_with_ctrl(y, x, to_y, to_x, b)
            controlled = cnt + 1
            q.append((ny, nx, b, controlled, ep))

        # 엔터키를 눌렀을 때
        if b[position] != 0:
            if ep == -1:
                new_entered = position
                q.append((y, x, b, cnt+1, new_entered))
            else:
                if ep != position and b[position] == b[ep]:
                    b = remove_cards(b, ep)
                    q.append((y, x, b, cnt+1, -1))
           
    return answer


board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0

answer = solution(board=board, r=r, c=c)
print(answer)