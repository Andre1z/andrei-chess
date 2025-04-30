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
