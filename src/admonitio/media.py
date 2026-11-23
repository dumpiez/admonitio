from pathlib import Path

from PySide6.QtGui import QMovie, Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class Media(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint
        )

        self.ASSETS_DIR = Path(__file__).resolve().parents[2] / "assets"
        self.GIF_PATH = self.ASSETS_DIR / "jumpscare_single.gif"

        self.label = QLabel()
        self.movie = QMovie(str(self.GIF_PATH))
        self.label.setMovie(self.movie)
        self.label.setScaledContents(True)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.label)

    def play(self):
        self.showFullScreen()
        self.movie.start()
