from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class Intervals(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Interval")

        self.button = QComboBox()
        self.button.addItems(["Random Interval", "Fixed Interval"])

        self.interval_label = QLabel("minutes")
        self.interval = QSpinBox()

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        spinbox_layout = QHBoxLayout()

        spinbox_layout.addStretch()
        spinbox_layout.addWidget(self.interval)
        spinbox_layout.addWidget(self.interval_label)
        spinbox_layout.addStretch()

        self.interval.hide()
        self.interval_label.hide()

        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(spinbox_layout)

        self.button.currentTextChanged.connect(self.fixed)

    @Slot()
    def fixed(self):
        self.interval_label.setVisible(self.button.currentIndex() == 1)
        self.interval.setVisible(self.button.currentIndex() == 1)
