from extensions import db
from models.area import Area


class AreaRepository:

    @staticmethod
    def get_all():

        return (
            Area.query
            .order_by(
                Area.display_order,
                Area.area_name
            )
            .all()
        )

    @staticmethod
    def search(keyword):

        keyword = f"%{keyword}%"

        return (
            Area.query.filter(
                (Area.area_code.like(keyword)) |
                (Area.area_name.like(keyword)) |
                (Area.category.like(keyword))
            )
            .order_by(
                Area.display_order,
                Area.area_name
            )
            .all()
        )

    @staticmethod
    def get(area_id):

        return db.session.get(
            Area,
            area_id
        )

    @staticmethod
    def get_by_code(area_code):

        return (
            Area.query
            .filter_by(area_code=area_code)
            .first()
        )

    @staticmethod
    def add(area):

        db.session.add(area)
        db.session.commit()

    @staticmethod
    def update():

        db.session.commit()

    @staticmethod
    def delete(area):

        db.session.delete(area)
        db.session.commit()