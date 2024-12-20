from dataclasses import dataclass


@dataclass(slots=True)
class RegisterResponse:
    access_token: str


@dataclass(slots=True)
class LoginResponse:
    access_token: str
