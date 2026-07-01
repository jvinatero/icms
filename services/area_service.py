from repositories.area_repository import AreaRepository
from models.area import Area


class AreaService:

    @staticmethod
    def get_all(search=""):

        if search:
            return AreaRepository.search(search)

        return AreaRepository.get_all()

    @staticmethod
    def create(
        area_code,
        area_name,
        category,
        estimated_minutes,
        display_order,
        map_color,
        active=True,
    ):

        area_code = area_code.strip().upper()
        area_name = area_name.strip()

        if not area_code:
            return False, "Area Code is required."

        if not area_name:
            return False, "Area Name is required."

        if AreaRepository.get_by_code(area_code):
            return False, "Area Code already exists."

        area = Area(
            area_code=area_code,
            area_name=area_name,
            category=category,
            estimated_minutes=int(estimated_minutes),
            display_order=int(display_order),
            map_order=int(display_order),
            map_color=map_color,
            active=active,
        )

        AreaRepository.add(area)

        return True, "Area added successfully."

    @staticmethod
    def update(
        area_id,
        area_code,
        area_name,
        category,
        estimated_minutes,
        display_order,
        map_color,
        active,
    ):

        area = AreaRepository.get(area_id)

        if not area:
            return False, "Area not found."

        duplicate = AreaRepository.get_by_code(
            area_code.upper()
        )

        if duplicate and duplicate.id != area.id:
            return False, "Area Code already exists."

        area.area_code = area_code.strip().upper()
        area.area_name = area_name.strip()
        area.category = category
        area.estimated_minutes = int(estimated_minutes)
        area.display_order = int(display_order)
        area.map_order = int(display_order)
        area.map_color = map_color
        area.active = active

        AreaRepository.update()

        return True, "Area updated successfully."

    @staticmethod
    def delete(area_id):

        area = AreaRepository.get(area_id)

        if not area:
            return False, "Area not found."

        AreaRepository.delete(area)

        return True, "Area deleted successfully."