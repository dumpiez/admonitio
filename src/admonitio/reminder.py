# from PySide6.QtCore import QUrl
# from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
# from PySide6.QtMultimediaWidgets import QVideoWidget
# from PySide6.QtGui import QMovie


import random

from PySide6.QtCore import QObject, QTimer

from admonitio.widgets.configuration import Configuration
from admonitio.widgets.switch import Switch


class Reminder(QObject):
    def trigger(self, switch: Switch, configuration: Configuration):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timeout)
        self.timer.setSingleShot(True)

        is_fixed = configuration.intervals.button.currentIndex() == 1

        if is_fixed:
            self.timer.setSingleShot(False)
            # self.minutes = configuration.intervals.interval.value() * 60000
            self.minutes = configuration.intervals.interval.value() * 1000
            self.timer.start(self.minutes)
        else:
            self.timer.start(random.randint(1000, 3_600_000))

    def stop(self):
        self.timer.stop()

    def timeout(self):
        print("test")
