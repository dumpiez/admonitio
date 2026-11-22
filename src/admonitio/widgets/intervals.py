from PySide6.QtCore import Qt
from PySide6.QtWidgets import QComboBox, QVBoxLayout, QWidget


class Intervals(QWidget):
    def __init__(self):
        super().__init__()

        self.button = QComboBox()
        self.button.addItems(["Fixed Interval", "Random Interval"])

        layout = QVBoxLayout(self)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)
