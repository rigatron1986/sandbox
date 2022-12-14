import sys
from qtpy import QtGui, QtWidgets, QtCore
# from core.pipeline_data import PipeData
import json
from validationUI import Ui_Form


class Validation(QtWidgets.QMainWindow, Ui_Form):

    def __init__(self, parent=None):
        super(Validation, self).__init__(parent=parent)
        self.setupUi(self)
        self.setMinimumSize(0, 0)
        self.setMaximumSize(376, 681)
        # ui_file = os.path.join(os.path.dirname(__file__), 'bundle.ui')
        # uic.loadUi(ui_file, self)


def main(argv):
    app = QtWidgets.QApplication(argv)

    window = Validation()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
