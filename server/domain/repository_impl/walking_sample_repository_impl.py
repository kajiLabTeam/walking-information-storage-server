from abc import ABCMeta, abstractmethod
from typing import Any, List

from psycopg2.extensions import connection

from domain.models.walking_parameter.walking_parameter import WalkingParameter


class WalkingSampleRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def find_for_trajectory_id(
        self,
        conn: connection,
        trajectory_id: str,
    ) -> List[WalkingParameter]:
        pass

    @abstractmethod
    def save(
        self, s3: Any, conn: connection, walking_sample: WalkingParameter
    ) -> WalkingParameter:
        pass
