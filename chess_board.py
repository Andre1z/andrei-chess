class ChessBoard:
    def __init__(self):
        # Representación inicial del tablero vacío con piezas
        self.board = self.create_initial_board()

    def create_initial_board(self):
        # Configura el tablero con las piezas en sus posiciones iniciales
        board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],  # Fila 1 (torres, caballos, etc.)
            ["p"] * 8,                                 # Fila 2 (peones)
            [" "] * 8,                                 # Filas 3 a 6 vacías
            [" "] * 8,
            [" "] * 8,
            [" "] * 8,
            ["P"] * 8,                                 # Fila 7 (peones blancos)
            ["R", "N", "B", "Q", "K", "B", "N", "R"]  # Fila 8 (torres, caballos, etc.)
        ]
        return board

    def display_board(self):
        # Imprime el tablero en consola
        for row in self.board:
            print(" ".join(row))

# Código de prueba
if __name__ == "__main__":
    chess_board = ChessBoard()
    chess_board.display_board()
