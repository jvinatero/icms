from extensions import db


class Schedule(db.Model):

    __tablename__ = "schedules"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    schedule_date = db.Column(
        db.Date,
        nullable=False
    )

    assignment_id = db.Column(
        db.Integer,
        db.ForeignKey("assignments.id"),
        nullable=False
    )

    completed = db.Column(
        db.Boolean,
        default=False
    )

    remarks = db.Column(
        db.Text
    )

    assignment = db.relationship(
        "Assignment",
        lazy=True
    )