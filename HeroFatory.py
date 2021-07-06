# -*- coding: utf-8 -*-
from Hero_list import Timo, Jinx


class HeroFatory:
    def create_hero(self, name):
        if name == "timo":
            return Timo()

        elif name == "jinx":
            return Jinx()
        else:
            raise Exception("不在英雄池内")


if __name__ == "__main__":
    hero = HeroFatory()
    timo = hero.create_hero("timo")
    jinx = hero.create_hero("jinx")
    # timo.fight(1000, 200, "jinx")
    result = timo.fight(1000, 200, "jinx")
    timo.level_up(1000, 200, result)
