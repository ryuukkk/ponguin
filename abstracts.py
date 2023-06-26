import abc
import functools

WIDTH, HEIGHT = 1100, 600
PADDING = 40
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG_ELEMENTS_COLOR = (200, 200, 200)
HOLE_COLOR = (0, 100, 100)
PADDLE_HEIGHT = 100
PADDLE_WIDTH = 20
BALL_RADIUS = 7
LEFT, RIGHT = -1, 1
GAME_STARTED = False
PLAY_WIDTH, PLAY_HEIGHT = WIDTH - 2 * PADDING, HEIGHT - 2 * PADDING
HOLE_HEIGHT = PLAY_HEIGHT * 0.6


# Meta-class that registers objects to their respective lists when they are created
class RegistrationMeta(abc.ABCMeta):

    def __new__(cls, classname, bases, attrs):
        attrs['instances'] = []
        return super().__new__(cls, classname, bases, attrs)

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        cls.instances.append(instance)
        return instance


# Descriptor that validates attributes of Paddle and Hole to lie within the play area.
class Validate:
    def __init__(self, attribute, mini, maxi):
        self.attribute = attribute
        self.mini = mini
        self.maxi = maxi

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, '_' + self.attribute)

    def __set__(self, instance, value):
        if self.mini > value:
            setattr(instance, '_' + self.attribute, self.mini)
        elif self.maxi < value:
            setattr(instance, '_' + self.attribute, self.maxi)
        else:
            setattr(instance, '_' + self.attribute, value)


# Abstract class for Rectangle objects (Hole and Paddle)
class RectObjects(abc.ABC, metaclass=RegistrationMeta):
    x = Validate('x', 0, WIDTH - PADDING)
    y = Validate('y', PADDING, HEIGHT - PADDING)
    width = Validate('width', min(PADDLE_WIDTH, PADDING),
                     max(PADDLE_WIDTH, PADDING))
    height = Validate('height', PLAY_HEIGHT / 6, PLAY_HEIGHT)
    side = Validate('side', LEFT, RIGHT)

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


def profiling(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        import cProfile
        profiler = cProfile.Profile()
        profiler.enable()
        function(*args, **kwargs)
        profiler.disable()
        return profiler.print_stats(sort='cumtime')

    return wrapper
