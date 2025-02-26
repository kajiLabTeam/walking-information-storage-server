from abc import ABCMeta, abstractmethod

from domain.repository_impl.dto.infrastructure_dto import (
    WalkingInformationRepositoryDto,
)
from psycopg2.extensions import connection


class WalkingInformationRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(
        self,
        conn: connection,
        pedestrian_id: str,
    ) -> WalkingInformationRepositoryDto:
        pass

    @abstractmethod
    def find_for_id(
        self,
        conn: connection,
        walking_information_id: str,
    ) -> WalkingInformationRepositoryDto | None:
        pass

    @abstractmethod
    def find_for_pedestrian_id(
        self,
        conn: connection,
        pedestrian_id: str,
    ) -> WalkingInformationRepositoryDto | None:
        pass
