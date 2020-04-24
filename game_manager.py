# Управление текущей игрой
# Запускает room_manager

from game.room import room_manager
from game.room.map_generator.titles.types_of_titles.mob import mob


def run():
    hero = mob.Mob('@', 'blue', 15, 15, 5)
    room_manager.run(hero)
