from PySide6.QtCore import Qt, QTimer, Slot
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMenu, QSystemTrayIcon, QVBoxLayout, QWidget

from admonitio.reminder import Reminder
from admonitio.widgets.configuration import Configuration
from admonitio.widgets.settings import Settings
from admonitio.widgets.switch import Switch
from admonitio.widgets.title import Title


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Admonitio")
        self.resize(600, 300)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.menu = QMenu()
        self.title = Title()
        self.configuration = Configuration()
        self.switch = Switch()
        self.settings = Settings()
        self.reminder = Reminder(self.switch, self.configuration, self.settings)
        self.timer = QTimer(self)
        self.tray = QSystemTrayIcon(self)

        # -------- TRAY SETTINGS ------ #
        open_app = QAction("Open Admonitio", self)
        open_app.triggered.connect(self.show)

        quit_app = QAction("Quit", self)
        quit_app.triggered.connect(QApplication.quit)

        self.menu.addAction(open_app)
        self.menu.addSeparator()
        self.menu.addAction(quit_app)

        self.tray.setContextMenu(self.menu)
        self.tray.setToolTip("Admonitio")
        self.tray.setVisible(self.settings.tray_toggle.isChecked())
        # ---------------------------- #

        # -------- APP LAYOUT -------- #
        layout.addWidget(self.title)
        layout.addWidget(self.configuration)
        layout.addStretch()
        layout.addWidget(self.settings)
        layout.addWidget(self.switch)
        # ---------------------------- #

        self.setLayout(layout)

        self.switch.start_button.clicked.connect(self.startEvent)
        self.switch.stop_button.clicked.connect(self.stopEvent)
        self.settings.tray_toggle.checkStateChanged.connect(
            self.toggle_disappear_into_tray
        )

    def closeEvent(self, event):
        if self.settings.tray_toggle.isChecked():
            event.ignore()
            self.hide()
        else:
            event.accept()
            QApplication.quit()

    @Slot()
    def startEvent(self):
        self.reminder.trigger()

    @Slot()
    def stopEvent(self):
        self.reminder.end()

    @Slot()
    def toggle_disappear_into_tray(self):
        if self.settings.tray_toggle.isChecked():
            self.tray.show()
        else:
            self.tray.hide()
