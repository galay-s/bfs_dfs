"Breadth-first search" and "Depth-first search" usage in the life.
================
This small repo illustrates how we can use BFS and DFS for finding of path for 
getting chess figure from cell X to cell Y of board (taking into account obstacles). 


How to use:
---------

You need to create board with `0` and `1`. Where `0` is empty cell and `1` is 
cell which is occupied and there is no possibility to put there your chess 
figure.

### Accessible figures:
```
king
knight
bishop
rook
queen
```
---

### Breadth-first search

```
from board import Board
from bfs import bfs

board = Board(
    'king',
    board=[
       # 1  2  3  4  5  6  7  8
        [0, 0, 0, 0, 0, 0, 0, 0],  # A
        [1, 1, 1, 1, 1, 0, 1, 1],  # B
        [1, 1, 1, 1, 1, 0, 1, 1],  # C
        [1, 1, 1, 1, 1, 0, 0, 0],  # D
        [1, 1, 1, 1, 1, 1, 1, 1],  # E
        [1, 1, 1, 1, 1, 1, 1, 1],  # F
        [1, 1, 1, 1, 1, 1, 1, 1],  # G
        [1, 1, 1, 1, 1, 1, 1, 1],  # H
    ]
)
start = 'A1'
stop = 'D8'
result = bfs(board, start, stop)
print(" -> ".join(result.get(stop, [])))
```
#### Output:
```
A1 -> A2 -> A3 -> A4 -> A5 -> B6 -> C6 -> D7 -> D8
```
This method will try to find  first possible path for chess figure.

---

### Depth-first search
```
from board import Board
from dfs import dfs

board = Board(
    'rook',
    board=[
       # 1  2  3  4  5  6  7  8
        [0, 0, 0, 0, 0, 0, 0, 0],  # A
        [1, 1, 1, 1, 1, 0, 1, 1],  # B
        [1, 1, 1, 1, 1, 0, 1, 1],  # C
        [1, 1, 1, 1, 1, 0, 0, 0],  # D
        [1, 1, 1, 1, 1, 1, 1, 1],  # E
        [1, 1, 1, 1, 1, 1, 1, 1],  # F
        [1, 1, 1, 1, 1, 1, 1, 1],  # G
        [1, 1, 1, 1, 1, 1, 1, 1],  # H
    ]
)
start = 'A1'
stop = 'D8'
result = dfs(board, start, stop)
for r in result:
    print(" -> ".join(r))
```
#### Output:
```
New path found. Paths amount:1
...
...
New path found. Paths amount:29
A1 -> A2 -> A3 -> A4 -> A5 -> A6 -> B6 -> C6 -> D6 -> D7 -> D8
...
...
A1 -> A6 -> C6 -> D6 -> D8
A1 -> A6 -> D6 -> D7 -> D8
A1 -> A6 -> D6 -> D8

```
DFS will look for all possible cases if `reduce_amount_cases` argument is `Falae`.
But I do not recommend to use this argument. Because in this case calculation will 
take much time. By default `reduce_amount_cases=True` and in this case method 
will try to find less paths than previous.

Launch files with preinstalled values:
----
There are two files bfs.py and dfs.py for "Breadth-first search" and "Depth-first search" accordingly.
You can launch these files:
```
python bfs.py 
```
```
python dfs.py 
```
