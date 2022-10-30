class Board:
    DEFAULT_BOARD = [
       # 1  2  3  4  5  6  7  8
        [0, 0, 0, 0, 0, 0, 0, 0],  # A
        [0, 0, 0, 0, 0, 0, 0, 0],  # B
        [0, 0, 0, 0, 0, 0, 0, 0],  # C
        [0, 0, 0, 0, 0, 0, 0, 0],  # D
        [0, 0, 0, 0, 0, 0, 0, 0],  # E
        [0, 0, 0, 0, 0, 0, 0, 0],  # F
        [0, 0, 0, 0, 0, 0, 0, 0],  # G
        [0, 0, 0, 0, 0, 0, 0, 0],  # H
    ]

    STR_INT_MAPPING = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
    }
    INT_STR_MAPPING = {v: k for k, v in STR_INT_MAPPING.items()}

    _bishop = [
        (i * j, i * k)
        for i in range(1, 8)
        for j, k in [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    ]
    _rook = [
        (i * j, i * k)
        for i in range(1, 8)
        for j, k in [(0, -1), (-1, 0), (0, 1), (1, 0)]
    ]
    MAPPING_FIGURES_RELATIVE_STEPS = {
        'king': [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)],
        'knight': [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)],
        'bishop': _bishop,
        'rook': _rook,
        'queen': _bishop + _rook
    }

    def __init__(self, figure, board=DEFAULT_BOARD):
        self.board = board
        self.figure = figure

    def str_int(self, point):
        x = int(point[1]) - 1  # -1 due to count from 0
        y = self.STR_INT_MAPPING[point[0]]
        return x, y

    def int_str(self, x, y):
        latter = self.INT_STR_MAPPING[y]
        x += 1  # -1 due to count from 0
        return f"{latter}{x}"

    @staticmethod
    def get_direction(delta):
        if delta > 0:
            direction = 1
        elif delta < 0:
            direction = -1
        else:
            direction = 0
        return direction

    def is_path_clean(self, x, y, delta_x, delta_y):
        if self.figure == 'knight':
            if self.board[y + delta_y][x + delta_x] == 1:
                return False
            return True
        else:
            direction_x = self.get_direction(delta_x)
            direction_y = self.get_direction(delta_y)
            cur_x, cur_y = x, y
            while (cur_x, cur_y) != (x + delta_x, y + delta_y):
                if self.board[cur_y][cur_x] == 1:
                    return False
                cur_x += direction_x
                cur_y += direction_y
            if self.board[cur_y][cur_x] == 1:
                return False
            return True

    def get_possible_steps_of_figure(self, point):
        relative_steps = self.MAPPING_FIGURES_RELATIVE_STEPS[self.figure]
        return self.get_possible_steps(point, relative_steps)

    def get_possible_steps(self, point, relative_steps):
        possible_steps = []
        x, y = self.str_int(point)
        for delta_x, delta_y in relative_steps:
            if (
                0 <= x + delta_x <= 7
                and 0 <= y + delta_y <= 7
                and self.is_path_clean(x, y, delta_x, delta_y)
            ):
                possible_steps.append(self.int_str(x + delta_x, y + delta_y))
        return possible_steps
