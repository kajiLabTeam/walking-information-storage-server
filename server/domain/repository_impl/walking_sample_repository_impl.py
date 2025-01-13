from abc import ABCMeta, abstractmethod

from psycopg2.extensions import connection

from server.domain.dataclasses import Pose
from server.domain.models.particle_collection.particle_collection import ParticleCollection
from server.domain.repository_impl.dto.infrastructure_dto import WalkingSampleRepositoryDto


class WalkingSampleRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(
        self,
        conn: connection,
        is_converged: bool,
        trajectory_id: str,
        walking_information_id: str,
    ) -> WalkingSampleRepositoryDto:
        pass

    @abstractmethod
    def find_latest_for_trajectory_id(
        self,
        conn: connection,
        trajectory_id: str,
    ) -> WalkingSampleRepositoryDto:
        pass


class ParticleRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save_all(
        self,
        conn: connection,
        walking_sample_id: str,
        particle_collection: ParticleCollection,
    ) -> None:
        pass

    @abstractmethod
    def find_for_walking_sample_id(
        self,
        conn: connection,
        walking_sample_id: str,
    ) -> ParticleCollection:
        pass


class PoseRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(
        self,
        conn: connection,
        estimated_pose: Pose,
        walking_sample_id: str,
    ) -> str:
        pass
