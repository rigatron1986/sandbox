class Sphere(object):
    COLORS = ('red', 'green', 'blue')

    def __init__(self, name='sphere', color='red'):
        self.name = name
        self.color = color

    def set_color(self, color):
        if color in self.COLORS:
            self.color = color

    @property
    def get_color(self):
        return self.color

    def set_name(self, name):
        if name:
            self.name = name


cc = Sphere(name='ball')
cc.set_color('green')

print(cc.get_color)


def set_trans(x=None, y=None, z=None):
    for name in ('x', 'y', 'z'):
        # print(locals())
        val = locals()[name]
        print(val)
        # if val is not None:
        #     print(val)
        #     print(name)


set_trans(x=15)
