from config.const.bucket import HEALTH_CHECK_BUCKET_NAME
from infrastructure.connection import MinIOConnection
from infrastructure.external.services.file_service import FileService


class HealthCheckService:
    def minio(self, bucket_name: str, upload_file: bytes) -> bytes:
        s3 = MinIOConnection.connect()

        file_service = FileService(s3)

        file_service.upload(
            bucket_type_name=HEALTH_CHECK_BUCKET_NAME,
            bucket_id=bucket_name,
            file=upload_file,
        )
        download_file = file_service.download(
            bucket_type_name=HEALTH_CHECK_BUCKET_NAME, bucket_id=bucket_name
        )

        return download_file
