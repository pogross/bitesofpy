from random import random
from time import sleep


def cached_property(func):
    """decorator used to cache expensive object attribute lookup"""

    def get(self):
        try:
            return self._property_cache[func]
        except AttributeError:
            self._property_cache = {}
            x = self._property_cache[func] = func(self)
            return x
        except KeyError:
            x = self._property_cache[func] = func(self)
            return x

    return property(get)


class Planet:
    """the nicest little orb this side of Orion's Belt"""

    GRAVITY_CONSTANT = 42
    TEMPORAL_SHIFT = 0.12345
    SOLAR_MASS_UNITS = "M\N{SUN}"

    def __init__(self, color):
        self.color = color
        self._mass = None

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.color)})"

    @cached_property
    def mass(self):
        scale_factor = random()
        sleep(self.TEMPORAL_SHIFT)
        self._mass = (
            f"{round(scale_factor * self.GRAVITY_CONSTANT, 4)} "
            f"{self.SOLAR_MASS_UNITS}"
        )
        return self._mass
