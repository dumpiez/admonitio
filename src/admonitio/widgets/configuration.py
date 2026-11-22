from PySide6.QtWidgets import QHBoxLayout, QWidget

from admonitio.widgets.events import Events
from admonitio.widgets.intervals import Intervals


class Configuration(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.addWidget(Intervals(), 1)
        layout.addWidget(Events(), 1)

        self.setLayout(layout)
