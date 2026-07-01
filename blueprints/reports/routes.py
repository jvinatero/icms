from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
)

from repositories.monthly_schedule_repository import (
    MonthlyScheduleRepository,
)

reports_bp = Blueprint(
    "reports",
    __name__,
    url_prefix="/reports",
)


@reports_bp.route("/print-schedule")
def print_schedule():

    schedules = MonthlyScheduleRepository.get_all()

    return render_template(
        "reports/print_schedule.html",
        schedules=schedules,
    )


@reports_bp.route("/preview/<int:id>")
def preview(id):

    schedule = MonthlyScheduleRepository.get_by_id(id)

    if schedule is None:

        flash(
            "Schedule not found.",
            "danger",
        )

        return redirect(
            url_for("reports.print_schedule")
        )

    return redirect(
        url_for(
            "monthly_schedule.preview",
            id=id,
        )
    )


@reports_bp.route("/print/<int:id>")
def print(id):

    schedule = MonthlyScheduleRepository.get_by_id(id)

    if schedule is None:

        flash(
            "Schedule not found.",
            "danger",
        )

        return redirect(
            url_for("reports.print_schedule")
        )

    return redirect(
        url_for(
            "monthly_schedule.print_schedule",
            id=id,
        )
    )