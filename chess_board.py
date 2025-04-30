from chess_pieces import Pawn, Rook, Knight, Bishop, Queen, King

class ChessBoard:
    def __init__(self):
        # Inicializa el tablero y las piezas
        self.board = self.create_initial_board()
        self.pieces = {
            "P": Pawn("white"),
            "p": Pawn("black"),
            "R": Rook("white"),
            "r": Rook("black"),
            "N": Knight("white"),
            "n": Knight("black"),
            "B": Bishop("white"),
            "b": Bishop("black"),
            "Q": Queen("white"),
            "q": Queen("black"),
            "K": King("white"),
            "k": King("black"),
        }

    def create_initial_board(self):
        # Configuración inicial del tablero con todas las piezas
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
        # Muestra el tablero en consola
        for row in self.board:
            print(" ".join(row))

    def move_piece(self, start_pos, end_pos):
        """
        Mueve una pieza desde `start_pos` (tupla) a `end_pos` (tupla).
        También maneja capturas de piezas enemigas.

        Parámetros:
        - start_pos: (fila_inicio, columna_inicio)
        - end_pos: (fila_fin, columna_fin)
        """
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        piece = self.board[start_row][start_col]
        if piece == " ":
            print("No hay ninguna pieza en esa posición.")
            return False

        if piece.upper() in self.pieces:
            chess_piece = self.pieces[piece.upper()]
            # Verifica si el movimiento es válido
            if chess_piece.is_valid_move(start_pos, end_pos, self.board):
                target_piece = self.board[end_row][end_col]
                # Manejo de captura
                if target_piece != " " and target_piece.islower() != piece.islower():
                    print(f"¡{piece} ha capturado a {target_piece}!")
                # Realiza el movimiento
                self.board[end_row][end_col] = piece
                self.board[start_row][start_col] = " "
                return True
            else:
                print("Movimiento inválido para esta pieza.")
                return False
        else:
            print("Esa pieza no tiene reglas implementadas todavía.")
            return False


# Bloque principal para ejecutar y probar el programa
if __name__ == "__main__":
    print("Iniciando el tablero de ajedrez...\n")
    chess_board = ChessBoard()  # Crea una instancia del tablero
    chess_board.display_board()  # Muestra el tablero inicial en consola

    print("\nIntentando mover un peón...")
    success = chess_board.move_piece((6, 4), (4, 4))  # Ejemplo: mueve un peón blanco
    if success:
        print("\nTablero después del movimiento del peón:")
        chess_board.display_board()
    else:
        print("\nMovimiento no válido.")

    print("\nPreparando el tablero para una captura...")
    chess_board.board[4][3] = "p"  # Añadimos un peón negro en (4, 3)
    chess_board.display_board()

    print("\nIntentando capturar al peón negro con la reina blanca...")
    success = chess_board.move_piece((7, 3), (4, 3))  # La reina blanca intenta capturar al peón negro
    if success:
        print("\nTablero después de la captura:")
        chess_board.display_board()
    else:
        print("\nLa captura no fue válida.")
