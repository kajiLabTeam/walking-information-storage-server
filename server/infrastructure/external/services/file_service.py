from io import BytesIO
from typing import Any

from config.const.bucket import BUCKET_NAME


class FileService:
    def __init__(self, s3: Any):
        self.__s3 = s3

    def download(self, file_type_name: str, file_id: str) -> bytes:
        key = f"{file_type_name}/{file_id}"
        obj = self.__s3.get_object(Bucket=BUCKET_NAME, Key=key)

        return obj["Body"].read()

    def upload(
        self,
        file_type_name: str,
        file_id: str,
        file: bytes,
    ) -> None:
        buffer = BytesIO(file)
        key = f"{file_type_name}/{file_id}"

        self.__s3.upload_fileobj(buffer, BUCKET_NAME, key)
        buffer.close()
