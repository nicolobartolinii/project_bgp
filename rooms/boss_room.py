from rooms.room import *
from creatures.boss import *


class BossRoom(Room):
    def __init__(self, floor: int = 0, cells=None, boss: Boss = None):
        super(BossRoom, self).__init__(floor, cells or [], None, None)
        self.boss = boss or None