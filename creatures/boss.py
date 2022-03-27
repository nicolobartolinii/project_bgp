from enemy import *


class Boss(Enemy):
    def __init__(self, name: str, total_hp: int, ad: int, drops=None, coins: int = 0, ability_drop=None):
        super(Boss, self).__init__(name, total_hp, ad, drops, coins)
        self.ability_drop = ability_drop or []
