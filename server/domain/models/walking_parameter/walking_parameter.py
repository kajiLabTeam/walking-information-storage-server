class WalkingParameter:
    def __init__(self, stride: int, angle_variation: int):
        self.__stride = stride
        self.__angle_variation = round(angle_variation, 0)

    def get_stride(self) -> int:
        return self.__stride

    def get_angle_variation(self) -> int:
        return self.__angle_variation
