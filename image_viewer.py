# 圖片顯示
from PyQt5 import QtWidgets, QtGui, QtCore
import os

class ImageViewer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.zoom_factor = 1.0
        self.setup_shortcuts()

    def initUI(self):
        self.setWindowTitle('Image Viewer')
        self.setGeometry(100, 100, 800, 600)

        self.image_label = QtWidgets.QLabel(self)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)

        self.index_label = QtWidgets.QLabel(self)
        self.index_label.setAlignment(QtCore.Qt.AlignCenter)

        self.saved_label = QtWidgets.QLabel(self)
        self.saved_label.setAlignment(QtCore.Qt.AlignCenter)

        self.pre_button = QtWidgets.QPushButton('Pre Image', self)
        self.pre_button.clicked.connect(self.preImage)

        self.next_button = QtWidgets.QPushButton('Next Image', self)
        self.next_button.clicked.connect(self.nextImage)

        self.save_button = QtWidgets.QPushButton('Save Image', self)
        self.save_button.clicked.connect(self.saveImage)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.index_label)
        layout.addWidget(self.saved_label)
        layout.addWidget(self.pre_button)
        layout.addWidget(self.next_button)
        layout.addWidget(self.save_button)
        self.setLayout(layout)

        self.image_paths = []
        self.current_index = 0
        self.image_saved = []

    def loadImagePaths(self, folder_path):
        # output_dir = os.path.join(folder_path, "temp", "predict")
        output_dir = folder_path
        self.image_paths = [os.path.join(output_dir, filename) for filename in os.listdir(output_dir) if filename.lower().endswith(('.jpg', '.png', '.jpeg'))]
        self.image_saved = [0]*len(self.image_paths)
        if self.image_paths:
            self.current_index = 0
            self.showImage()

    def preImage(self):
        if self.image_paths:
            self.current_index = (self.current_index - 1) % len(self.image_paths)
            #print(f"image_path: {self.image_paths[self.current_index]}")
            self.showImage()

    def nextImage(self):
        if self.image_paths:
            self.current_index = (self.current_index + 1) % len(self.image_paths)
            #print(f"image_path: {self.image_paths[self.current_index]}")
            self.showImage()

    def showImage(self):
        image_path = self.image_paths[self.current_index]
        pixmap = QtGui.QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(pixmap.size() * self.zoom_factor, QtCore.Qt.KeepAspectRatio)
        self.image_label.setPixmap(scaled_pixmap)
        self.index_label.setText(f"Image {self.current_index + 1}/{len(self.image_paths)}")
        if self.image_saved[self.current_index] == 1:
            self.saved_label.setText("Saved")
        else:
            self.saved_label.setText("Not Saved")

    # Ctrl++ 跟 Ctrl+-圖片放大縮小
    def setup_shortcuts(self):
        zoom_in_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtGui.QKeySequence.ZoomIn), self)
        zoom_in_shortcut.activated.connect(self.zoom_in)

        zoom_out_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtGui.QKeySequence.ZoomOut), self)
        zoom_out_shortcut.activated.connect(self.zoom_out)

    def zoom_in(self):
        self.zoom_factor *= 1.25
        self.showImage()

    def zoom_out(self):
        self.zoom_factor /= 1.25
        self.showImage()

    #可以使用滑鼠滾輪
    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.zoom_in()
        else:
            self.zoom_out()

    def saveImage(self):
        image_path = self.image_paths[self.current_index]
        folder_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Image",filter='IMAGE(*.jpg *.png *.JPG)')
        if folder_path:
            # print(f"folder_path = {folder_path}")
            pixmap = QtGui.QPixmap(image_path)
            if pixmap:
                pixmap.save(folder_path)
                self.image_saved[self.current_index] = 1
                self.showImage()

        # self.index_label.setText(f"Image {self.current_index + 1}/{len(self.image_paths)}")