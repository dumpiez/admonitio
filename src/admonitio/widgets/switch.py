from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QHBoxLayout, QPushButton, QWidget


class Switch(QWidget):
    def __init__(self):
        super().__init__()

        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.stop_button.setDisabled(True)

        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)

        self.start_button.clicked.connect(self.disable_button)
        self.stop_button.clicked.connect(self.disable_button)

    @Slot()
    def disable_button(self):
        self.start_button.setDisabled(self.start_button.isEnabled())
        self.stop_button.setDisabled(self.stop_button.isEnabled())
