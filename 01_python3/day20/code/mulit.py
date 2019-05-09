class Car:
    def run(self, speed):
        print("汽车以", speed, "km/h的速度行驶")

class Plane:
    def fly(self, height):
        print("飞机以海拔", height, "米的高度飞行")

class PlaneCar(Car, Plane):
    pass


p1 = PlaneCar()
p1.fly(1000)
p1.run(280)


