from calendar import monthcalendar
from datetime import date

from models.monthly_schedule import MonthlySchedule
from models.monthly_schedule_detail import MonthlyScheduleDetail

from repositories.assignment_repository import AssignmentRepository
from repositories.monthly_schedule_repository import (
    MonthlyScheduleRepository,
)


class MonthlyScheduleService:

    @staticmethod
    def generate(year, month, force=False):

        existing = MonthlyScheduleRepository.get(year, month)

        if existing:

            if not force:
                return False, "Schedule already exists."

            MonthlyScheduleRepository.delete(existing)

        assignments = AssignmentRepository.get_all()

        if not assignments:
            return False, "No Assignment Board found."

        previous = MonthlyScheduleRepository.get_previous(
            year,
            month,
        )

        start_rotation = 0

        if previous and previous.details:

            last_week = max(
                d.week_no
                for d in previous.details
            )

            start_rotation = last_week % len(assignments)

        calendar = monthcalendar(year, month)

        fridays = []
        sundays = []

        for week in calendar:

            if week[4]:
                fridays.append(date(year, month, week[4]))

            if week[6]:
                sundays.append(date(year, month, week[6]))

        total_weeks = min(
            len(fridays),
            len(sundays),
        )

        schedule = MonthlySchedule(
            year=year,
            month=month,
        )

        MonthlyScheduleRepository.add(schedule)
        MonthlyScheduleRepository.commit()

        areas = [a.area for a in assignments]

        for week in range(total_weeks):

            rotation = (start_rotation + week) % len(areas)

            for order, assignment in enumerate(assignments):

                area = areas[
                    (order + rotation) % len(areas)
                ]

                detail = MonthlyScheduleDetail(
                    schedule_id=schedule.id,
                    week_no=week + 1,
                    friday_date=fridays[week],
                    sunday_date=sundays[week],
                    group_id=assignment.group_id,
                    area_id=area.id,
                    display_order=order + 1,
                )

                schedule.details.append(detail)

        MonthlyScheduleRepository.commit()

        return True, "Monthly schedule generated successfully."