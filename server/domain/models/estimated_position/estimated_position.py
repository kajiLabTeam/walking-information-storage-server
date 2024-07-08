class EstimatedPosition:
    def __init__(self, x: int, y: int, direction: float) -> None:
        self.__x = x
        self.__y = y
        self.__direction = direction

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    def get_direction(self) -> float:
        return self.__direction
