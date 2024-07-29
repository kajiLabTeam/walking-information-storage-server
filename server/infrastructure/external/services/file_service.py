from io import BytesIO
from typing import Any

from config.const.bucket import BUCKET_NAME


class FileService:
    def __init__(self, s3: Any):
        self.__s3 = s3

    def download(self, bucket_type_name: str, bucket_id: str) -> bytes:
        key = f"{bucket_type_name}/{bucket_id}"
        obj = self.__s3.get_object(Bucket=BUCKET_NAME, Key=key)

        return obj["Body"].read()

    def upload(
        self,
        bucket_type_name: str,
        bucket_id: str,
        file: bytes,
    ) -> None:
        buffer = BytesIO(file)
        key = f"{bucket_type_name}/{bucket_id}"

        self.__s3.upload_fileobj(buffer, BUCKET_NAME, key)
        buffer.close()
