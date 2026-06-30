from models.group import Group
from extensions import db


class GroupRepository:

    @staticmethod
    def get_all():
        return Group.query.order_by(Group.group_name).all()

    @staticmethod
    def search(keyword):
        return Group.query.filter(
            Group.group_name.contains(keyword)
        ).order_by(Group.group_name).all()

    @staticmethod
    def get(group_id):
        return db.session.get(Group, group_id)

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