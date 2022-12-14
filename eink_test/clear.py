try:
    from waveshare_epd import epd2in13b_V3
except ImportError:
    pass


class Epd2in13bv3(object):

    def __init__(self, mode=None):
        super().__init__()
        self.epd = epd2in13b_V3.EPD()

        self.epd.init()

    def clean_screen(self):
        self.epd.Clear()


d = Epd2in13bv3()
d.clean_screen()
