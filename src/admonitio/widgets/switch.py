from PySide6.QtCore import Qt, QTimer, Slot
from PySide6.QtWidgets import QHBoxLayout, QPushButton, QWidget

from admonitio.reminder import Reminder


class Switch(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)

        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.stop_button.setDisabled(True)

        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)

    @Slot()
    def stop(self):
        self.start_button.setDisabled(self.start_button.isEnabled())
        self.stop_button.setDisabled(self.stop_button.isEnabled())

        self.timer.stop()

    @Slot()
    def start(self):
        self.start_button.setDisabled(self.start_button.isEnabled())
        self.stop_button.setDisabled(self.stop_button.isEnabled())
        self.reminder = Reminder()

        self.timer.timeout.connect(self.reminder.trigger)
        self.timer.start(2000)
