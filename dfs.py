from board import Board


def dfs(board, start, stop, reduce_amount_cases=True, visited=None, all_paths=None):
    """Depth-first search."""

    if visited is None:
        all_paths = []
        visited = [start]

    # NOTE: It necessary for reduce paths amount and calculation time
    # Every new a found path will be less than previous
    # (it may be equal if path is found in current recursion step)
    if reduce_amount_cases and all_paths and len(visited) >= min(map(len, all_paths)):
        return
    next_steps = board.get_possible_steps_of_figure(start)
    for next_step in next_steps:
        if next_step == stop:
            all_paths.append(visited + [next_step])
            print(f"New path found. Paths amount:{len(all_paths)}")
        else:
            x, y = board.str_int(next_step)
            if next_step not in visited:
                dfs(board, next_step, stop, reduce_amount_cases, visited + [next_step], all_paths)
    return all_paths


def main():
    board = Board(
        'queen',
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
    result = dfs(board, 'A1', 'A7')
    for r in result:
        print(" -> ".join(r))


if __name__ == '__main__':
    main()
