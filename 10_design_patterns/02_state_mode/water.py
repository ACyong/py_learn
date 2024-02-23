from state import Context, SolidState, LiquidState, GaseousState, State


class Water(Context):
    def __init__(self):
        super().__init__()
        self.add_state(SolidState("固态"))
        self.add_state(LiquidState("液态"))
        self.add_state(GaseousState("气态"))
        self.set_temperature(25)

    def get_temperature(self):
        return self.get_state_info()

    def set_temperature(self, temperature):
        self.set_state_info(temperature)

    def rise_temperature(self, step):
        self.set_temperature(self.get_temperature() + step)

    def reduce_temperature(self, step):
        self.set_temperature(self.get_temperature() - step)

    def behavior(self):
        state = self.get_state()
        if isinstance(state, State):
            state.behavior(self)


def test_water():
    water = Water()
    water.behavior()
    water.set_temperature(-4)
    water.behavior()
    water.rise_temperature(18)
    water.behavior()
    water.rise_temperature(110)
    water.behavior()


if __name__ == '__main__':
    test_water()
