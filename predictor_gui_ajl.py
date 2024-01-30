
# Python Package Imports
import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from PyQt5 import QtWidgets
from prophet import Prophet

# App Imports
from predictor_gui_pyqt_output import Ui_MainWindow

class MatplotlibWidget(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig, self.axes = plt.subplots(figsize=(width, height), dpi=dpi)
        plt.rcParams.update({'font.weight': 'normal', 'font.size': 16}) # set font size and weight on the plot
        FigureCanvasQTAgg.__init__(self, self.fig)
        self.setParent(parent)

    def plot(self, x, y):
        self.axes.clear()
        self.axes.plot(x, y)
        self.axes.set_title('Plot of y vs. x', fontweight='bold')
        self.axes.set_xlabel('x', fontweight='bold')
        self.axes.set_ylabel('y', fontweight='bold')
        self.draw()

    def save_bool(self, savefile='')->bool:
        if savefile:
            self.fig.savefig(savefile+'.pdf', format='pdf')
            return True
        else:
            return False

class Predictor_UI_MainWindow(Ui_MainWindow):

    def __init__(self, main_wind):

        # call setupUi method from the pyuic autocode
        # the autocode didn't define a constructor (__init__) method
        # so setupUi has to be called manually
        self.setupUi(MainWindow=main_wind)

        # define instance of the matplotlib Canvas widget
        self.mpl_widge = MatplotlibWidget(width=5, height=4, dpi=45)
        self.mpl_widge.plot([0, 1], [0, 0])

        # add the matplotlib widget to the main window
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.mpl_widge)
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.verticalLayout_4.addWidget(widget)

        # connect signals & slots on initialization
        self.sig_slot_connects()

    def sig_slot_connects(self):
        self.ButtonPredict.clicked.connect(self.predict_button_click)
        self.pushButtonInputFile.clicked.connect(self.input_file_click)

    def predict_button_click(self):

        # read csv with data
        data = self.get_data_from_file()
        #future_data = self.train_prophet_model(data)
        #print(f'data returned from prophet model:{future_data}')
        #print(f'type of prophet model data:{type(future_data)}')
        #future_data.to_csv('prophetmodelresults.csv')


        save_choice = self.checkSavePlotToFile.isChecked()
        s_file = self.linePlotFile.text()

        self.mpl_widge.plot(data['x'], data['y'])
        if save_choice:
            save_success = self.mpl_widge.save_bool(savefile=s_file)
            if not save_success:
                self.textBrowserOutput.append(f'No Plot Output File Name Provided.\nTry again.')

    def get_data_from_file(self)->pd.DataFrame:
        f_name = self.lineInputDataFile.text()

        try:
            data = pd.read_csv(f_name)
            return data
        except FileNotFoundError:
            self.textBrowserOutput.append(f'file {f_name} not found in the current directory.\nTry again.')
            return pd.DataFrame({'x': [0, 0], 'y': [0, 0]})

    def input_file_click(self):

        # open file dialog box, so user can select input file
        fname = QtWidgets.QFileDialog.getOpenFileName(caption='Open File', directory='',
                                                      filter='CSV Files (*.csv)')

        if fname:
            self.lineInputDataFile.setText(fname[0])

    @staticmethod
    def train_prophet_model(data)->pd.DataFrame:
        m = Prophet()
        m.fit(data)
        future = m.make_future_dataframe(periods=365)
        forecast = m.predict(future)
        return forecast

# drive application
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Predictor_UI_MainWindow(main_wind=MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())