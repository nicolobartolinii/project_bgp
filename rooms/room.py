from creatures.enemy import *
from creatures.npc import *


class Room:
    def __init__(self, floor: int = 0, cells=None, enemies=None, npcs=None):
        self.floor = floor
        self.cells = cells or []
        self.enemies = enemies or []
        self.npcs = npcs or []
