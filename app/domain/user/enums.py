from enum import IntEnum


class Gender(IntEnum):
    FEMALE = 0
    MALE = 1


class UserStatus(IntEnum):
    ACTIVE = 0
    DELETED = 1
    BLOCKED = 2
