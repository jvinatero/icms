from extensions import db


class MonthlySchedule(db.Model):

    __tablename__ = "monthly_schedules"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    year = db.Column(
        db.Integer,
        nullable=False
    )

    month = db.Column(
        db.Integer,
        nullable=False
    )

    generated_on = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        nullable=False
    )

    details = db.relationship(
        "MonthlyScheduleDetail",
        back_populates="schedule",
        cascade="all, delete-orphan",
        order_by="MonthlyScheduleDetail.week_no, MonthlyScheduleDetail.display_order"
    )

    def __repr__(self):

        return f"<MonthlySchedule {self.year}-{self.month:02d}>"