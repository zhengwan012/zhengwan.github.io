from ez import EZ
from hero import Hero


class Jinx(Hero):
    hp = 2000
    power = 210
    name = "jinx"


if __name__ == "__main__":
    jinx = Jinx()
    # import库可以使用alt+回车快捷键
    ez = EZ()
    ez.fight(jinx.power, jinx.hp)
