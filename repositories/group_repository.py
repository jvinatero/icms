from models.group import Group
from extensions import db


class GroupRepository:

    @staticmethod
    def get_all():
        return Group.query.order_by(Group.id).all()

    @staticmethod
    def get_by_id(group_id):
        return Group.query.get(group_id)

    @staticmethod
    def get_by_name(name):
        return Group.query.filter_by(group_name=name).first()

    @staticmethod
    def add(group):
        db.session.add(group)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(group):
        db.session.delete(group)
        db.session.commit()