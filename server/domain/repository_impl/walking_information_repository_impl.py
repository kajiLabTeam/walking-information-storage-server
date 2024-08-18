from abc import ABCMeta, abstractmethod

from psycopg2.extensions import connection


class WalkingInformationRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection, pedestrian_id: str) -> str:
        pass


class GyroscopeRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection, walking_information_id: str) -> str:
        pass


class AccelerometerRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection, walking_information_id: str) -> str:
        pass


class RatioWaveRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(
        self,
        conn: connection,
        rssi: float,
        walking_information_id: str,
    ) -> str:
        pass


class AtmosphericPressureRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(
        self, conn: connection, pressure: float, walking_information_id: str
    ) -> str:
        pass
