class Rectangle:
    def __init__(self, min_x: int, min_y, width: int, height: int):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = min_x + width
        self.max_y = min_y + height

    def center(self) -> tuple[int, int]:
        return (self.min_x + self.max_x) // 2, (self.min_y + self.max_y) // 2

    def top_left(self) -> tuple[int, int]:
        return (self.min_x, self.min_y)

    def bottom_right(self) -> tuple[int, int]:
        return (self.max_x, self.max_y)
