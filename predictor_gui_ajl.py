
# Python Package Imports
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from PyQt5 import QtWidgets
import numpy as np

# App Imports
from predictor_gui_pyqt_output import Ui_MainWindow

class MatplotlibWidget(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig, self.axes = plt.subplots(figsize=(width, height), dpi=dpi)
        plt.rcParams.update({'font.weight': 'normal', 'font.size': 16}) # set font size and weight on the plot
        FigureCanvasQTAgg.__init__(self, fig)
        self.setParent(parent)

    def plot(self, x, y):
        self.axes.clear()
        self.axes.plot(x, y)
        self.axes.set_title('Plot of y vs. x', fontweight='bold')
        self.axes.set_xlabel('x', fontweight='bold')
        self.axes.set_ylabel('y', fontweight='bold')
        self.draw()

class Predictor_UI_MainWindow(Ui_MainWindow):

    def __init__(self, main_wind):
        self.setupUi(MainWindow=main_wind)
        self.mpl_widge = MatplotlibWidget(width=5, height=4, dpi=45)
        self.mpl_widge.plot([0, 1], [0, 0])

        # create toolbar, passing canvas as first param
        #toolbar = NavigationToolbar2QT(sc, self)


        layout = QtWidgets.QVBoxLayout()
        #layout.addWidget(toolbar)
        layout.addWidget(self.mpl_widge)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.verticalLayout_4.addWidget(widget)

        # connect signals & slots on initialization
        self.sig_slot_connects()

    def sig_slot_connects(self):
        self.ButtonPredict.clicked.connect(self.predict_button_click)

    def predict_button_click(self):
        x_data = np.linspace(0, 10, 100)
        y_data = np.sin(x_data)
        self.mpl_widge.plot(x_data,y_data)

# drive application
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Predictor_UI_MainWindow(main_wind=MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())