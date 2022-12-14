# from PyQt4 import QtGui, QtCore, uic


class Runner(object):
    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b

    def addition(self):
        result = self.value_a + self.value_b
        return result

    def subraction(self):
        result = self.value_a - self.value_b
        return result


class FileManger(object):
    def __init__(self):
        pass

    def run(self, a, b):
        val_a = a
        val_b = b
        com = Runner(val_a, val_b)
        res = com.addition()
        return res


res = FileManger()
print(res.run(4, 8))
print(res)
val = Runner(13, 4)
print(val.addition())
print(val.subraction())
