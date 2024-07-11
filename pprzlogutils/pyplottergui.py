"""
pprzlogutils - A Python library for parsing and processing Paparazzi UAV log files.

pyplottergui provides the GUI for the application based in Qt5.

Author: Pelochus
"""

import webbrowser

# TODO: Remove unnecesary ones
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QStatusBar,
    QToolBar,
    QVBoxLayout,
    QWidget,
)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)
        
        self.plot_example()

    def plot_example(self):
        # Ejemplo de un gráfico simple
        x = [0, 1, 2, 3, 4]
        y = [0, 1, 4, 9, 16]
        self.axes.plot(x, y)
        self.draw()

class pyplottergui(QMainWindow):
    def __init__(self):
        super().__init__()

        # Main window config
        self.setWindowTitle('pprz-py-plotter')
        self.setGeometry(600, 600, 800, 400)
        menubar = self.menuBar()

        # File menu
        fileMenu = menubar.addMenu('File')
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        # Messages select menu. Select a message ad its variables
        # TODO: Implement this, probably better on a function outside, this will be long
        # Sort alphabetically, this will be big
        # More ideas: Use checkboxes per variable
        editMenu = menubar.addMenu('Messages')
        cutAction = QAction('Cut', self)
        cutAction.setShortcut('Ctrl+X')
        cutAction.setStatusTip('Cut selected text')
        editMenu.addAction(cutAction)

        # Help menu
        helpMenu = menubar.addMenu('Help')
        aboutAction = QAction('About (GitHub repo)', self)
        aboutAction.setStatusTip('Show application GitHub repo')
        aboutAction.triggered.connect(self.open_about_url)
        helpMenu.addAction(aboutAction)

        # Show matplotlib canvas in the center of the window
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        layout.addWidget(self.canvas)

        self.show()

    def open_about_url(self):
        webbrowser.open('https://github.com/Pelochus/pprz-py-plotter')