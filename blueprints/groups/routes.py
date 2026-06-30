from flask import Blueprint, render_template, request, redirect, flash

from services.group_service import GroupService

groups_bp = Blueprint(
    "groups",
    __name__,
    url_prefix="/groups"
)


@groups_bp.route("/")
def index():

    groups = GroupService.get_all()

    return render_template(
        "groups/index.html",
        groups=groups
    )


@groups_bp.route("/add", methods=["POST"])
def add():

    name = request.form["group_name"].strip()

    ok, msg = GroupService.create(name)

    flash(msg, "success" if ok else "danger")

    return redirect("/groups/")