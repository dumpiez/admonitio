from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QComboBox, QLabel, QSpinBox, QVBoxLayout, QWidget


class Intervals(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Interval")

        self.button = QComboBox()
        self.button.addItems(["Random Interval", "Fixed Interval"])

        self.interval = QSpinBox()
        self.interval.hide()

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.interval, alignment=Qt.AlignmentFlag.AlignCenter)

        self.button.currentTextChanged.connect(self.fixed)

    @Slot()
    def fixed(self):
        self.interval.setVisible(self.button.currentIndex() == 1)
