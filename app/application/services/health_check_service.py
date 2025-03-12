from app.config.const import HEALTH_CHECK_BUCKET_NAME
from app.infrastructure.connection import MinIOConnection
from app.infrastructure.external.services import FileService


class HealthCheckService:
    def minio(
        self,
        bucket_name: str,
        upload_file: bytes,
    ) -> bytes:
        s3 = MinIOConnection.connect()

        file_service = FileService(s3)

        file_service.upload(
            key=f"{HEALTH_CHECK_BUCKET_NAME}/{bucket_name}",
            file=upload_file,
        )

        return file_service.download(key=f"{HEALTH_CHECK_BUCKET_NAME}/{bucket_name}")
