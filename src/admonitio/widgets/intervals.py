from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QComboBox, QSpinBox, QVBoxLayout, QWidget


class Intervals(QWidget):
    def __init__(self):
        super().__init__()

        self.button = QComboBox()
        self.button.addItems(["Fixed Interval", "Random Interval"])

        self.interval = QSpinBox()

        layout = QVBoxLayout(self)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.interval, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        self.button.currentTextChanged.connect(self.fixed)

    @Slot()
    def fixed(self):
        self.interval.setVisible(self.button.currentIndex() == 0)
