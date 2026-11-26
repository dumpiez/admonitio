from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QWidget,
    QFileDialog,
)


class Settings(QWidget):
    def __init__(self):
        super().__init__()

        self.tray_switch = QCheckBox("Minimze to system tray")
        self.gif_picker = QPushButton("Change GIF")
        self.audio_picker = QPushButton("Change Audio")

        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.tray_switch)
        layout.addWidget(self.gif_picker)
        layout.addWidget(self.audio_picker)
