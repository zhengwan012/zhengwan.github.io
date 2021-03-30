class Bicycle:
    def run(self, miles):
        """
        :param miles: 骑行里程，要求为数字类型
        :return:
        """
        print(f"自行车骑行里程数为{miles}公里")


class EBicycle(Bicycle):
    # 构造函数，在类实例化的时候传入的参数
    def __init__(self, valume):
        """
        :param valume: 电池量
        """
        self.valume = valume  # 实例变量

    def fill_charge(self, add_volume):
        """
        :param add_volume: 充电变量
        :return:
        """
        self.valume += add_volume

    def run(self, miles):
        """
        每10km消耗1度电，当电消耗完后调用父类的run方法
        :param miles: 骑行公里数
        :return:
        """
        # 先计算电池量能够骑行多少km
        ele_miles = self.valume * 10
        # 再计算剩余公里数
        res_miles = ele_miles - miles
        if res_miles >= 0:
            print(f"骑行的总公里数为{miles}")
        else:
            print(f"使用电动车骑行的公里数为{ele_miles}")
            # 如果子类重写了父类，那么又需要去调用父类的属性，可以使用super（）
            super().run(miles - ele_miles)


if __name__ == "__main__":
    ebike = EBicycle(100)
    ebike.run(10000)
