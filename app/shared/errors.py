from fastapi import status


class BaseError(Exception):
    status_code: int
    message: str

    def __init__(
        self,
        status_code: int,
        message: str,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code


class NotFoundError(BaseError):
    def __init__(self, message: str = "Not found") -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            message=message,
        )
