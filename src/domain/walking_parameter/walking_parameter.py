class WalkingParameter:
    def __init__(self, stride: int, angle_variation: int):
        self.__stride = stride
        self.__angle_variation = angle_variation

    def get_stride(self):
        return self.__stride

    def get_angle_variation(self):
        return self.__angle_variation
