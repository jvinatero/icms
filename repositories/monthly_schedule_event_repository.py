from extensions import db
from models.monthly_schedule_event import MonthlyScheduleEvent


class MonthlyScheduleEventRepository:

    @staticmethod
    def get(detail_id, meeting_type):

        return MonthlyScheduleEvent.query.filter_by(
            detail_id=detail_id,
            meeting_type=meeting_type
        ).first()

    @staticmethod
    def save(event):

        db.session.add(event)
        db.session.commit()