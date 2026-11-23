from pathlib import Path

from PySide6.QtGui import QMovie, Qt
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class Media(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint
        )

        self.ASSETS_DIR = Path(__file__).resolve().parents[2] / "assets"
        self.GIF_PATH = self.ASSETS_DIR / "jumpscare_single.gif"

        # VIDEO STUFFS
        self.label = QLabel()
        self.movie = QMovie(str(self.GIF_PATH))
        self.label.setMovie(self.movie)
        self.label.setScaledContents(True)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.label)

        # AUDIO STUFFS
        self.player = QMediaPlayer(self)
        self.audio = QAudioOutput(self)
        self.AUDIO_PATH = self.ASSETS_DIR / "jumpscare.mp3"

        self.player.setAudioOutput(self.audio)
        self.player.setSource(str(self.AUDIO_PATH))

        self.player.mediaStatusChanged.connect(self.finished_check)

    def play(self):
        self.showFullScreen()
        self.movie.start()
        self.player.play()

    def finished_check(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.movie.stop()
            self.player.stop()
            self.hide()
