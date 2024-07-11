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
    QWidget,
)

class pyplottergui(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle('pprz-py-plotter')
        self.setGeometry(600, 600, 800, 400)

        # Crear la barra de menú
        menubar = self.menuBar()

        # Crear el menú "File"
        fileMenu = menubar.addMenu('File')

        # Crear una acción para "Exit" y añadirla al menú "File"
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        # Crear el menú "Edit"
        editMenu = menubar.addMenu('Edit')

        # Crear una acción para "Cut" y añadirla al menú "Edit"
        cutAction = QAction('Cut', self)
        cutAction.setShortcut('Ctrl+X')
        cutAction.setStatusTip('Cut selected text')
        editMenu.addAction(cutAction)

        # Crear una acción para "Copy" y añadirla al menú "Edit"
        copyAction = QAction('Copy', self)
        copyAction.setShortcut('Ctrl+C')
        copyAction.setStatusTip('Copy selected text')
        editMenu.addAction(copyAction)

        # Crear una acción para "Paste" y añadirla al menú "Edit"
        pasteAction = QAction('Paste', self)
        pasteAction.setShortcut('Ctrl+V')
        pasteAction.setStatusTip('Paste from clipboard')
        editMenu.addAction(pasteAction)

        # Crear el menú "Help"
        helpMenu = menubar.addMenu('Help')

        # Crear una acción para "About" y añadirla al menú "Help"
        aboutAction = QAction('About', self)
        aboutAction.setStatusTip('Show application info')
        aboutAction.triggered.connect(self.open_about_url)
        helpMenu.addAction(aboutAction)

        # Creación de un botón
        btn = QPushButton('Haz clic aquí', self)
        btn.move(150, 80)
        btn.clicked.connect(self.show_message)

        self.show()

    def open_about_url(self):
        # Abrir una URL cuando se hace clic en "About"
        webbrowser.open('https://github.com/Pelochus/pprz-py-plotter')

    def show_message(self):
        # Mostrar un mensaje cuando se hace clic en el botón
        QMessageBox.information(self, 'Mensaje', '¡Hola, mundo!')