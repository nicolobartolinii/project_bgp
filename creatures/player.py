from creature import *
from items.weapon import *
from rooms.room import *


class Player(Creature):
    def __init__(self, name: str, total_hp: int, weapon: Weapon = None, inventory=None, coins: int = 0, current_room: Room = Room(1)):
        super(Player, self).__init__(name, total_hp)
        self.weapon = weapon
        self.inventory = inventory or []
        self.coins = coins
        self.current_room = current_room
