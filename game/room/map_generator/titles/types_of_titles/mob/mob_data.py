from bearlibterminal import terminal

USED_KEYS = [terminal.TK_ESCAPE, terminal.TK_LEFT, terminal.TK_RIGHT, terminal.TK_DOWN, terminal.TK_UP]
COMMANDS = dict()
COMMANDS[terminal.TK_ESCAPE] = 'quit'
COMMANDS[terminal.TK_LEFT] = 'move left'
COMMANDS[terminal.TK_RIGHT] = 'move right'
COMMANDS[terminal.TK_DOWN] = 'move down'
COMMANDS[terminal.TK_UP] = 'move up'
