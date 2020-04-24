# TODO: Сейчас выбирается тип ячейки и под нее такая же комната. Возможно, стоит выбирать тип ячейки, а под нее
#  случайную комнату, которая подходит для ячейки. Например в квадратную влезет нормал, хай, смол и квадратная

import random
from game.room.map_generator import map_generator_data as m_g_data
from game.room.map_generator.titles import titles
from game.room.map_generator.titles.types_of_titles.base import base_data


def _generate_list(range_x, range_y, fill_icon):
    new_list = []
    for _x in range(range_x):
        new_list.append([])
        for _y in range(range_y):
            new_list[_x].append(fill_icon)
    return new_list


def _select_random_type(types):
    max_dice = 0
    types_probabilities = []
    for room_type in types:
        probability = m_g_data.ROOMS[room_type]['probability']
        max_dice += probability
        types_probabilities.append(max_dice)
    type_index = 0
    dice = random.randint(1, max_dice)
    while types_probabilities[type_index] < dice:
        type_index += 1
    new_type = types[type_index]
    return new_type


def _generate_room(room_type, cell_index_x, cell_index_y):
    x0 = cell_index_x * m_g_data.CELL_SIZE_X
    y0 = cell_index_y * m_g_data.CELL_SIZE_X
    min_width = m_g_data.ROOMS[room_type]['min width']
    max_width = m_g_data.ROOMS[room_type]['max width']
    min_height = m_g_data.ROOMS[room_type]['min height']
    max_height = m_g_data.ROOMS[room_type]['max height']
    space_width = m_g_data.ROOMS[room_type]['cell width'] * m_g_data.CELL_SIZE_X
    space_height = m_g_data.ROOMS[room_type]['cell height'] * m_g_data.CELL_SIZE_Y
    room_width = random.randint(min_width, max_width)
    room_height = random.randint(min_height, max_height)
    free_space_x = space_width - room_width
    dx = random.randint(1, free_space_x - 1)
    free_space_y = space_height - room_height
    dy = random.randint(1, free_space_y - 1)
    room_x0 = x0 + dx
    room_y0 = y0 + dy
    return [room_x0, room_y0, room_width, room_height]


def _get_new_wave(current_wave, init_mark, c_map, final_mark):
    new_wave = []
    for point in current_wave:
        _x = point[0]
        _y = point[1]
        for vector in m_g_data.MOVE_VECTORS:
            dx = vector[0]
            dy = vector[1]
            try:
                if c_map[_x + dx][_y + dy] == init_mark:
                    new_wave.append([_x + dx, _y + dy])
                    c_map[_x + dx][_y + dy] = final_mark
            except IndexError:
                pass
    return new_wave, c_map


def _mark_zone(c_map, x0, y0, final_mark):
    init_mark = c_map[x0][y0]
    c_map[x0][y0] = final_mark
    start_point = [[x0, y0]]
    new_wave, c_map = _get_new_wave(start_point, init_mark, c_map, final_mark)
    while new_wave:
        current_wave = new_wave
        new_wave, c_map = _get_new_wave(current_wave, init_mark, c_map, final_mark)
    return c_map


def _get_point(c_map, marker):
    _x = random.randint(0, m_g_data.MAP_WIDTH - 1)
    _y = random.randint(0, m_g_data.MAP_HEIGHT - 1)
    while c_map[_x][_y] != marker:
        _x = random.randint(0, m_g_data.MAP_WIDTH - 1)
        _y = random.randint(0, m_g_data.MAP_HEIGHT - 1)
    return [_x, _y]


