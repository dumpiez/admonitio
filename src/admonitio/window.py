from PySide6.QtWidgets import QVBoxLayout, QWidget

from admonitio.widgets.helloworld import HelloWorldWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Remainder")
        self.resize(400, 300)

        layout = QVBoxLayout()
        layout.addWidget(HelloWorldWidget())

        self.setLayout(layout)
