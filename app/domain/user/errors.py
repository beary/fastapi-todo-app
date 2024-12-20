from fastapi import status

from app.shared.errors import BaseError


class UnauthorizedError(BaseError):
    def __init__(self, message: str = "Unauthorized") -> None:
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message=message,
        )


class UserNameExistsError(BaseError):
    def __init__(self, message: str = "Username already exists") -> None:
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            message=message,
        )
