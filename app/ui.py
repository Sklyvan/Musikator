from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog,
    QLineEdit, QMessageBox, QProgressBar
)
from PyQt5.QtCore import QThread, pyqtSignal
from app.main import main
import sys

ERROR_MESSAGE_TITLE = "Error"
ERROR_MESSAGE = "Avisa a la PEDAZO de puta de Sklyvan que algo ha ido mal"

SUCCESS_MESSAGE_TITLE = "LEKKER!"
SUCCESS_MESSAGE = "La Dahyun es una CERDA"

class Worker(QThread):
    progress = pyqtSignal(int, int)
    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, path):
        super().__init__()
        self.path = path

    def run(self):
        try:
            for i, n in main(self.path):
                self.progress.emit(i, n)
            self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))

class ConverterUI(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(350, 180)
        self.setWindowTitle("Audio to AIFF Converter")
        self.layout = QVBoxLayout()

        self.inputPath = QLineEdit()
        self.layout.addWidget(self.inputPath)

        self.browseBtn = QPushButton("Browse")
        self.browseBtn.clicked.connect(self.browse_folder)
        self.layout.addWidget(self.browseBtn)

        self.convertBtn = QPushButton("Convert")
        self.convertBtn.clicked.connect(self.convert_files)
        self.layout.addWidget(self.convertBtn)

        self.progressBar = QProgressBar()
        self.progressBar.setValue(0)
        self.layout.addWidget(self.progressBar)

        self.setLayout(self.layout)
        self.worker = None

    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.inputPath.setText(folder)

    def convert_files(self):
        path = self.inputPath.text()
        if not path:
            QMessageBox.warning(self, ERROR_MESSAGE_TITLE, ERROR_MESSAGE)
            return

        self.progressBar.setValue(0)
        self.convertBtn.setEnabled(False)
        self.worker = Worker(path)
        self.worker.progress.connect(self.update_progress)
        self.worker.finished.connect(self.conversion_finished)
        self.worker.error.connect(self.conversion_error)
        self.worker.start()

    def update_progress(self, i, n):
        self.progressBar.setMaximum(n)
        self.progressBar.setValue(i)

    def conversion_finished(self):
        self.convertBtn.setEnabled(True)
        QMessageBox.information(self, SUCCESS_MESSAGE_TITLE, SUCCESS_MESSAGE)

    def conversion_error(self, msg):
        self.convertBtn.setEnabled(True)
        QMessageBox.critical(self, ERROR_MESSAGE_TITLE, msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterUI()
    window.show()
    sys.exit(app.exec_())
