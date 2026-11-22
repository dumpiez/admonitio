from PySide6.QtWidgets import QVBoxLayout, QWidget

from admonitio.widgets.configuration import Configuration
from admonitio.widgets.title import Title


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Admonitio")
        self.resize(400, 400)

        layout = QVBoxLayout()
        layout.addWidget(Title())
        layout.addWidget(Configuration())
        layout.addStretch()

        self.setLayout(layout)
