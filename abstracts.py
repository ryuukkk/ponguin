import abc


class RegistrationMeta(abc.ABCMeta):

    def __new__(cls, classname, bases, attrs):
        attrs['_instances'] = []
        return super().__new__(cls, classname, bases, attrs)

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        cls._instances.append(instance)
        return instance

class RectObjects(abc.ABC, metaclass=RegistrationMeta):
    @abc.abstractmethod
    def __init__(self, x, y, width, height, side):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.side = side

    @abc.abstractmethod
    def draw(self, win):
        pass

    @abc.abstractmethod
    def move(self, win):
        pass
