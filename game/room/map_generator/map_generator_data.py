MAP_WIDTH = 80
MAP_HEIGHT = 20
CELL_SIZE_X = 10
CELL_SIZE_Y = 10
CELLS_COUNT_X = MAP_WIDTH // CELL_SIZE_X
CELLS_COUNT_Y = MAP_HEIGHT // CELL_SIZE_Y
MOVE_VECTORS = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


ROOMS = dict()

ROOMS['normal'] = dict()
ROOMS['normal']['min width'] = 9
ROOMS['normal']['max width'] = 15
ROOMS['normal']['min height'] = 4
ROOMS['normal']['max height'] = 7
ROOMS['normal']['cell width'] = 2
ROOMS['normal']['cell height'] = 1
ROOMS['normal']['probability'] = 30

ROOMS['small'] = dict()
ROOMS['small']['min width'] = 6
ROOMS['small']['max width'] = 8
ROOMS['small']['min height'] = 6
ROOMS['small']['max height'] = 8
ROOMS['small']['cell width'] = 1
ROOMS['small']['cell height'] = 1
ROOMS['small']['probability'] = 5

ROOMS['high'] = dict()
ROOMS['high']['min width'] = 7
ROOMS['high']['max width'] = 8
ROOMS['high']['min height'] = 7
ROOMS['high']['max height'] = 13
ROOMS['high']['cell width'] = 1
ROOMS['high']['cell height'] = 2
ROOMS['high']['probability'] = 25

ROOMS['wide'] = dict()
ROOMS['wide']['min width'] = 19
ROOMS['wide']['max width'] = 27
ROOMS['wide']['min height'] = 4
ROOMS['wide']['max height'] = 7
ROOMS['wide']['cell width'] = 3
ROOMS['wide']['cell height'] = 1
ROOMS['wide']['probability'] = 35

ROOMS['square'] = dict()
ROOMS['square']['min width'] = 13
ROOMS['square']['max width'] = 17
ROOMS['square']['min height'] = 9
ROOMS['square']['max height'] = 13
ROOMS['square']['cell width'] = 2
ROOMS['square']['cell height'] = 2
ROOMS['square']['probability'] = 5
