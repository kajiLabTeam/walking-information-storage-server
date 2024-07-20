from typing import Optional


class WalkingParameter:
    def __init__(self, id: Optional[str], step: int, angle_changed: int):
        self.__id = id
        self.__step = step
        self.__angle_changed = round(angle_changed, 0)

    def get_id(self) -> str:
        if self.__id is None:
            raise ValueError("Not found")

        return self.__id

    def get_step(self) -> int:
        return self.__step

    def get_angle_changed(self) -> int:
        return self.__angle_changed
