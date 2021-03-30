class House:
    def __init__(self):
        # 类的属性
        self.door = ""
        self.floor = ""

    # 类的方法
    def cook(self):
        print("我在厨房炸鸡排")

    def sleep(self):
        print("我在卧室睡觉")


if __name__ == "__main__":
    bob_house = House()
    bob_house.door = "white"
    bob_house.floor = "black"
    # 修改实例的属性不会影响到类本身
    print("house.door:", House().door)
    # 修改当前实例的属性不会影响到其它实例
    mary_house = House()
    print(mary_house)
