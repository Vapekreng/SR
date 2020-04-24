from bearlibterminal import terminal
from game.room import room_data


def view_full_map(title_map):
    width = len(title_map)
    height = len(title_map[0])
    for x in range(width):
        for y in range(height):
            icon, color = title_map[x][y].get_icon()
            terminal.color(color)
            x0 = x + room_data.MAP_HORIZONTAL_START_POSITION
            y0 = y + room_data.MAP_VERTICAL_START_POSITION
            terminal.printf(x0, y0, icon)
    terminal.refresh()


def view_aos(titles, title_map):
    for title in titles:
        x, y = title
        icon, color = title_map[x][y].get_icon()
        terminal.color(color)
        x0 = x + room_data.MAP_HORIZONTAL_START_POSITION
        y0 = y + room_data.MAP_VERTICAL_START_POSITION
        terminal.printf(x0, y0, icon)
    terminal.refresh()

