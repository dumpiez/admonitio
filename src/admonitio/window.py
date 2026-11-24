from PySide6.QtCore import Qt, QTimer, Slot
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMenu, QSystemTrayIcon, QVBoxLayout, QWidget

from admonitio.reminder import Reminder
from admonitio.widgets.configuration import Configuration
from admonitio.widgets.switch import Switch
from admonitio.widgets.title import Title


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Admonitio")
        self.resize(600, 300)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        menu = QMenu()

        self.title = Title()
        self.configuration = Configuration()
        self.switch = Switch()
        self.reminder = Reminder(self.switch, self.configuration)
        self.timer = QTimer(self)
        self.tray = QSystemTrayIcon(self)

        open_app = QAction("Open Admonitio", self)
        open_app.triggered.connect(self.show)

        quit_app = QAction("Quit", self)
        quit_app.triggered.connect(QApplication.quit)

        menu.addAction(open_app)
        menu.addSeparator()
        menu.addAction(quit_app)

        self.tray.setContextMenu(menu)
        self.tray.show()

        # ---------------------------- #
        layout.addWidget(self.title)
        layout.addWidget(self.configuration)
        layout.addStretch()
        layout.addWidget(self.switch)
        # ---------------------------- #

        self.setLayout(layout)

        self.switch.start_button.clicked.connect(self.startEvent)
        self.switch.stop_button.clicked.connect(self.stopEvent)

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    @Slot()
    def startEvent(self):
        self.reminder.trigger()

    @Slot()
    def stopEvent(self):
        self.reminder.end()
