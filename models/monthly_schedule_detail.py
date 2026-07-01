from extensions import db


class MonthlyScheduleDetail(db.Model):

    __tablename__ = "monthly_schedule_details"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    schedule_id = db.Column(
        db.Integer,
        db.ForeignKey("monthly_schedules.id"),
        nullable=False
    )

    week_no = db.Column(
        db.Integer,
        nullable=False
    )

    friday_date = db.Column(
        db.Date,
        nullable=False
    )

    sunday_date = db.Column(
        db.Date,
        nullable=False
    )

    group_id = db.Column(
        db.Integer,
        db.ForeignKey("groups.id"),
        nullable=False
    )

    area_id = db.Column(
        db.Integer,
        db.ForeignKey("areas.id"),
        nullable=False
    )

    display_order = db.Column(
        db.Integer,
        nullable=False
    )

    schedule = db.relationship(
        "MonthlySchedule",
        back_populates="details"
    )

    group = db.relationship(
        "Group"
    )

    area = db.relationship(
        "Area"
    )

    def __repr__(self):

        return (
            f"<MonthlyScheduleDetail "
            f"Week {self.week_no} "
            f"Group {self.group_id} "
            f"Area {self.area_id}>"
        )