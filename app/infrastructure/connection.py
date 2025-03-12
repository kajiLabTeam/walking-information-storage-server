import boto3
from botocore.client import BaseClient
from sqlalchemy.engine import Engine
from sqlmodel import Session, SQLModel, create_engine

from app.config import MinioEnv, PostgresEnv


class DBConnection:
    @staticmethod
    def get_session() -> Session:
        engine = DBConnection.__get_engine()
        return Session(bind=engine)

    @staticmethod
    def __get_engine() -> Engine:
        env = PostgresEnv()
        return create_engine(
            f"postgresql://{env.get_user_of_private_value()}:{env.get_password_of_private_value()}@"
            f"{env.get_host_of_private_value()}:{env.get_port_of_private_value()}/{env.get_database_of_private_value()}"
        )

    @staticmethod
    def init_db() -> None:
        SQLModel.metadata.create_all(DBConnection.__get_engine())


class MinIOConnection:
    @staticmethod
    def connect() -> BaseClient:
        env = MinioEnv()
        return boto3.client(
            service_name=env.get_service_name_of_private_value(),
            endpoint_url=env.get_endpoint_of_private_value(),
            aws_access_key_id=env.get_access_key_of_private_value(),
            aws_secret_access_key=env.get_secret_key_of_private_value(),
            region_name=env.get_region_of_private_value(),
        )
