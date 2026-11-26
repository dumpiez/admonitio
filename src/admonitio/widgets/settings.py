from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (
    QCheckBox,
    QFileDialog,
    QHBoxLayout,
    QPushButton,
    QWidget,
)


class Settings(QWidget):
    def __init__(self):
        super().__init__()

        self.gif_path = None
        self.audio_path = None

        self.tray_toggle = QCheckBox("Minimize to system tray")
        self.tray_toggle.setChecked(True)

        self.gif_picker = QPushButton("Change GIF")
        self.audio_picker = QPushButton("Change Audio")

        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.tray_toggle)
        layout.addWidget(self.gif_picker)
        layout.addWidget(self.audio_picker)

        self.gif_picker.clicked.connect(self.open_gif_picker)
        self.audio_picker.clicked.connect(self.open_audio_picker)

    @Slot()
    def open_gif_picker(self):
        self.gif_path, _ = QFileDialog.getOpenFileName(
            self, "Select a GIF file", "", "GIF (*.gif)"
        )

        if self.gif_path:
            print(f"{self.gif_path}")

    @Slot()
    def open_audio_picker(self):
        self.audio_path, _ = QFileDialog.getOpenFileName(
            self, "Select an Audio File", "", "Audio (*.mp3 *.m4a *.aac *.ogg *.wav)"
        )

        if self.audio_path:
            print(f"{self.audio_path}")
