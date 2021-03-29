from PythonPractice.heroPractice.police import Police
from PythonPractice.heroPractice.timo import Timo

class HeroFactory:
    #创建英雄的方法
    def creatHero(self, name):
        if name == "timo":
            return Timo(530, 10, "timo")
        elif name == "police":
            return Police(510, 20, "police")
        else:
            raise Exception("工厂中没有此英雄！")
