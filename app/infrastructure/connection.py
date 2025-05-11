import boto3
from botocore.client import BaseClient
from sqlalchemy.engine import Engine
from sqlmodel import Session, SQLModel, create_engine

from app.config import MinioEnv, PostgresEnv


class DBConnection:
    _engine: Engine | None = None

    @staticmethod
    def get_session() -> Session:
        return Session(bind=DBConnection.__get_engine())

    @staticmethod
    def __get_engine() -> Engine:
        if DBConnection._engine is None:
            env = PostgresEnv()
            DBConnection._engine = create_engine(
                f"postgresql://{env.get_user_of_private_value()}:{env.get_password_of_private_value()}@"
                f"{env.get_host_of_private_value()}:{env.get_port_of_private_value()}/{env.get_database_of_private_value()}"
            )
        return DBConnection._engine

    @staticmethod
    def init_db() -> None:
        SQLModel.metadata.create_all(DBConnection.__get_engine())


class MinIOConnection:
    _client: BaseClient | None = None

    @classmethod
    def connect(cls) -> BaseClient:
        if cls._client is None:
            env = MinioEnv()
            cls._client = boto3.client(
                service_name=env.get_service_name_of_private_value(),
                endpoint_url=env.get_endpoint_of_private_value(),
                aws_access_key_id=env.get_access_key_of_private_value(),
                aws_secret_access_key=env.get_secret_key_of_private_value(),
                region_name=env.get_region_of_private_value(),
            )
        return cls._client
