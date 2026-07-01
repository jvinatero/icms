from extensions import db


class Area(db.Model):

    __tablename__ = "areas"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    area_code = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    area_name = db.Column(
        db.String(100),
        nullable=False
    )

    category = db.Column(
        db.String(50)
    )

    estimated_minutes = db.Column(
        db.Integer,
        default=0
    )

    display_order = db.Column(
        db.Integer,
        default=1
    )

    map_color = db.Column(
        db.String(20),
        default="#D9D9D9"
    )

    map_order = db.Column(
        db.Integer,
        default=1
    )

    active = db.Column(
        db.Boolean,
        default=True
    )

    assignments = db.relationship(
        "Assignment",
        back_populates="area",
        lazy=True
    )

    def __repr__(self):

        return f"<Area {self.area_name}>"