from creature import *


class Enemy(Creature):
    def __init__(self, name: str, total_hp: int, ad: int, drops=None, coins: int = 0):
        super(Enemy, self).__init__(name, total_hp)
        self.ad = ad
        self.drops = drops or []
        self.coins = coins
