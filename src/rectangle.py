class Rectangle:
    def __init__(s, min_x: int, min_y, width: int, height: int):
        s.min_x = min_x
        s.min_y = min_y
        s.max_x = min_x + width
        s.max_y = min_y + height

    def center(s) -> tuple[int, int]:
        return (s.min_x + s.max_x) // 2, (s.min_y + s.max_y) // 2

    def top_left(s) -> tuple[int, int]:
        return (s.min_x, s.min_y)

    def bottom_right(s) -> tuple[int, int]:
        return (s.max_x, s.max_y)
