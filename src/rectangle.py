from secrets import randbelow


class Rectangle:
    def __init__(self, min_x: int, min_y, width: int, height: int):
        assert min_x >= 0
        assert min_y >= 0
        assert width >= 0
        assert height >= 0

        self.min_x = min_x
        self.min_y = min_y
        self.max_x = min_x + width
        self.max_y = min_y + height

        self.width = width
        self.height = height

    def center(self) -> tuple[int, int]:
        """
        Center coordinates within the rectangle, rounded down.
        (X , Y)
        """
        return (self.min_x + self.max_x) // 2, (self.min_y + self.max_y) // 2

    def top_left(self) -> tuple[int, int]:
        """
        Top left corner coordinates of rectangle.
        (X , Y)
        """
        return self.min_x, self.min_y

    def bottom_right(self) -> tuple[int, int]:
        """
        Bottom right corner coordinates of rectangle.
        (X , Y)
        """
        return self.max_x, self.max_y

    def random_within(self) -> tuple[int, int]:
        """
        Random coordinates within the rectangle.
        (X , Y)
        """
        x_offset = randbelow(self.width)
        y_offset = randbelow(self.height)
        return self.min_x + x_offset, self.min_y + randbelow(y_offset)
