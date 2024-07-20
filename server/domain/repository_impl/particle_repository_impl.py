from abc import ABCMeta, abstractmethod

from domain.models.particle_collection.particle_collection import \
    ParticleCollection
from psycopg2.extensions import connection


class ParticleRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save_all(
        self,
        conn: connection,
        realtime_walking_sample_id: str,
        particle_collection: ParticleCollection,
    ) -> None:
        pass

    @abstractmethod
    def find_for_realtime_walking_sample_id(
        self, conn: connection, realtime_walking_sample_id: str
    ) -> ParticleCollection:
        pass
