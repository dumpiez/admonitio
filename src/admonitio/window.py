from PySide6.QtCore import QTimer, Qt, Slot
from PySide6.QtWidgets import QVBoxLayout, QWidget

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

        self.title = Title()
        self.configuration = Configuration()
        self.switch = Switch()
        self.reminder = Reminder()
        self.timer = QTimer(self)

        # ---------------------------- #
        layout.addWidget(self.title)
        layout.addWidget(self.configuration)
        layout.addStretch()
        layout.addWidget(self.switch)
        # ---------------------------- #

        self.setLayout(layout)

        self.switch.start_button.clicked.connect(self.startEvent)
        self.switch.stop_button.clicked.connect(self.stopEvent)

    @Slot()
    def startEvent(self):
        self.reminder.trigger(self.switch, self.configuration)

    @Slot()
    def stopEvent(self):
        self.reminder.stop()
