from extensions import db


class MonthlyScheduleEvent(db.Model):

    __tablename__ = "monthly_schedule_events"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    detail_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "monthly_schedule_details.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    meeting_type = db.Column(
        db.String(10),
        nullable=False,
    )

    completed = db.Column(
        db.Boolean,
        default=False,
        nullable=False,
    )

    completed_on = db.Column(
        db.DateTime,
    )

    completed_by = db.Column(
        db.String(100),
    )

    detail = db.relationship(
        "MonthlyScheduleDetail",
        passive_deletes=True,
    )

    def __repr__(self):

        return (
            f"<MonthlyScheduleEvent "
            f"{self.detail_id} "
            f"{self.meeting_type}>"
        )