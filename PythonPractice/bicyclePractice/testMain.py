from PythonPractice.bicyclePractice.testEBicycle import EBicycle

valume = int(input("电动车原剩余电量："))
eBicycle = EBicycle(valume)
add_valume = int(input("电动车充电电量："))
eBicycle.fill_charge(add_valume)
total_km = int(input("到达目的地一共需要骑行的里程数："))
eBicycle.run(total_km)