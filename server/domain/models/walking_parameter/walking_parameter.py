class WalkingParameter:
    def __init__(self, stride: int, angle_variation: int, rssi: int = 0):
        self.__stride = stride
        self.__angle_variation = angle_variation
        self.__rssi = rssi

    def get_stride(self) -> int:
        return self.__stride

    def get_angle_variation(self) -> int:
        return self.__angle_variation

    def get_rssi(self) -> int:
        return self.__rssi
