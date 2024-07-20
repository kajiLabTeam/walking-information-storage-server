from psycopg2.extensions import connection

from domain.models.estimated_position.estimated_position import \
    EstimatedPosition
from domain.repository_impl.finger_print_repository_impl import (
    AccessPointRepositoryImpl, FingerPrintModelRepositoryImpl,
    FingerPrintRepositoryImpl)


class FingerPrintRepository(FingerPrintRepositoryImpl):
    def save(self, conn: connection, estimated_position: EstimatedPosition) -> None:
        pass


class AccessPointRepository(AccessPointRepositoryImpl):
    def save(self, conn: connection, estimated_position: EstimatedPosition) -> None:
        pass


class FingerPrintModelRepository(FingerPrintModelRepositoryImpl):
    def save(self, conn: connection, estimated_position: EstimatedPosition) -> None:
        pass
