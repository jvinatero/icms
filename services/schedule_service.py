from datetime import date

from models.schedule import Schedule
from services.assignment_service import AssignmentService
from repositories.schedule_repository import ScheduleRepository


class ScheduleService:

    @staticmethod
    def generate(schedule_date):

        assignments = AssignmentService.get_all()

        if not assignments:
            return False, "No assignments found."

        ScheduleRepository.delete_by_date(schedule_date)

        for assignment in assignments:

            ScheduleRepository.add(

                Schedule(

                    schedule_date=schedule_date,

                    assignment_id=assignment.id,

                    completed=False

                )

            )

        ScheduleRepository.commit()

        return True, "Schedule generated successfully."