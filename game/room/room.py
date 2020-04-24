from game.room.map_generator import map_generator
from game.room import room_data
from game.room import area_of_sight
from game.room import room_viewer


class Room:

    def __init__(self):
        self._mobs = []
        self.current_mob = None
        self.current_command = None
        self._map = map_generator.Map().get_map()
        self.make_action = dict()
        self.make_action['move left'] = self._move_mob
        self.make_action['move right'] = self._move_mob
        self.make_action['move up'] = self._move_mob
        self.make_action['move down'] = self._move_mob
        self.make_action['quit'] = self.quit

    def get_map(self):
        return self._map

    def get_mobs(self):
        return self._mobs

    def _move_mob(self):
        mob = self.current_mob
        command = self.current_command
        dx, dy = room_data.MOVE_VECTORS[command]
        x0, y0 = mob.get_coordinates()
        new_x = x0 + dx
        new_y = y0 + dy
        if self._title_in_map(new_x, new_y):
            if self._map[new_x][new_y].is_passable():
                self._map[x0][y0].remove_mob()
                self._map[new_x][new_y].add_mob(mob)
                mob.set_coordinates(new_x, new_y)

    def set_current_mob(self, mob):
        self.current_mob = mob

    def set_current_command(self, command):
        self.current_command = command

    def add_mob(self, mob):
        self._mobs.append(mob)
        x, y = mob.get_coordinates()
        self._map[x][y].add_mob(mob)

    def quit(self):
        pass

    def _title_in_map(self, x, y):
        answer = True
        try:
            # noinspection PyUnusedLocal
            title = self._map[x][y]
        except IndexError:
            answer = False
        return answer

    def get_map_of_transparency(self):
        map_of_transparency = []
        width = len(self._map)
        height = len(self._map[0])
        for x in range(width):
            map_of_transparency.append([])
            for y in range(height):
                map_of_transparency[x].append(self._map[x][y].is_transparent())
        return map_of_transparency

    def hero_looks_around(self):
        x0, y0 = self.current_mob.get_coordinates()
        radius_of_sight = self.current_mob.get_radius_of_sight()
        map_of_transparency = self.get_map_of_transparency()
        visible_titles = area_of_sight.AoS(x0, y0, radius_of_sight, map_of_transparency).get_aos()
        room_viewer.view_aos(visible_titles, self.get_map())
