from extensions import db


class Group(db.Model):

    __tablename__ = "groups"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    group_name = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    active = db.Column(
        db.Boolean,
        default=True
    )

    assignments = db.relationship(
        "Assignment",
        back_populates="group",
        lazy=True
    )

    def __repr__(self):

        return f"<Group {self.group_name}>"