from extensions import db
from models.assignment import Assignment


class AssignmentRepository:

    @staticmethod
    def get_all():

        return (
            Assignment.query
            .filter_by(active=True)
            .order_by(Assignment.display_order)
            .all()
        )

    @staticmethod
    def get(id):

        return db.session.get(
            Assignment,
            id
        )

    @staticmethod
    def add(assignment):

        db.session.add(assignment)

    @staticmethod
    def delete_all():

        Assignment.query.delete()

    @staticmethod
    def commit():

        db.session.commit()