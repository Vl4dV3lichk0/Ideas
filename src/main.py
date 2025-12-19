from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ideas")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  
    app.exec()