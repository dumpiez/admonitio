from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QWidget

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
        # ---------------------------- #
        layout.addWidget(Title())
        layout.addWidget(Configuration())
        layout.addStretch()
        layout.addWidget(Switch())
        # ---------------------------- #

        self.setLayout(layout)
