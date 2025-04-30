from chess_pieces import Pawn, Rook, Knight, Bishop, Queen, King

class ChessBoard:
    def __init__(self):
        # Inicializa el tablero, las piezas y el turno actual
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
        self.current_turn = "white"  # Comienza el turno de las blancas

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
        print(f"\nTurno actual: {self.current_turn.capitalize()}")

    def move_piece(self, start_pos, end_pos):
        """
        Mueve una pieza desde `start_pos` (tupla) a `end_pos` (tupla).
        También maneja capturas de piezas enemigas y verifica el turno.

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

        # Verificar que la pieza pertenece al jugador actual
        if (self.current_turn == "white" and piece.islower()) or \
           (self.current_turn == "black" and piece.isupper()):
            print("No puedes mover las piezas del oponente.")
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
                # Cambiar el turno
                self.switch_turn()
                return True
            else:
                print("Movimiento inválido para esta pieza.")
                return False
        else:
            print("Esa pieza no tiene reglas implementadas todavía.")
            return False

    def switch_turn(self):
        # Cambia el turno al otro jugador
        self.current_turn = "black" if self.current_turn == "white" else "white"


# Bloque principal para ejecutar y probar el programa
if __name__ == "__main__":
    print("Iniciando el tablero de ajedrez con gestión de turnos...\n")
    chess_board = ChessBoard()  # Crea una instancia del tablero
    chess_board.display_board()  # Muestra el tablero inicial en consola

    # Turno 1: Blancas mueven un peón
    print("\nIntentando mover un peón blanco...")
    success = chess_board.move_piece((6, 4), (4, 4))  # Mueve un peón blanco
    if success:
        print("\nTablero después del movimiento del peón blanco:")
        chess_board.display_board()
    else:
        print("\nMovimiento no válido.")

    # Turno 2: Negras mueven un peón
    print("\nIntentando mover un peón negro...")
    success = chess_board.move_piece((1, 3), (3, 3))  # Mueve un peón negro desde (1,3) a (3,3)
    if success:
        print("\nTablero después del movimiento del peón negro:")
        chess_board.display_board()
    else:
        print("\nMovimiento no válido para el peón negro.")

    # Turno 3: Negras intentan capturar una pieza blanca
    print("\nPreparando captura con un peón negro...")
    chess_board.board[4][4] = "P"  # Añadimos un peón blanco en (4,4)
    success = chess_board.move_piece((3, 3), (4, 4))  # Peón negro intenta capturar
    if success:
        print("\nTablero después de la captura del peón negro:")
        chess_board.display_board()
    else:
        print("\nMovimiento de captura no válido.")
