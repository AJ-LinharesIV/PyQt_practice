
# Python Package Imports
import sys
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from PyQt5 import QtWidgets
from prophet import Prophet
from datetime import date

# App Imports
from predictor_gui_pyqt_output import Ui_MainWindow

class MplWidget(FigureCanvasQTAgg):

    def __init__(self, figure, parent=None):
        FigureCanvasQTAgg.__init__(self, figure)
        self.setParent(parent)

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

        # connect signals & slots
        self.sig_slot_connects()

    def sig_slot_connects(self):
        self.ButtonPredict.clicked.connect(self.predict_button_click)
        self.pushButtonInputFile.clicked.connect(self.input_file_click)

    def predict_button_click(self):

        save_choice = self.checkSavePlotToFile.isChecked()
        s_file = self.linePlotFile.text()

        input_fname = self.lineInputDataFile.text()

        try:
            data = pd.read_csv(input_fname)
            self.train_prophet_model(data, save_plot=save_choice, s_file=s_file)
        except FileNotFoundError:
            self.textBrowserOutput.append(f'file {input_fname} not found in the current directory.\nTry again.')

    def input_file_click(self):

        # open file dialog box, so user can select input file
        fname = QtWidgets.QFileDialog.getOpenFileName(caption='Open File', directory='',
                                                      filter='CSV Files (*.csv)')

        if fname:
            self.lineInputDataFile.setText(fname[0])

    def train_prophet_model(self, data: pd.DataFrame, save_plot: bool, s_file: str):

        self.textBrowserOutput.append('Fitting Prophet regression model to data...\n')

        # instantiate a Prophet model
        m = Prophet()

        # regression fit the input data
        m.fit(data)

        # calculate the number of extra days to add to the future dataframe
        ld_ls = [int(i) for i in str(data['ds'].iloc[-1]).split(sep='-')]
        last_date = date(ld_ls[0], ld_ls[1], ld_ls[2])
        to_date = self.datePredictEnd.date().toPyDate()
        delta = to_date - last_date

        if delta.days > 0:
            future = m.make_future_dataframe(periods=delta.days)
        else:
            self.textBrowserOutput.append(f'date {self.datePredictEnd.date().toPyDate()} is before or '
                                   f'concurrent with last date in input dataset...\n'
                                   f'Arbitrarily setting end date 365 days after last date in'
                                   f'dataset.\nTry again if this isnt what you want.\n')
            future = m.make_future_dataframe(periods=365)

        # use Prophet predict method to forecast into the future
        self.textBrowserOutput.append('Forecasting future data...\n')
        forecast = m.predict(future)

        # get the predicted value for the specific date requested by user
        spec_date = str(self.datePredictSpec.date().toPyDate())
        if spec_date in forecast['ds'].values:
            fc = forecast.set_index('ds')
            spec_yhat = fc['yhat'].loc[spec_date]
            self.linePredValue.text(str(round(spec_yhat,3)))
        else:
            self.textBrowserOutput.append('Requested date doesnt appear in dataset...\nTry Again.\n')

        # delete placeholder graphicsView widge from verticalLayout4 in prep for Prophet plot
        self.graphicsView.close()
        self.verticalLayout_4.update()

        # create an instance of the MplWidget using the Prophet .plot() method as the figure
        mpl_widget = MplWidget(figure=m.plot(forecast, figsize=(4,5), include_legend=True))

        # add the matplotlib widget to the main window
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(mpl_widget)
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)

        self.verticalLayout_4.addWidget(widget)

        # save plot if reqd
        if save_plot:
            save_success = mpl_widget.save_bool(savefile=s_file)
            if not save_success:
                self.textBrowserOutput.append(f'No Plot Output File Name Provided.\nTry again.')

# drive application
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Predictor_UI_MainWindow(main_wind=MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())