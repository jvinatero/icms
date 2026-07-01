from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)

from services.area_service import AreaService

areas_bp = Blueprint(
    "areas",
    __name__,
    url_prefix="/areas",
)


@areas_bp.route("/")
def index():

    search = request.args.get("search", "")

    areas = AreaService.get_all(search)

    return render_template(
        "areas/index.html",
        areas=areas,
        search=search,
    )


@areas_bp.route("/add", methods=["POST"])
def add():

    ok, msg = AreaService.create(

        request.form["area_code"],

        request.form["area_name"],

        request.form["category"],

        request.form["estimated_minutes"],

        request.form["display_order"],

        request.form["map_color"],

        "active" in request.form,

    )

    flash(
        msg,
        "success" if ok else "danger",
    )

    return redirect(
        url_for("areas.index")
    )


@areas_bp.route("/edit/<int:id>", methods=["POST"])
def edit(id):

    ok, msg = AreaService.update(

        id,

        request.form["area_code"],

        request.form["area_name"],

        request.form["category"],

        request.form["estimated_minutes"],

        request.form["display_order"],

        request.form["map_color"],

        "active" in request.form,

    )

    flash(
        msg,
        "success" if ok else "danger",
    )

    return redirect(
        url_for("areas.index")
    )


@areas_bp.route("/delete/<int:id>")
def delete(id):

    ok, msg = AreaService.delete(id)

    flash(
        msg,
        "success" if ok else "danger",
    )

    return redirect(
        url_for("areas.index")
    )