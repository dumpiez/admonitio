from random import randint

from PySide6.QtCore import QObject, QTimer

from admonitio.media import Media
from admonitio.widgets.configuration import Configuration
from admonitio.widgets.switch import Switch


class Reminder(QObject):
    def __init__(self, switch: Switch, configuration: Configuration):
        super().__init__()

        self.configuration = configuration
        self.switch = switch
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.remind)
        self.event_type = self.configuration.events.button.currentIndex()
        self.media = Media(self.configuration.events)

    def trigger(self):
        is_fixed = self.configuration.intervals.button.currentIndex() == 1

        if is_fixed:
            self.timer.setSingleShot(False)

            # FIXED INTERVAL CONFIGURATION

            # default interval - turns interval into minutes
            # self.interval = self.configuration.intervals.interval.value() * 60000

            # for debugging purposes - turns interval into seconds
            self.interval = self.configuration.intervals.interval.value() * 1000
        else:
            self.timer.setSingleShot(True)

            # RANDOM INTERVAL CONFIGURATION

            # default interval - range is 1 second to 1 hour
            # self.interval = randint(1000, 3_600_000)

            # for debugging purposes - range is 1 to 10 seconds
            self.interval = randint(1000, 10000)

        self.timer.start(self.interval)

    def end(self):
        self.timer.stop()

    def remind(self):
        # print("Time Elapsed: ", self.interval)
        self.media.play()

        # if interval mode is set to random, then generate
        # new interval
        if not self.configuration.intervals.button.currentIndex():
            self.trigger()
