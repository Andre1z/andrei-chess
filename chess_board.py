class ChessBoard:
    def __init__(self):
        self.board = self.create_initial_board()

    def create_initial_board(self):
        board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p"] * 8,
            [" "] * 8,
            [" "] * 8,
            [" "] * 8,
            [" "] * 8,
            ["P"] * 8,
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]
        return board

    def display_board(self):
        for row in self.board:
            print(" ".join(row))

    def move_piece(self, start_pos, end_pos):
        """
        Mueve una pieza desde `start_pos` (tupla de coordenadas) a `end_pos`.

        Parámetros:
        start_pos: tupla (fila_inicio, columna_inicio)
        end_pos: tupla (fila_fin, columna_fin)
        """
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Verifica que la posición inicial no esté vacía
        if self.board[start_row][start_col] == " ":
            print("No hay ninguna pieza en esa posición.")
            return False

        # Realiza el movimiento
        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = " "
        return True

# Código de prueba
if __name__ == "__main__":
    chess_board = ChessBoard()
    chess_board.display_board()

    print("\nMoviendo un peón...")
    chess_board.move_piece((6, 4), (4, 4))  # Ejemplo: mueve el peón de la columna 'e' (fila 7 a fila 5)
    chess_board.display_board()
