from extensions import db


class Assignment(db.Model):

    __tablename__ = "assignments"

    id = db.Column(
        db.Integer,
        primary_key=True
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
        nullable=False,
        default=1
    )

    active = db.Column(
        db.Boolean,
        default=True
    )

    group = db.relationship(
        "Group",
        back_populates="assignments"
    )

    area = db.relationship(
        "Area",
        back_populates="assignments"
    )

    def __repr__(self):

        return f"<Assignment {self.group_id} -> {self.area_id}>"