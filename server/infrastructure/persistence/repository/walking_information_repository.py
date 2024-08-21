from domain.repository_impl.dto.infrastructure_dto import (
    AccelerometerRepositoryDto,
    AtmosphericPressureRepositoryDto,
    GyroscopeRepositoryDto,
    RatioWaveRepositoryDto,
    WalkingInformationRepositoryDto,
)
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
    def save(
        self, conn: connection, pedestrian_id: str
    ) -> WalkingInformationRepositoryDto:
        with conn.cursor() as cursor:
            walking_information_id = str(ULID())

            cursor.execute(
                "INSERT INTO walking_informations (id, pedestrian_id) VALUES (%s, %s)",
                ((walking_information_id), pedestrian_id),
            )

            return WalkingInformationRepositoryDto(
                walking_information_id=walking_information_id,
                pedestrian_id=pedestrian_id,
            )


class GyroscopeRepository(GyroscopeRepositoryImpl):
    def save(
        self, conn: connection, walking_information_id: str
    ) -> GyroscopeRepositoryDto:
        with conn.cursor() as cursor:
            gyroscope_id = str(ULID())

            cursor.execute(
                "INSERT INTO gyroscopes (id, walking_information_id) VALUES (%s, %s)",
                ((gyroscope_id), walking_information_id),
            )

            return GyroscopeRepositoryDto(
                gyroscope_id=gyroscope_id,
                walking_information_id=walking_information_id,
            )


class AccelerometerRepository(AccelerometerRepositoryImpl):
    def save(
        self, conn: connection, walking_information_id: str
    ) -> AccelerometerRepositoryDto:
        with conn.cursor() as cursor:
            accelerometer_id = str(ULID())

            cursor.execute(
                "INSERT INTO accelerometers (id, walking_information_id) VALUES (%s, %s)",
                ((accelerometer_id), walking_information_id),
            )

            return AccelerometerRepositoryDto(
                accelerometer_id=accelerometer_id,
                walking_information_id=walking_information_id,
            )


class RatioWaveRepository(RatioWaveRepositoryImpl):
    def save(
        self,
        conn: connection,
        rssi: float,
        walking_information_id: str,
    ) -> RatioWaveRepositoryDto:
        with conn.cursor() as cursor:
            ratio_wave_id = str(ULID())

            cursor.execute(
                "INSERT INTO ratio_waves (id, rssi, walking_information_id) VALUES (%s, %s, %s)",
                ((ratio_wave_id), rssi, walking_information_id),
            )

            return RatioWaveRepositoryDto(
                ratio_wave_id=ratio_wave_id,
                rssi=rssi,
                walking_information_id=walking_information_id,
            )


class AtmosphericPressureRepository(AtmosphericPressureRepositoryImpl):
    def save(
        self, conn: connection, pressure: float, walking_information_id: str
    ) -> AtmosphericPressureRepositoryDto:
        with conn.cursor() as cursor:
            atmospheric_pressure_id = str(ULID())

            cursor.execute(
                "INSERT INTO atmospheric_pressures (id, pressure, walking_information_id) VALUES (%s, %s, %s)",
                ((atmospheric_pressure_id), pressure, walking_information_id),
            )

            return AtmosphericPressureRepositoryDto(
                atmospheric_pressure_id=atmospheric_pressure_id,
                pressure=pressure,
                walking_information_id=walking_information_id,
            )
