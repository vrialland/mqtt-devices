import machine
import neopixel


LEDS_ALL = const(-1)
ZERO = const(0)


class WS2812:
    def __init__(self, gpio_pin, nb_leds):
        self.nb_leds = nb_leds
        self._np = neopixel.NeoPixel(machine.Pin(gpio_pin), nb_leds)

    def _set_color(self, r=ZERO, g=ZERO, b=ZERO, index=LEDS_ALL):
        if not 0 <= index < self.nb_leds:
            raise IndexError("Invalid led index")
        self._np[index] = (r, g, b)

    def set_color(self, r=ZERO, g=ZERO, b=ZERO, index=LEDS_ALL, write=True):
        if index == LEDS_ALL:
            for i in range(self.nb_leds):
                self._set_color(r, g, b, i)
        else:
            self._set_color(r, g, b, index)
        if write:
            self._np.write()
