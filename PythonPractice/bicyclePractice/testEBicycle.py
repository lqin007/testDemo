from PythonPractice.bicyclePractice.testBicycle import Bicycle

class EBicycle(Bicycle):
    valume = 0
    def __init__ (self,valume):
        self.valume = valume
    def fill_charge(self,vol):
        self.valume = self.valume+vol
    def run(self,total_km):
        EBicycle_km = self.valume*10
        if (total_km-EBicycle_km) >0:
            Bicycle_km = total_km-EBicycle_km
            print(f"电动车骑行了{EBicycle_km}公里\n")
            #使用super().方法名或者super().属性名来访问父类的方法或属性
            print(f"自行车骑行了{super().run(Bicycle_km)}公里")
        else:
            print(f"电动车骑行了{EBicycle_km}公里\n")