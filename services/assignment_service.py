from models.assignment import Assignment
from repositories.assignment_repository import AssignmentRepository


class AssignmentService:

    @staticmethod
    def get_all():
        return AssignmentRepository.get_all()

    @staticmethod
    def save(assignments):

        if not assignments:
            return False, "No assignments to save."

        used_groups = set()
        used_areas = set()

        # ---------- Validate ----------

        for row in assignments:

            group_id = row.get("group_id")
            area_id = row.get("area_id")

            if not group_id:
                return False, "Every row must have a Cleaning Group."

            if not area_id:
                return False, "Every row must have a Cleaning Area."

            group_id = int(group_id)
            area_id = int(area_id)

            if group_id in used_groups:
                return False, "Duplicate Cleaning Group."

            if area_id in used_areas:
                return False, "Duplicate Cleaning Area."

            used_groups.add(group_id)
            used_areas.add(area_id)

        # ---------- Save ----------

        AssignmentRepository.delete_all()

        for row in assignments:

            AssignmentRepository.add(

                Assignment(

                    display_order=int(row["display_order"]),
                    group_id=int(row["group_id"]),
                    area_id=int(row["area_id"]),
                    active=True

                )

            )

        AssignmentRepository.commit()

        return True, "Assignments saved successfully."