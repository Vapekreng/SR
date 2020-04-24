# Основной модуль
# Инициализирует терминал
# Запускает game_manager

from game import game_manager
from main_manager_data import DEFAULT_FONT_NAME, DEFAULT_FONT_SIZE
from bearlibterminal import terminal

terminal.open()
terminal.set('font: ' + DEFAULT_FONT_NAME + ', size=' + DEFAULT_FONT_SIZE)
game_manager.run()
