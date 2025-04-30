class ChessPiece:
    def __init__(self, name, color):
        """
        Inicializa una pieza de ajedrez.
        name: Nombre de la pieza (e.g., 'Pawn', 'Rook').
        color: Color de la pieza ('white' o 'black').
        """
        self.name = name
        self.color = color

    def is_valid_move(self, start_pos, end_pos, board):
        """
        Verifica si el movimiento es válido para esta pieza.
        Este método será sobrescrito en las subclases específicas.
        """
        return False


class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__("Pawn", color)

    def is_valid_move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Reglas básicas del peón
        if self.color == "white":
            if start_row - 1 == end_row and start_col == end_col and board[end_row][end_col] == " ":
                return True  # Movimiento hacia adelante
            if start_row - 2 == end_row and start_col == end_col and start_row == 6 and board[end_row][end_col] == " ":
                return True  # Movimiento doble desde la posición inicial
        elif self.color == "black":
            if start_row + 1 == end_row and start_col == end_col and board[end_row][end_col] == " ":
                return True  # Movimiento hacia adelante
            if start_row + 2 == end_row and start_col == end_col and start_row == 1 and board[end_row][end_col] == " ":
                return True  # Movimiento doble desde la posición inicial
        return False

class Rook(ChessPiece):
    def __init__(self, color):
        super().__init__("Rook", color)

    def is_valid_move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Movimiento en la misma fila o columna
        if start_row == end_row or start_col == end_col:
            # Verifica que no haya piezas bloqueando el camino
            if self.is_path_clear(start_pos, end_pos, board):
                return True
        return False

    def is_path_clear(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Verifica el camino en línea recta
        if start_row == end_row:  # Movimiento horizontal
            step = 1 if start_col < end_col else -1
            for col in range(start_col + step, end_col, step):
                if board[start_row][col] != " ":
                    return False
        elif start_col == end_col:  # Movimiento vertical
            step = 1 if start_row < end_row else -1
            for row in range(start_row + step, end_row, step):
                if board[row][start_col] != " ":
                    return False
        return True

class Knight(ChessPiece):
    def __init__(self, color):
        super().__init__("Knight", color)

    def is_valid_move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Movimiento en forma de "L"
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            return True
        return False

class Bishop(ChessPiece):
    def __init__(self, color):
        super().__init__("Bishop", color)

    def is_valid_move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Movimiento diagonal (la diferencia de filas debe ser igual a la diferencia de columnas)
        if abs(end_row - start_row) == abs(end_col - start_col):
            # Verifica que no haya piezas bloqueando el camino
            if self.is_path_clear(start_pos, end_pos, board):
                return True
        return False

    def is_path_clear(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        step_row = 1 if end_row > start_row else -1
        step_col = 1 if end_col > start_col else -1
        for i in range(1, abs(end_row - start_row)):
            row = start_row + step_row * i
            col = start_col + step_col * i
            if board[row][col] != " ":
                return False
        return True

class Queen(ChessPiece):
    def __init__(self, color):
        super().__init__("Queen", color)

    def is_valid_move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Movimiento tipo torre (horizontal/vertical)
        if start_row == end_row or start_col == end_col:
            if self.is_path_clear(start_pos, end_pos, board):
                return True
        
        # Movimiento tipo alfil (diagonal)
        elif abs(end_row - start_row) == abs(end_col - start_col):
            if self.is_path_clear(start_pos, end_pos, board):
                return True
        
        return False

    def is_path_clear(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Movimiento horizontal
        if start_row == end_row:
            step = 1 if start_col < end_col else -1
            for col in range(start_col + step, end_col, step):
                if board[start_row][col] != " ":
                    return False

        # Movimiento vertical
        elif start_col == end_col:
            step = 1 if start_row < end_row else -1
            for row in range(start_row + step, end_row, step):
                if board[row][start_col] != " ":
                    return False

        # Movimiento diagonal
        else:
            step_row = 1 if end_row > start_row else -1
            step_col = 1 if end_col > start_col else -1
            for i in range(1, abs(end_row - start_row)):
                row = start_row + step_row * i
                col = start_col + step_col * i
                if board[row][col] != " ":
                    return False

        # Verificar la casilla final (si es una pieza enemiga, permite captura)
        final_piece = board[end_row][end_col]
        if final_piece != " " and (
            (final_piece.islower() and self.color == "white") or
            (final_piece.isupper() and self.color == "black")
        ):
            return True

        # Casilla final vacía
        return board[end_row][end_col] == " "


class King(ChessPiece):
    def __init__(self, color):
        super().__init__("King", color)

    def is_valid_move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Movimiento limitado a una casilla en cualquier dirección
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        if row_diff <= 1 and col_diff <= 1:
            return True
        return False
