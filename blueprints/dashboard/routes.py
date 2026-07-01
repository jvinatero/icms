from flask import Blueprint, render_template

from models.group import Group
from models.area import Area

dashboard_bp = Blueprint(
    "dashboard",
    __name__
)


@dashboard_bp.route("/")
def index():

    total_groups = Group.query.count()

    total_areas = Area.query.count()

    active_areas = Area.query.filter_by(
        active=True
    ).count()

    inactive_areas = Area.query.filter_by(
        active=False
    ).count()

    return render_template(
        "dashboard/index.html",
        total_groups=total_groups,
        total_areas=total_areas,
        active_areas=active_areas,
        inactive_areas=inactive_areas,
    )