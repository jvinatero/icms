from extensions import db
from models.schedule import Schedule


class ScheduleRepository:

    @staticmethod
    def get_all():

        return (
            Schedule.query
            .order_by(
                Schedule.schedule_date.desc()
            )
            .all()
        )

    @staticmethod
    def add(schedule):

        db.session.add(schedule)

    @staticmethod
    def commit():

        db.session.commit()

    @staticmethod
    def delete_by_date(schedule_date):

        Schedule.query.filter_by(
            schedule_date=schedule_date
        ).delete()

        db.session.commit()