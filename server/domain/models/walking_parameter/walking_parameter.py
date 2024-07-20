class WalkingParameter:
    def __init__(self, step: int, angle_variation: int):
        self.__step = step
        self.__angle_variation = round(angle_variation, 0)

    def get_step(self) -> int:
        return self.__step

    def get_angle_variation(self) -> int:
        return self.__angle_variation
