from abc import ABCMeta, abstractmethod

from domain.models.walking_parameter.walking_parameter import WalkingParameter
from psycopg2.extensions import connection


class RealtimeWalkingSampleRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(
        self, conn: connection, realtime_id: str, walking_sample: WalkingParameter
    ) -> WalkingParameter:
        pass

    @abstractmethod
    def find_latest_for_realtime_id(
        self, conn: connection, realtime_id: str
    ) -> WalkingParameter:
        pass

    @abstractmethod
    def find_latest_id_for_realtime_id(self, conn: connection, realtime_id: str) -> str:
        pass


class ModifiedWalkingSampleRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(
        self, conn: connection, modified_id: str, walking_sample: WalkingParameter
    ) -> WalkingParameter:
        pass
