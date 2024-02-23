class Observable:
    """被观察着的基类"""

    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self, obj=0):
        for o in self.__observers:
            o.update(self, obj)
