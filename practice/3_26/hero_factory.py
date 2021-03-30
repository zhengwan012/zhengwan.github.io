from jinx import Jinx
from ez import EZ


class HeroFactory:

    """
    简单工厂模式专门定义一个类来负责创建其它类型的英雄的实例
    1、职责清晰
    2、提供了一个入口，比如添加了新的英雄，其他研发调用代码的过程中，可以以factory为主，不需要一个个文件的去读写
    """
    def create_hero(self, name):
        if name == "jinx":
            return Jinx()
        elif name == "ez":
            return EZ()
        else:
            raise Exception("此英雄不在英雄工厂中")


if __name__ == "__main__":
    hero_factory = HeroFactory()
    # import库可以使用alt+回车快捷键
    jinx = hero_factory.create_hero('jinx')
    ez = hero_factory.create_hero('ez')
    ez.fight(jinx.power, jinx.hp)
