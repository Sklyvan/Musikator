from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLineEdit, QMessageBox
from app.main import main
import sys

ERROR_MESSAGE_TITLE = "Error"
ERROR_MESSAGE = "Avisa a la PEDAZO de puta de Sklyvan que algo ha ido mal"

SUCCESS_MESSAGE_TITLE = "LEKKER!"
SUCCESS_MESSAGE = "La Dahyun es una CERDA"

class ConverterUI(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(350, 150)

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

        self.setLayout(self.layout)

    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.inputPath.setText(folder)

    def convert_files(self):
        path = self.inputPath.text()
        if not path:
            QMessageBox.warning(self, ERROR_MESSAGE_TITLE, ERROR_MESSAGE)
            return
        try:
            main(path)
            QMessageBox.information(self, SUCCESS_MESSAGE_TITLE, SUCCESS_MESSAGE)
        except Exception as e:
            QMessageBox.critical(self, ERROR_MESSAGE_TITLE, str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterUI()
    window.show()
    sys.exit(app.exec_())
