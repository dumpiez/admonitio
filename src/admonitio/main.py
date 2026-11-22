import sys

from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Admonitio")
window.resize(400, 400)
window.show()

layout = QVBoxLayout(window)
label = QLabel("hello world")
layout.addWidget(label)


sys.exit(app.exec())