class Map:

    def __init__(self):
        self._map = _generate_list(m_g_data.MAP_WIDTH, m_g_data.MAP_HEIGHT, base_data.WALL_NAME)
        self._table_of_free_cells = _generate_list(m_g_data.CELLS_COUNT_X, m_g_data.CELLS_COUNT_Y, True)
        self._room_types = m_g_data.ROOMS.keys()
        self._generate_rooms()
        self._make_coherence()
        self._convert_map_to_titles()
        
    def get_map(self):
        return self._map

    def _generate_rooms(self):
        for cell_index_y in range(m_g_data.CELLS_COUNT_Y):
            for cell_index_x in range(m_g_data.CELLS_COUNT_X):
                if self._table_of_free_cells[cell_index_x][cell_index_y]:
                    good_types = self._get_good_types(cell_index_x, cell_index_y)
                    room_type = _select_random_type(good_types)
                    self._mark_cells_as_busy(room_type, cell_index_x, cell_index_y)
                    new_room = _generate_room(room_type, cell_index_x, cell_index_y)
                    self._add_room(new_room)

    def _get_good_types(self, _x, _y):
        good_types = []
        for room_type in self._room_types:
            if self._type_is_good(room_type, _x, _y):
                good_types.append(room_type)
        return good_types

    def _type_is_good(self, room_type, x0, y0):
        type_width = m_g_data.ROOMS[room_type]['cell width']
        type_height = m_g_data.ROOMS[room_type]['cell height']
        answer = True
        for _x in range(type_width):
            for _y in range(type_height):
                try:
                    if not self._table_of_free_cells[x0 + _x][y0 + _y]:
                        answer = False
                        break
                except IndexError:
                    answer = False
                    break
        return answer

    def _mark_cells_as_busy(self, room_type, x0, y0):
        width = m_g_data.ROOMS[room_type]['cell width']
        height = m_g_data.ROOMS[room_type]['cell height']
        for _x in range(width):
            for _y in range(height):
                # noinspection PyTypeChecker
                self._table_of_free_cells[x0 + _x][y0 + _y] = False

    def _add_room(self, room):
        x0 = room[0]
        y0 = room[1]
        width = room[2]
        height = room[3]
        for dx in range(width):
            for dy in range(height):
                self._map[x0 + dx][y0 + dy] = base_data.FLOOR_NAME

    def _get_coherence_map(self):
        coherence_map = _generate_list(m_g_data.MAP_WIDTH, m_g_data.MAP_HEIGHT, base_data.WALL_NAME)
        for _x in range(m_g_data.MAP_WIDTH):
            for _y in range(m_g_data.MAP_HEIGHT):
                coherence_map[_x][_y] = self._map[_x][_y]
        coherence_index = 0
        for _x in range(m_g_data.MAP_WIDTH):
            for _y in range(m_g_data.MAP_HEIGHT):
                if coherence_map[_x][_y] == base_data.FLOOR_NAME:
                    coherence_index += 1
                    coherence_map = _mark_zone(coherence_map, _x, _y, coherence_index)
        return coherence_map, coherence_index

    def _make_coherence(self):
        coherence_map, coherence_index = self._get_coherence_map()
        while coherence_index > 1:
            self._add_passage(coherence_map, coherence_index)
            coherence_map, coherence_index = self._get_coherence_map()

    def _add_passage(self, c_map, c_index):
        first_zone_marker = 1
        second_zone_marker = random.randint(2, c_index)
        first_point = _get_point(c_map, first_zone_marker)
        second_point = _get_point(c_map, second_zone_marker)
        self._connect_points(first_point, second_point)

    def _connect_points(self, first_point, second_point):
        x0 = first_point[0]
        x1 = second_point[0]
        y0 = first_point[1]
        y1 = second_point[1]
        dice = random.randint(0, 1)
        if (x0 == x1) or (y0 == y1):
            self._dig_passage(x0, y0, x1, y1)
        elif dice == 0:
            self._dig_passage(x0, y0, x1, y0)
            self._dig_passage(x1, y0, x1, y1)
        else:
            self._dig_passage(x0, y0, x0, y1)
            self._dig_passage(x0, y1, x1, y1)

    def _dig_passage(self, x0, y0, x1, y1):
        dx = 1
        if x0 == x1:
            dx = 0
        elif x0 > x1:
            dx = -1
        dy = 1
        if y0 == y1:
            dy = 0
        elif y0 > y1:
            dy = -1
        passage_length = max(abs(x0 - x1), abs(y0 - y1))
        for i in range(passage_length):
            current_x = x0 + i * dx
            current_y = y0 + i * dy
            self._map[current_x][current_y] = base_data.FLOOR_NAME
            
    def _convert_map_to_titles(self):
        for x in range(m_g_data.MAP_WIDTH):
            for y in range(m_g_data.MAP_HEIGHT):
                new_title_name = self._map[x][y]
                self._map[x][y] = titles.Titles(new_title_name)
