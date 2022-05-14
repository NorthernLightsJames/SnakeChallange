from itertools import product


def next_cell(move: str, my_snake: list) -> list:

    global snake
    current_head_x, current_head_y = my_snake[0][0], my_snake[0][1]

    if move == 'L':
        return [(current_head_x - 1) % board[0], current_head_y]
    if move == 'U':
        return [current_head_x, (current_head_y - 1) % board[1]]
    if move == 'R':
        return [(current_head_x + 1) % board[0], current_head_y]
    if move == 'D':
        return [current_head_x, (current_head_y + 1) % board[1]]


def is_in_snake(cell: list, snake_clone: list) -> bool:
    return cell in snake_clone[:-1]


# def is_out_of_map(cell: list) -> bool:
#     return any([cell[0] < 0, cell[0] > board[0] - 1, cell[1] < 0, cell[1] > board[1] - 1])


def update_snake(_snake: list, direction: str) -> tuple:
    next_head_position = next_cell(direction, _snake)

    if is_in_snake(next_head_position, _snake):
        return False, _snake
    _snake.pop()
    _snake.insert(0, next_head_position)
    return True, _snake


def number_of_available_different_paths(board: list, snake: list, depth: int) -> int:

    global solutions

    if depth > 0:
        for move_direction in 'LURD':
            valid_move, new_snake = update_snake(snake.copy(), move_direction)
            if not valid_move:
                solutions = solutions - len(list(product('LURD', repeat=depth))) // 4
            else:
                number_of_available_different_paths(board, new_snake.copy(), depth - 1)
    return solutions


if __name__ == '__main__':

    # Test1
    board = [4, 3]
    snake = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
    depth = 3
    # Test2
    # board = [2, 3]
    # snake = [[0, 2], [0, 1], [0, 0], [1, 0], [1, 1], [1, 2]]
    # depth = 10
    # Test3
    # board = [10, 10]
    # snake = [[5, 5], [5, 4], [4, 4], [4, 5]]
    # depth = 4
    all_possible_paths = list(product('LURD', repeat=depth))
    solutions = len(all_possible_paths)
    answer = number_of_available_different_paths(board, snake, depth)
    print(f"Result : {answer}")
