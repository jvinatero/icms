from datetime import datetime

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)

from services.schedule_service import ScheduleService
from repositories.schedule_repository import ScheduleRepository

schedules_bp = Blueprint(
    "schedules",
    __name__,
    url_prefix="/schedules",
)


@schedules_bp.route("/")
def index():

    schedules = ScheduleRepository.get_all()

    return render_template(
        "schedules/index.html",
        schedules=schedules,
    )


@schedules_bp.route("/generate", methods=["POST"])
def generate():

    schedule_date = datetime.strptime(
        request.form["schedule_date"],
        "%Y-%m-%d"
    ).date()

    ok, msg = ScheduleService.generate(
        schedule_date
    )

    flash(
        msg,
        "success" if ok else "danger"
    )

    return redirect(
        url_for("schedules.index")
    )