from game.room import room


def run(hero):
    new_room = room.Room()
    new_room.add_mob(hero)
    new_room.set_current_mob(hero)
    new_room.hero_looks_around()
    command = new_room.current_mob.get_command()
    new_room.set_current_command(command)
    while command != 'quit':
        new_room.make_action[command]()
        new_room.hero_looks_around()
        command = new_room.current_mob.get_command()
        new_room.set_current_command(command)

