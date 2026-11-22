from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class HelloWorldWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.helloworld = QLabel("hello, world!")
        layout = QVBoxLayout(self)
        layout.addWidget(self.helloworld)

        self.setLayout(layout)
