from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class Title(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel(
            "Admonitio.",
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )
        font = self.label.font()
        font.setPointSize(18)
        self.label.setFont(font)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

        self.setLayout(layout)
