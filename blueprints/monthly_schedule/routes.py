from collections import OrderedDict

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    jsonify,
)

from repositories.monthly_schedule_repository import (
    MonthlyScheduleRepository,
)

from repositories.monthly_schedule_event_repository import (
    MonthlyScheduleEventRepository,
)

from services.monthly_schedule_service import (
    MonthlyScheduleService,
)

from services.monthly_schedule_event_service import (
    MonthlyScheduleEventService,
)

monthly_schedule_bp = Blueprint(
    "monthly_schedule",
    __name__,
    url_prefix="/monthly-schedule",
)


@monthly_schedule_bp.route("/")
def index():

    schedules = MonthlyScheduleRepository.get_all()

    return render_template(
        "monthly_schedule/index.html",
        schedules=schedules,
    )


@monthly_schedule_bp.route("/generate", methods=["POST"])
def generate():

    year = int(request.form["year"])
    month = int(request.form["month"])
    force = request.form.get("force") == "1"

    ok, msg = MonthlyScheduleService.generate(
        year,
        month,
        force,
    )

    flash(
        msg,
        "success" if ok else "danger",
    )

    return redirect(
        url_for("monthly_schedule.index")
    )


@monthly_schedule_bp.route("/delete/<int:id>")
def delete(id):

    schedule = MonthlyScheduleRepository.get_by_id(id)

    if schedule is None:

        flash(
            "Schedule not found.",
            "danger",
        )

    else:

        MonthlyScheduleRepository.delete_commit(schedule)

        flash(
            "Schedule deleted successfully.",
            "success",
        )

    return redirect(
        url_for("monthly_schedule.index")
    )


@monthly_schedule_bp.route("/preview/<int:id>")
def preview(id):

    schedule = MonthlyScheduleRepository.get_by_id(id)

    if schedule is None:

        flash(
            "Schedule not found.",
            "danger",
        )

        return redirect(
            url_for("monthly_schedule.index")
        )

    week_headers = OrderedDict()
    matrix = OrderedDict()

    details = sorted(
        schedule.details,
        key=lambda d: (
            d.display_order,
            d.week_no,
        ),
    )

    for detail in details:

        if detail.week_no not in week_headers:

            week_headers[detail.week_no] = {

                "friday": detail.friday_date,

                "sunday": detail.sunday_date,

            }

        friday = MonthlyScheduleEventRepository.get(
            detail.id,
            "Friday",
        )

        sunday = MonthlyScheduleEventRepository.get(
            detail.id,
            "Sunday",
        )

        detail.friday_done = (
            friday.completed
            if friday
            else False
        )

        detail.sunday_done = (
            sunday.completed
            if sunday
            else False
        )

        if detail.group_id not in matrix:

            matrix[detail.group_id] = {

                "group": detail.group,

                "weeks": OrderedDict(),

            }

        matrix[detail.group_id]["weeks"][detail.week_no] = detail

    months = [
        "",
        "JANUARY",
        "FEBRUARY",
        "MARCH",
        "APRIL",
        "MAY",
        "JUNE",
        "JULY",
        "AUGUST",
        "SEPTEMBER",
        "OCTOBER",
        "NOVEMBER",
        "DECEMBER",
    ]

    return render_template(

        "monthly_schedule/schedule.html",

        schedule=schedule,

        week_headers=week_headers,

        matrix=matrix,

        month_name=months[schedule.month],

    )


@monthly_schedule_bp.route("/toggle", methods=["POST"])
def toggle():

    data = request.get_json()

    completed = MonthlyScheduleEventService.toggle(

        int(data["detail_id"]),

        data["meeting_type"],

    )

    return jsonify({

        "success": True,

        "completed": completed,

    })

@monthly_schedule_bp.route("/print/<int:id>")
def print_schedule(id):

    schedule = MonthlyScheduleRepository.get_by_id(id)

    if schedule is None:

        flash(
            "Schedule not found.",
            "danger",
        )

        return redirect(
            url_for("monthly_schedule.index")
        )

    week_headers = OrderedDict()
    matrix = OrderedDict()

    details = sorted(
        schedule.details,
        key=lambda d: (
            d.display_order,
            d.week_no,
        ),
    )

    for detail in details:

        if detail.week_no not in week_headers:

            week_headers[detail.week_no] = {

                "friday": detail.friday_date,

                "sunday": detail.sunday_date,

            }

        friday = MonthlyScheduleEventRepository.get(
            detail.id,
            "Friday",
        )

        sunday = MonthlyScheduleEventRepository.get(
            detail.id,
            "Sunday",
        )

        detail.friday_done = (
            friday.completed
            if friday
            else False
        )

        detail.sunday_done = (
            sunday.completed
            if sunday
            else False
        )

        if detail.group_id not in matrix:

            matrix[detail.group_id] = {

                "group": detail.group,

                "weeks": OrderedDict(),

            }

        matrix[detail.group_id]["weeks"][detail.week_no] = detail

    months = [
        "",
        "JANUARY",
        "FEBRUARY",
        "MARCH",
        "APRIL",
        "MAY",
        "JUNE",
        "JULY",
        "AUGUST",
        "SEPTEMBER",
        "OCTOBER",
        "NOVEMBER",
        "DECEMBER",
    ]

    return render_template(

        "monthly_schedule/print.html",

        schedule=schedule,

        week_headers=week_headers,

        matrix=matrix,

        month_name=months[schedule.month],

    )