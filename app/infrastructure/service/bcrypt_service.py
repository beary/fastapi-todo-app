import bcrypt


class BcryptService:
    def hash_password(self, password: str) -> str:
        pwd_bytes = password.encode()
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
        return hashed_password.decode()

    def verify_password(self, password: str, hashed_password: str):
        password_byte_enc = password.encode()
        hashed_password_byte_enc = hashed_password.encode()
        return bcrypt.checkpw(
            password=password_byte_enc,
            hashed_password=hashed_password_byte_enc,
        )
