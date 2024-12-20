import base64
import random
from datetime import date
from uuid import uuid4


def guid() -> str:
    return base64.urlsafe_b64encode(uuid4().bytes[:9]).decode()


def gcode() -> str:
    return str(random.randint(100000, 999999))


def calculate_age(birthday: date) -> int:
    today = date.today()
    return (
        today.year
        - birthday.year
        - ((today.month, today.day) < (birthday.month, birthday.day))
    )
