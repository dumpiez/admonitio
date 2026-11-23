from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget


class Events(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint
        )
