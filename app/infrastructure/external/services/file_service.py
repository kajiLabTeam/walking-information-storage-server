from io import BytesIO

from botocore.client import BaseClient

from app.config.constants import BUCKET_NAME
from app.infrastructure.errors.infrastructure_error import (
    InfrastructureError,
    InfrastructureErrorType,
)


class FileService:
    def __init__(
        self,
        s3: BaseClient,
    ) -> None:
        self.__s3 = s3

    def download(
        self,
        key: str,
    ) -> bytes:
        try:
            obj = self.__s3.get_object(
                Bucket=BUCKET_NAME,
                Key=key,
            )
        except Exception as e:
            raise InfrastructureError(
                InfrastructureErrorType.FILE_DOWNLOAD_ERROR,
                500,
                "Failed to download file",
            ) from e

        return obj["Body"].read()

    def upload(
        self,
        key: str,
        file: bytes,
    ) -> None:
        buffer = BytesIO(file)

        try:
            self.__s3.upload_fileobj(
                buffer,
                BUCKET_NAME,
                key,
            )
            buffer.close()
        except Exception as e:
            raise InfrastructureError(
                InfrastructureErrorType.FILE_UPLOAD_ERROR,
                500,
                "Failed to upload file",
            ) from e

    def upload_all(
        self,
        files: list[tuple[str, bytes]],
    ) -> None:
        try:
            for key, file_data in files:
                self.upload(key, file_data)
        except Exception as e:
            raise InfrastructureError(
                InfrastructureErrorType.FILE_UPLOAD_ERROR,
                500,
                "Failed to upload file",
            ) from e
