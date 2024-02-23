from observable import Observable
from observer import Observer


class WaterHeater(Observable):
    """热水器：战胜寒冬的有利武器"""

    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature
        print(f'当前温度是：{self.__temperature}℃')
        self.notify_observers()


class WashingMode(Observer):
    """该模块用于洗澡"""

    def update(self, observable, obj):
        if isinstance(observable, WaterHeater) and 50 <= observable.get_temperature() < 70:
            print('水已烧好，可以洗澡了')


class DrinkingMode(Observer):
    """该模块用于饮用"""

    def update(self, observable, obj):
        if isinstance(observable, WaterHeater) and observable.get_temperature() >= 100:
            print('水已烧开，可以饮用了')


def test_water_heater():
    heater = WaterHeater()
    washing = WashingMode()
    drinking = DrinkingMode()
    heater.add_observer(washing)
    heater.add_observer(drinking)
    heater.set_temperature(40)
    heater.set_temperature(60)
    heater.set_temperature(100)


if __name__ == '__main__':
    test_water_heater()
