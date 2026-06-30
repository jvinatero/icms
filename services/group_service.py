from models.group import Group
from repositories.group_repository import GroupRepository


class GroupService:

    @staticmethod
    def get_all():
        return GroupRepository.get_all()

    @staticmethod
    def create(name):

        if GroupRepository.get_by_name(name):
            return False, "Group already exists."

        group = Group(group_name=name)

        GroupRepository.add(group)

        return True, "Group added successfully."