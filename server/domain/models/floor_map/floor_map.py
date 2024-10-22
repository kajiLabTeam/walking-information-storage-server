import math
from io import (
    BytesIO,
)
from typing import (
    Tuple,
)

from config.const import (
    INSIDE_PARTICLE_COLOR,
    PEDESTRIAN_SIZE,
)
from domain.dataclasses.coordinate import (
    Coordinate,
)
from PIL import (
    Image,
    ImageDraw,
)
from PIL.Image import (
    Image as ImageType,
)


class FloorMap:
    def __init__(
        self,
        floor_map_image_bytes: bytes,
    ) -> None:
        image_stream = BytesIO(floor_map_image_bytes)
        floor_map_image = Image.open(image_stream)

        self.__floor_map = floor_map_image
        self.__draw = ImageDraw.Draw(self.__floor_map)
        (
            self.__map_width,
            self.__map_height,
        ) = self.__floor_map.size

    def get_floor_map(
        self,
    ) -> ImageType:
        return self.__floor_map

    def get_map_width(
        self,
    ) -> int:
        return self.__map_width

    def get_map_height(
        self,
    ) -> int:
        return self.__map_height

    def depict(
        self,
        position: Tuple[
            int,
            int,
        ],
        color: Color,
    ) -> None:
        """## 指定した座標位置を描画する"""
        try:
            (
                x,
                y,
            ) = position
            self.__floor_map.putpixel(
                (
                    x,
                    y,
                ),
                color,
            )
        except Exception:
            pass

    def depict_circle(
        self,
        position: Tuple[
            int,
            int,
        ],
        color: Color,
        outline_color: Color,
    ) -> None:
        """## 指定した座標位置を中心とする円を描画する"""
        try:
            (
                x,
                y,
            ) = position
            self.__draw.ellipse(
                (
                    x - PEDESTRIAN_SIZE,
                    y - PEDESTRIAN_SIZE,
                    x + PEDESTRIAN_SIZE,
                    y + PEDESTRIAN_SIZE,
                ),
                fill=color,
                outline=outline_color,
            )
        except Exception:
            pass

    def depict_rectangle(
        self,
        position: Tuple[
            int,
            int,
        ],
        color: Color,
    ) -> None:
        """## 指定した座標位置を中心とする四角形を描画する"""
        try:
            (
                x,
                y,
            ) = position
            self.__draw.rectangle(
                (
                    x - PEDESTRIAN_SIZE,
                    y - PEDESTRIAN_SIZE,
                    x + PEDESTRIAN_SIZE,
                    y + PEDESTRIAN_SIZE,
                ),
                fill=color,
            )
        except Exception:
            pass

    def depict_cross(
        self,
        coordinate: Coordinate,
        color: Color,
    ) -> None:
        """## 指定した座標位置を十字形に描画する"""
        (
            x,
            y,
        ) = (
            coordinate.x,
            coordinate.y,
        )

        self.__floor_map.putpixel(
            (
                x,
                y,
            ),
            color,
        )
        self.__floor_map.putpixel(
            (
                x + 1,
                y,
            ),
            color,
        )
        self.__floor_map.putpixel(
            (
                x - 1,
                y,
            ),
            color,
        )
        self.__floor_map.putpixel(
            (
                x,
                y + 1,
            ),
            color,
        )
        self.__floor_map.putpixel(
            (
                x,
                y - 1,
            ),
            color,
        )

    def depict_correct_trajectory(
        self,
        coordinate: Coordinate,
    ) -> None:
        """## 正解軌跡を描画する"""
        (
            x,
            y,
        ) = (
            coordinate.x,
            coordinate.y,
        )

        for i in range(
            -PEDESTRIAN_SIZE,
            PEDESTRIAN_SIZE,
        ):
            for j in range(
                -PEDESTRIAN_SIZE,
                PEDESTRIAN_SIZE,
            ):
                self.depict(
                    (
                        x + i,
                        y + j,
                    ),
                    color=INSIDE_PARTICLE_COLOR,
                )

    def is_inside_floor(
        self,
        coordinate: Coordinate,
    ) -> bool:
        """## 指定した座標が歩行可能領域内に存在するかどうかを判定する"""
        (
            x,
            y,
        ) = (
            coordinate.x,
            coordinate.y,
        )

        if 0 <= x < self.__map_width and 0 <= y < self.__map_height:
            if (
                self.__floor_map.getpixel(
                    (
                        x,
                        y,
                    )
                )
                == INSIDE_PARTICLE_COLOR
            ):
                return True

        return False

    def get_nearest_inside_coordinate(
        self,
        outside_position: Coordinate,
        search_range: int,
    ) -> Coordinate:
        """## 指定した座標から最も近い歩行可能領域内の座標を取得する"""
        # すでに歩行可能領域内に存在する場合は引数をそのまま返す
        (
            x,
            y,
        ) = (
            outside_position.x,
            outside_position.y,
        )
        if self.is_inside_floor(outside_position):
            return outside_position

        for radius in range(
            1,
            search_range,
        ):
            for angle in range(
                0,
                360,
                10,
            ):
                estimated_x = int(x + radius * math.cos(math.radians(angle)))
                estimated_y = int(y + radius * math.sin(math.radians(angle)))

                if self.is_inside_floor(
                    Coordinate(
                        x=estimated_x,
                        y=estimated_y,
                    )
                ):
                    return Coordinate(
                        x=estimated_x,
                        y=estimated_y,
                    )

        return outside_position
