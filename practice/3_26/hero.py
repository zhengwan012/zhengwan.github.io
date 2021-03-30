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
