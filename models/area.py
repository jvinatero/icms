from extensions import db


class Area(db.Model):

    __tablename__ = "areas"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    area_code = db.Column(
        db.String(10),
        unique=True,
        nullable=False
    )

    area_name = db.Column(
        db.String(100),
        nullable=False
    )

    category = db.Column(
        db.String(30),
        nullable=False
    )

    estimated_minutes = db.Column(
        db.Integer,
        nullable=False,
        default=30
    )

    display_order = db.Column(
        db.Integer,
        nullable=False,
        default=1
    )

    color = db.Column(
        db.String(20),
        nullable=False,
        default="#0d6efd"
    )

    active = db.Column(
        db.Boolean,
        default=True
    )

    remarks = db.Column(
        db.Text
    )

    def __repr__(self):
        return f"<Area {self.area_name}>"