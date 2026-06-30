from flask import Blueprint, render_template, request, redirect, flash, url_for

from services.group_service import GroupService

groups_bp = Blueprint(
    "groups",
    __name__,
    url_prefix="/groups"
)


@groups_bp.route("/")
def index():

    search = request.args.get("search", "").strip()

    groups = GroupService.get_all(search)

    return render_template(
        "groups/index.html",
        groups=groups,
        search=search
    )


@groups_bp.route("/add", methods=["POST"])
def add():

    name = request.form["group_name"].strip()

    ok, msg = GroupService.create(name)

    flash(msg, "success" if ok else "danger")

    return redirect(url_for("groups.index"))


@groups_bp.route("/delete/<int:id>")
def delete(id):

    ok, msg = GroupService.delete(id)

    flash(msg, "success" if ok else "danger")

    return redirect(url_for("groups.index"))

@groups_bp.route("/edit/<int:id>", methods=["POST"])
def edit(id):

    name = request.form["group_name"].strip()

    ok, msg = GroupService.update(id, name)

    flash(msg, "success" if ok else "danger")

    return redirect(url_for("groups.index"))