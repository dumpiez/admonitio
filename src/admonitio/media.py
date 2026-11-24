import sys
from pathlib import Path

from PySide6.QtGui import QMovie, Qt
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from admonitio.widgets.events import Events


class Media(QWidget):
    def __init__(self, event: Events):
        super().__init__()

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.events = event
        self.event_type = self.events.button.currentIndex()

        # check whether its running pyinstaller or development
        if getattr(sys, "frozen", False):
            self.ASSETS_DIR = Path(sys._MEIPASS) / "assets"
        else:
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
        self.player.setSource(str(self.AUDIO_PATH))

        self.player.setAudioOutput(self.audio)

        self.events.button.currentIndexChanged.connect(self.update_event_type)
        self.movie.frameChanged.connect(self.finish_video_only)
        self.player.mediaStatusChanged.connect(self.finish_audio_and_video)

    def update_event_type(self):
        self.event_type = self.events.button.currentIndex()

    def play(self):
        # INDEX 0: AUDIO AND VIDEO
        # INDEX 1: VIDEO
        # INDEX 2: AUDIO

        if self.event_type == 0 or self.event_type == 1:
            self.showFullScreen()
            self.movie.start()
        if self.event_type == 0 or self.event_type == 2:
            self.player.play()

    def finish_audio_and_video(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.movie.stop()
            self.player.stop()
            self.hide()

    def finish_video_only(self, frame):
        if self.event_type == 1 and frame == self.movie.frameCount() - 1:
            self.movie.stop()
            self.hide()
