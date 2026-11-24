import sys

from PySide6.QtWidgets import QApplication

from admonitio.window import MainWindow

app = QApplication(sys.argv)

app.setQuitOnLastWindowClosed(False)
window = MainWindow()
window.show()

sys.exit(app.exec())
