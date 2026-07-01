from flask import Blueprint, render_template, request, flash

from models.group import Group
from models.area import Area
from services.assignment_service import AssignmentService

assignments_bp = Blueprint(
    "assignments",
    __name__,
    url_prefix="/assignments",
)


@assignments_bp.route("/")
def index():

    groups = (
        Group.query
        .filter_by(active=True)
        .order_by(Group.group_name)
        .all()
    )

    areas = (
        Area.query
        .filter_by(active=True)
        .order_by(Area.display_order)
        .all()
    )

    assignments = AssignmentService.get_all()

    assignment_map = {}

    for a in assignments:
        assignment_map[a.display_order] = {
            "group_id": a.group_id,
            "area_id": a.area_id
        }

    return render_template(
        "assignments/index.html",
        groups=groups,
        areas=areas,
        assignment_map=assignment_map,
    )


@assignments_bp.route("/save", methods=["POST"])
def save():

    ok, msg = AssignmentService.save(request.json)

    flash(msg, "success" if ok else "danger")

    return {
        "success": ok,
        "message": msg
    }