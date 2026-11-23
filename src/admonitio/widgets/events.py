from PySide6.QtCore import Qt
from PySide6.QtWidgets import QComboBox, QLabel, QVBoxLayout, QWidget


class Events(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Event Type")

        self.button = QComboBox()
        self.button.addItems(["Audio", "Video", "Audio and Video"])

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
