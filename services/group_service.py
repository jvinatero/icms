from repositories.group_repository import GroupRepository
from models.group import Group


class GroupService:

    @staticmethod
    def get_all(search=""):

        if search:
            return GroupRepository.search(search)

        return GroupRepository.get_all()

    @staticmethod
    def create(name):

        if not name:
            return False, "Group name is required."

        if GroupRepository.get_by_name(name):
            return False, "Group already exists."

        GroupRepository.add(
            Group(group_name=name)
        )

        return True, "Group added successfully."

    @staticmethod
    def update(group_id, name):

        group = GroupRepository.get(group_id)

        if not group:
            return False, "Group not found."

        duplicate = GroupRepository.get_by_name(name)

        if duplicate and duplicate.id != group.id:
            return False, "Group already exists."

        group.group_name = name

        GroupRepository.update()

        return True, "Group updated successfully."

    @staticmethod
    def delete(group_id):

        group = GroupRepository.get(group_id)

        if not group:
            return False, "Group not found."

        GroupRepository.delete(group)

        return True, "Group deleted."