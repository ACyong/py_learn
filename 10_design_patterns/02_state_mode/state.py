from abc import ABCMeta, abstractmethod
from functools import wraps


class Context(metaclass=ABCMeta):
    """状态模式的上下文环境类"""

    def __init__(self):
        self.__states = []
        self.__cur_state = None
        # 状态发生变化依赖的属性，当这一变量由多个变量共同决定时，可以将其单独定义成一个类
        self.__state_info = 0

    def add_state(self, state):
        if state not in self.__states:
            self.__states.append(state)

    def change_state(self, state):
        if state is None:
            return False
        if self.__cur_state is None:
            print(f"初始化为{state.get_name()}")
        else:
            print(f"由{self.__cur_state.get_name()}变为{state.get_name()}")
        self.__cur_state = state
        self.add_state(state)
        return True

    def get_state(self):
        return self.__cur_state

    def set_state_info(self, state_info):
        self.__state_info = state_info
        for state in self.__states:
            if state.is_match(state_info):
                self.change_state(state)

    def get_state_info(self):
        return self.__state_info


class State(metaclass=ABCMeta):
    """状态类"""

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def is_match(self, state_info):
        """状态的属性state_info是否在当前的状态范围内"""
        return False

    @abstractmethod
    def behavior(self, obj):
        """状态对应的行为"""
        pass


# 单例的装饰器
def singleton(cls):
    instances = {}

    @wraps(cls)
    def __singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return __singleton


@singleton
class SolidState(State):
    """固态"""

    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info < 0

    def behavior(self, context):
        print(f"当前温度{context.get_state_info()}, 固态")


@singleton
class LiquidState(State):
    """液态"""

    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return 0 <= state_info < 100

    def behavior(self, context):
        print(f"当前温度{context.get_state_info()}, 液态")


@singleton
class GaseousState(State):
    """气态"""

    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info >= 100

    def behavior(self, context):
        print(f"当前温度{context.get_state_info()}, 气态")
