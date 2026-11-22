from PySide6.QtWidgets import QVBoxLayout, QWidget

from admonitio.widgets.events import Events
from admonitio.widgets.intervals import Intervals
from admonitio.widgets.title import Title


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Admonitio")
        self.resize(400, 400)

        layout = QVBoxLayout()
        layout.addWidget(Title())
        layout.addWidget(Intervals())
        layout.addWidget(Events())
        layout.addStretch()

        self.setLayout(layout)
