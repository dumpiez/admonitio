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

        self.title = Title()
        self.configuration = Configuration()
        self.switch = Switch()
        # ---------------------------- #
        layout.addWidget(self.title)
        layout.addWidget(self.configuration)
        layout.addStretch()
        layout.addWidget(self.switch)
        # ---------------------------- #

        self.setLayout(layout)
