from game.room.map_generator.titles.types_of_titles.base import base_data


class TitleBase:

    def __init__(self, base_name):
        new_base = base_data.TITLES[base_name]
        self._icon = new_base['icon']
        self._color = new_base['color']
        self._is_passable = new_base['is passable']
        self._is_transparent = new_base['is transparent']

    def get_icon(self):
        return self._icon, self._color

    def base_is_passable(self):
        return self._is_passable

    def base_is_transparent(self):
        return self._is_transparent
