import hashlib

from dao.user import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        # if filters.get("director_id") is not None:
        #     movies = self.dao.get_by_director_id(filters.get("director_id"))
        # elif filters.get("genre_id") is not None:
        #     movies = self.dao.get_by_genre_id(filters.get("genre_id"))
        # elif filters.get("year") is not None:
        #     movies = self.dao.get_by_year(filters.get("year"))
        # else:
        users = self.dao.get_all()
        return users

    def create(self, user_d):
        return self.dao.create(user_d)

    def update(self, user_d):
        self.dao.update(user_d)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)

    def get_hash(password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")
