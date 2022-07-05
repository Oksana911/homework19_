from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(User).get(bid)

    def get_all(self):
        # А еще можно сделать так, вместо всех методов get_by_*
        # t = self.session.query(User)
        # if "director_id" in filters:
        #     t = t.filter(user.director_id == filters.get("director_id"))
        # if "genre_id" in filters:
        #     t = t.filter(user.genre_id == filters.get("genre_id"))
        # if "year" in filters:
        #     t = t.filter(user.year == filters.get("year"))
        # return t.all()
        return self.session.query(User).all()

    # def get_by_director_id(self, val):
    #     return self.session.query(User).filter(User.director_id == val).all()
    #
    # def get_by_genre_id(self, val):
    #     return self.session.query(User).filter(User.genre_id == val).all()
    #
    # def get_by_year(self, val):
    #     return self.session.query(User).filter(User.year == val).all()

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_d):
        user = self.get_one(user_d.get("id"))
        user.title = user_d.get("title")
        user.description = user_d.get("description")
        user.trailer = user_d.get("trailer")
        user.year = user_d.get("year")
        user.rating = user_d.get("rating")
        user.genre_id = user_d.get("genre_id")
        user.director_id = user_d.get("director_id")

        self.session.add(user)
        self.session.commit()
