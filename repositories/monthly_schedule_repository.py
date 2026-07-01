from extensions import db

from models.monthly_schedule import MonthlySchedule


class MonthlyScheduleRepository:

    @staticmethod
    def add(schedule):

        db.session.add(schedule)

    @staticmethod
    def commit():

        db.session.commit()

    @staticmethod
    def get(year, month):

        return MonthlySchedule.query.filter_by(
            year=year,
            month=month,
        ).first()

    @staticmethod
    def get_by_id(id):

        return db.session.get(
            MonthlySchedule,
            id,
        )

    @staticmethod
    def get_all():

        return (
            MonthlySchedule.query
            .order_by(
                MonthlySchedule.year.desc(),
                MonthlySchedule.month.desc(),
            )
            .all()
        )

    @staticmethod
    def get_previous(year, month):

        return (
            MonthlySchedule.query
            .filter(
                (MonthlySchedule.year < year)
                |
                (
                    (MonthlySchedule.year == year)
                    &
                    (MonthlySchedule.month < month)
                )
            )
            .order_by(
                MonthlySchedule.year.desc(),
                MonthlySchedule.month.desc(),
            )
            .first()
        )

    @staticmethod
    def delete(schedule):

        db.session.delete(schedule)

        db.session.flush()

    @staticmethod
    def delete_commit(schedule):

        db.session.delete(schedule)

        db.session.commit()