from collections import deque

from board import Board


def bfs(board, start, stop):
    """Breadth-first search."""

    queue = deque([(start, [])])
    visited = {start: []}
    
    while queue:
        cur_step, path_to_cur_step = queue.popleft()
        if cur_step == stop:
            visited[stop] = path_to_cur_step + [cur_step]
            break
        next_steps = board.get_possible_steps_of_figure(cur_step)
        for next_step in next_steps:
            if next_step not in visited:
                path_to_next_step = path_to_cur_step + [cur_step]
                queue.append((next_step, path_to_next_step))
                visited[next_step] = path_to_next_step
    return visited


def main():
    board = Board(
        'knight',
        board=[
            # 1  2  3  4  5  6  7  8
            [0, 1, 0, 0, 0, 1, 0, 1],  # A
            [0, 1, 0, 1, 0, 1, 0, 1],  # B
            [0, 1, 0, 1, 0, 1, 0, 1],  # C
            [0, 1, 0, 1, 0, 1, 0, 1],  # D
            [0, 1, 0, 1, 0, 1, 0, 1],  # E
            [0, 1, 0, 1, 0, 1, 0, 1],  # F
            [0, 1, 0, 1, 0, 1, 0, 1],  # G
            [0, 0, 0, 1, 0, 0, 0, 1],  # H
        ],
    )
    start = 'A1'
    stop = 'A7'
    result = bfs(board, start, stop)
    print(" -> ".join(result.get(stop, [])))


if __name__ == '__main__':
    main()
