from ultralytics import YOLO
from PyQt5 import QtWidgets, QtCore
from image_viewer import ImageViewer
import sys

# 主視窗
class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('黑潮Photo-ID')
        self.setGeometry(100, 100, 300, 150)

        self.folder_label = QtWidgets.QLabel('選擇資料夾:')
        self.folder_edit = QtWidgets.QLineEdit()
        self.folder_button = QtWidgets.QPushButton('瀏覽')
        self.folder_button.clicked.connect(self.openFolder)

        self.run_button = QtWidgets.QPushButton('執行YOLO')
        self.run_button.clicked.connect(self.runYOLO)

        # self.status_label = QtWidgets.QLabel(self)
        # self.status_label.setAlignment(QtCore.Qt.AlignCenter)

        self.image_button = QtWidgets.QPushButton('查看照片')
        self.image_button.clicked.connect(self.runViewer)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.folder_label)
        folder_layout = QtWidgets.QHBoxLayout()
        folder_layout.addWidget(self.folder_edit)
        folder_layout.addWidget(self.folder_button)
        layout.addLayout(folder_layout)
        layout.addWidget(self.image_button)
        layout.addWidget(self.run_button)
        # layout.addWidget(self.status_label)
        self.setLayout(layout)

    def openFolder(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, "選擇資料夾")
        if folder_path:
            self.folder_edit.setText(folder_path)
            # self.status_label.setText("Not executed yet")

    # YOLO
    def runYOLO(self):
        folder_path = self.folder_edit.text()
        if folder_path:
            model = YOLO("YOLO/best.pt")
            model.predict(source=folder_path, mode="predict", project="temp", name='predict', save=True, imgsz=(512, 512), conf=0.51, device="cpu", save_crop=True)
            # self.status_label.setText("Finished")
            self.viewer = ImageViewer()
            folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, "選擇資料夾")
            self.viewer.loadImagePaths(folder_path)
            self.viewer.show()

    def runViewer(self):
        folder_path = self.folder_edit.text()
        if folder_path:
            self.viewer = ImageViewer()
            self.viewer.loadImagePaths(folder_path)
            self.viewer.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())