class Hero:
    hp=0
    power=0
    name=""

    def __init__(self, hp, power,name):
        self.hp = hp
        self.power = power
        self.name = name
    #回合格斗方法
    def fight(self,enemy):
        self.hp = self.hp - enemy.power
        enemy.hp = enemy.hp -self.power
        #我方胜利，输出英雄台词
        if self.hp > enemy.hp:
            print(f"{self.name}赢了")
            self.speak_lines()
        #对方胜利，输出对方台词
        elif self.hp < enemy.hp:
            print(f"{enemy.name}赢了")
            enemy.speak_lines()
        #打平，双方均输出台词
        elif self.hp == enemy.hp:
            print(f"双方打平~")
            self.speak_lines()
            enemy.speak_lines()