"""
使用简单工厂方法， 实现timo 和 police 两个英雄
一个回合制游戏，有两个英雄，分别以两个类进行定义。分别是timo和police。每个英雄都有 hp 属性和 power属性，hp 代表血量，power 代表攻击力

每个英雄都有一个 fight 方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个 hp 进行对比，血量剩余多的人获胜

每个英雄都一个speak_lines方法
调用speak_lines方法，不同的角色会打印（讲出）不同的台词
timo : 提莫队长正在待命
police: 见识一下法律的子弹
"""

from timo import Timo
from police import Police


class HeroFactory:
    """
    简单工厂模式专门定义一个类来负责创建其它类型的英雄的实例
    1、职责清晰
    2、提供了一个入口，比如添加了新的英雄，其他研发调用代码的过程中，可以以factory为主，不需要一个个文件的去读写
    """
    def create_hero(self, name):
        if name == "timo":
            return Timo()
        elif name == "police":
            return Police()
        else:
            raise Exception("此英雄不在英雄工厂中")


if __name__ == "__main__":
    hero_factory = HeroFactory()
    # import库可以使用alt+回车快捷键
    timo = hero_factory.create_hero('timo')
    police = hero_factory.create_hero('police')
    # timo.fight(police.power, police.hp)
    police.fight(timo.power, timo.hp)
    timo.speak_lines('timo')
    police.speak_lines('police')

