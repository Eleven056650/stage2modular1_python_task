# -*- coding: utf-8 -*-
import random


class Hero:
    # def __init__(self, hero_hp, hero_power, hero_name):        # 构造通用属性：血量、攻击力
    #     self.hero_hp = hero_hp
    #     self.hero_power = hero_power
    #     self.hero_name = hero_name

    hero_hp = 0
    hero_power = 0
    hero_name = ""

    def fight(self, enemy_hp, enemy_power, enemy_name, hero_win=1):
        hero_final_hp = self.hero_hp - enemy_power
        enemy_final_hp = enemy_hp - self.hero_power
        self.enemy_name = enemy_name

        if hero_final_hp > enemy_final_hp:
            print(f"{self.hero_name}获胜！")
        elif hero_final_hp < enemy_final_hp:
            print(f"{self.enemy_name}获胜！")
            hero_win = 0
        else:
            print("双方平局！")
            hero_win = 0
        return hero_win

    # 战斗狂人模式 ， 战斗失败后可调用属性（血量）升级方法，直至战斗获胜
    def level_up(self, enemy_hp, enemy_power, hero_win):
        up_total = 0  # 初始化属性（血量）提升总和
        i = 1  # 初始化提升次数
        print(f"我方{self.hero_name}战斗失败，需提升属性")
        while hero_win == 0:  # 循环标识，战斗失败则继续提升（血量）
            up_num = random.randint(10, 100)
            print(f"第{i}次提升属性，提升{up_num}")
            self.hero_hp = self.hero_hp + up_num  # 多次循环的属性值（血量）叠加
            hero_final_hp_update = self.hero_hp - enemy_power
            if hero_final_hp_update > (enemy_hp - self.hero_power):
                print(f"{self.hero_name}获胜！")
                hero_win = 1  # 战斗获胜，循环标识置1，跳出循环，战斗结束
            elif hero_final_hp_update < (enemy_hp - self.hero_power):
                print(f"仍是{self.enemy_name}获胜！")  # 战斗失败，继续循环，并打印内容
            up_total = up_total + up_num  # 属性（血量）提升总和计算
            i += 1  # 计数
        print(f"总共升级属性值为{up_total}")


class Timo(Hero):
    ## 自定义构造英雄属性，可在HeroFatory中增加变量"create_hero(self, hp, power, name):"并返回"Timo(hp, power, name)"
    # def __init__(self, hero_hp, hero_power, hero_name):
    #     Hero.__init__(self, hero_hp, hero_power, hero_name)       #继承父类构造函数

    hero_hp = 1000
    hero_power = 100
    hero_name = "timo"


class Jinx(Hero):
    # def __init__(self, hero_hp, hero_power, hero_name):
    #     Hero.__init__(self, hero_hp, hero_power, hero_name)
    hero_hp = 1500
    hero_power = 100
    hero_name = "jinx"
