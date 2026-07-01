from datetime import datetime

from models.monthly_schedule_event import MonthlyScheduleEvent

from repositories.monthly_schedule_event_repository import (
    MonthlyScheduleEventRepository,
)


class MonthlyScheduleEventService:

    @staticmethod
    def toggle(detail_id, meeting_type):

        event = MonthlyScheduleEventRepository.get(
            detail_id,
            meeting_type,
        )

        if event is None:

            event = MonthlyScheduleEvent(

                detail_id=detail_id,

                meeting_type=meeting_type,

                completed=True,

                completed_on=datetime.now(),

            )

        else:

            event.completed = not event.completed

            event.completed_on = (
                datetime.now()
                if event.completed
                else None
            )

        MonthlyScheduleEventRepository.save(event)

        return event.completed