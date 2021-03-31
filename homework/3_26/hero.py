class Hero:
    hp = 0
    power = 0
    name = ""

    def fight(self, enemy_power, enemy_hp):
        my_hp = self.hp - enemy_power  # 我的血量
        enemy_final_hp = enemy_hp - self.power  # 敌人的血量
        if my_hp > enemy_final_hp:
            print(f"{self.name} 赢了")
        elif my_hp == enemy_final_hp:
            print("打成平手")
        else:
            print("敌人赢了")

    def speak_lines(self, name):
        if name == 'timo':
            print("提莫队长正在待命")
        elif name == "police":
            print("见识一下法律的子弹")
