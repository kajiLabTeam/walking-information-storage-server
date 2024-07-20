from abc import ABCMeta, abstractmethod
from typing import Any, List

from domain.models.walking_parameter.walking_parameter import WalkingParameter
from psycopg2.extensions import connection


class RealtimeWalkingSampleRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save_realtime(
        self, conn: connection, walking_sample: WalkingParameter
    ) -> WalkingParameter:
        pass


class ModifiedWalkingSampleRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save_modified(
        self, conn: connection, walking_sample: WalkingParameter
    ) -> WalkingParameter:
        pass
