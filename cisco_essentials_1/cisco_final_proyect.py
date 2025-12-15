import random
from typing import List, Tuple


def display_board(board: List[List[int | str]]) -> None:
    """
    Muestra el estado actual del tablero en consola.

    Args:
        board (List[List[str]]): Tablero 3x3 con valores 1..9 o 'X'/'O'

    Ejemplo:
        >>> b = [[1,2,3],[4,5,6],[7,8,9]]
        >>> display_board(b)  # doctest: +SKIP
    """
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        for cell in row:
            print(f"|   {cell}   ", end="")
        print("|")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board: List[List[int | str]]) -> None:
    """
    Pide al usuario una posición (1..9), valida y marca con 'O'.

    Args:
        board (List[List[str]]): Estado actual del tablero. Se actualiza in-place.

    Ejemplo: (manual - skip doctest)
        >>> b = [[1,2,3],[4,5,6],[7,8,9]]
        >>> enter_move(b)  # doctest: +SKIP
    """
    free = make_list_of_free_fields(board)
    if not free:
        return
    valid = False
    while not valid:
        try:
            value = int(input("Selecciona posición (1..9): "))
        except ValueError:
            print("Entrada inválida. Debes escribir un número entre 1 y 9.")
            continue
        # map value to (row, col)
        if value < 1 or value > 9:
            print("Por favor selecciona un valor entre 1 y 9.")
            continue
        row = (value - 1) // 3
        col = (value - 1) % 3
        if (row, col) not in free:
            print("La posición ya está ocupada. Elige otra.")
            continue
        board[row][col] = 'O'
        valid = True


def make_list_of_free_fields(board: List[List[int | str]]) -> List[Tuple[int, int]]:
    """
    Examina el tablero y devuelve una lista con coordenadas (fila, columna) de celdas libres.

    Args:
        board (List[List[str]]): Estado actual del tablero.

    Returns:
        List[Tuple[int,int]]: Lista de tuplas con coordenadas libres.

    Examples:
        >>> b = [[1, 'X', 3], [4, 'O', 6], [7,8,9]]
        >>> make_list_of_free_fields(b)
        [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
    """
    free = []
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell not in ('X', 'O'):
                free.append((r, c))
    return free


def victory_for(board: List[List[int | str]], sign: str) -> bool:
    """
    Comprueba si el símbolo `sign` ('X' o 'O') tiene 3 en línea.

    Args:
        board (List[List[str]]): Estado actual del tablero.
        sign (str): 'X' o 'O'.

    Returns:
        bool: True si `sign` ha ganado, False si no.

    Examples:
        >>> b = [['X','X','X'], [4,5,6], [7,8,9]]
        >>> victory_for(b, 'X')
        True
        >>> b = [['O',2,3], ['X','O',6], [7,8,'O']]
        >>> victory_for(b, 'O')
        True
    """
    # Check rows
    for row in board:
        if all(cell == sign for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == sign for i in range(3)):
        return True
    if all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False
        


def draw_move(board: List[List[int | str]]) -> None:
    """
    Ejecuta el movimiento del ordenador: elige una celda libre y marca 'X'.

    Args:
        board (List[List[str]]): Estado actual del tablero que se actualizará.

    Examples: (non deterministic - skip doctest)
        >>> b = [[1,2,3],[4,5,6],[7,8,9]]
        >>> draw_move(b)  # doctest: +SKIP
    """
    free = make_list_of_free_fields(board)
    if not free:
        return
    r, c = random.choice(free)
    board[r][c] = 'X'


def _default_board() -> List[List[int | str]]:
    """Devuelve el tablero inicial estándar."""
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def main() -> None:
    """
    Juego principal: ejecuta el bucle alternando jugador y ordenador hasta final.

    No hay doctest para la interacción, ejecute manualmente.
    """
    board = _default_board()
    print("TIC-TAC-TOE: Tú juegas con 'O', la máquina con 'X'.")
    display_board(board)
    while True:
        # Player
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("¡Felicidades! Has ganado.")
            break
        if not make_list_of_free_fields(board):
            print("Empate.")
            break
        # Machine
        print("Turno de la máquina...")
        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("La máquina ha ganado.")
            break
        if not make_list_of_free_fields(board):
            print("Empate.")
            break


if __name__ == "__main__":
    main()
