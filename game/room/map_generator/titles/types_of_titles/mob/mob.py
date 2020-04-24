from bearlibterminal import terminal

from game.room.map_generator.titles.types_of_titles.mob import mob_data


class Mob:

    def __init__(self, icon, color, x, y, radius_of_sight):
        self._icon = icon
        self._color = color
        self._x = x
        self._y = y
        self._used_keys = mob_data.USED_KEYS
        self._radius_of_sight = radius_of_sight

    def get_icon(self):
        return self._icon, self._color

    def set_coordinates(self, new_x, new_y):
        self._x = new_x
        self._y = new_y

    def get_coordinates(self):
        return self._x, self._y

    def get_command(self):
        new_key = terminal.read()
        while new_key not in self._used_keys:
            new_key = terminal.read()
        command = mob_data.COMMANDS[new_key]
        return command

    def get_radius_of_sight(self):
        return self._radius_of_sight
