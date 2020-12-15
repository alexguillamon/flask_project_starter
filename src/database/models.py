from database import db


class BaseModel(db.Model):
    """
    This abstract class implements common methods that you would see in a SQL alchemy model.
    """
    __abstract__ = True

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Model(BaseModel):
    pass
