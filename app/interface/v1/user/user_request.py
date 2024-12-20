from pydantic import BaseModel, ConfigDict, Field

username_regex = r"^\w{3,20}$"
password_regex = r"^.{6,64}$"


class UserRegisterRequest(BaseModel):
    username: str = Field(pattern=username_regex)
    password: str = Field(pattern=password_regex)

    model_config = ConfigDict(str_strip_whitespace=True)


class UserLoginRequest(BaseModel):
    username: str = Field(pattern=username_regex)
    password: str = Field(pattern=password_regex)

    model_config = ConfigDict(str_strip_whitespace=True)
