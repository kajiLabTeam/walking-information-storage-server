from domain.repository_impl.walking_information_repository_impl import (
    AccelerometerRepositoryImpl,
    AtmosphericPressureRepositoryImpl,
    GyroscopeRepositoryImpl,
    RatioWaveRepositoryImpl,
    WalkingInformationRepositoryImpl,
)
from psycopg2.extensions import connection
from ulid import ULID


class WalkingInformationRepository(WalkingInformationRepositoryImpl):
    def save(self, conn: connection, pedestrian_id: str) -> str:
        with conn.cursor() as cursor:
            walking_information_id = str(ULID())

            cursor.execute(
                "INSERT INTO walking_information (id, pedestrian_id) VALUES (%s, %s)",
                ((walking_information_id), pedestrian_id),
            )

            return walking_information_id


class GyroscopeRepository(GyroscopeRepositoryImpl):
    def save(self, conn: connection, walking_information_id: str) -> str:
        with conn.cursor() as cursor:
            gyroscope_id = str(ULID())

            cursor.execute(
                "INSERT INTO gyroscopes (id, walking_information_id) VALUES (%s, %s)",
                ((gyroscope_id), walking_information_id),
            )

            return gyroscope_id


class AccelerometerRepository(AccelerometerRepositoryImpl):
    def save(self, conn: connection, walking_information_id: str) -> str:
        with conn.cursor() as cursor:
            accelerometer_id = str(ULID())

            cursor.execute(
                "INSERT INTO accelerometers (id, walking_information_id) VALUES (%s, %s)",
                ((accelerometer_id), walking_information_id),
            )

            return accelerometer_id


class RatioWaveRepository(RatioWaveRepositoryImpl):
    def save(
        self,
        conn: connection,
        rssi: float,
        walking_information_id: str,
    ) -> str:
        with conn.cursor() as cursor:
            ratio_wave_id = str(ULID())

            cursor.execute(
                "INSERT INTO ratio_waves (id, rssi, walking_information_id) VALUES (%s, %s, %s)",
                ((ratio_wave_id), rssi, walking_information_id),
            )

            return ratio_wave_id


class AtmosphericPressureRepository(AtmosphericPressureRepositoryImpl):
    def save(
        self, conn: connection, pressure: float, walking_information_id: str
    ) -> str:
        with conn.cursor() as cursor:
            atmospheric_pressure_id = str(ULID())

            cursor.execute(
                "INSERT INTO atmospheric_pressures (id, pressure, walking_information_id) VALUES (%s, %s, %s)",
                ((atmospheric_pressure_id), pressure, walking_information_id),
            )

            return atmospheric_pressure_id
