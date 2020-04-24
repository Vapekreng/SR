from game.room.map_generator.titles.types_of_titles.base import base


class Titles:

    def __init__(self, base_name):
        self._base = base.TitleBase(base_name)
        self._mob = None

    def get_icon(self):
        icon = self._base.get_icon()
        if self._mob:
            icon = self._mob.get_icon()
        return icon

    def add_mob(self, mob):
        answer = False
        if self._mob is None:
            self._mob = mob
            answer = True
        return answer

    def remove_mob(self):
        self._mob = None

    def is_passable(self):
        answer = self._base.base_is_passable() and not self._mob
        return answer

    def is_transparent(self):
        return self._base.base_is_transparent()



