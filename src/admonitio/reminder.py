# from PySide6.QtCore import QUrl
# from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
# from PySide6.QtMultimediaWidgets import QVideoWidget
# from PySide6.QtGui import QMovie


import random

from PySide6.QtCore import QObject, QTimer

from admonitio.widgets.configuration import Configuration
from admonitio.widgets.switch import Switch


class Reminder(QObject):
    def __init__(self, switch: Switch, configuration: Configuration):
        self.configuration = configuration
        self.switch = switch
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.remind)

    def trigger(self):
        is_fixed = self.configuration.intervals.button.currentIndex() == 1

        if is_fixed:
            # self.minutes = configuration.intervals.interval.value() * 60000
            self.interval = self.configuration.intervals.interval.value() * 1000
        else:
            self.interval = random.randint(1000, 3_600_600)

        self.timer.start(self.interval)

    def end(self):
        self.timer.stop()

    def remind(self):
        # if interval mode is set to random, then generate
        # new interval before running the event
        if not self.configuration.intervals.button.currentIndex():
            self.trigger()
