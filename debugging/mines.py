def play(self):
    while True:
        self.print_board()
        try:
            x = int(input("Enter x coordinate: "))
            y = int(input("Enter y coordinate: "))

            if not (0 <= x < self.width and 0 <= y < self.height):
                print("Coordinates out of bounds!")
                continue

            if not self.reveal(x, y):
                self.print_board(reveal=True)
                print("Game Over! You hit a mine.")
                break

        except ValueError:
            print("Invalid input. Please enter numbers only.")
