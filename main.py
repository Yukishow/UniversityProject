from ultralytics import YOLO
from PyQt5 import QtWidgets, QtGui
from PIL import Image
import sys
import os

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowTitle('KURO SHIO PHOTO-ID')  # 設定標題
        self.resize(900, 960)
        self.ui()

    def ui(self):
        btn1 = QtWidgets.QPushButton(self)
        btn1.move(20, 20)
        btn1.setText('選擇圖片')
        btn1.clicked.connect(self.openfile)
        btn2 = QtWidgets.QPushButton(self)
        btn2.move(20, 50)
        btn2.setText('執行YOLO')
        btn2.clicked.connect(self.yolomodel)
        #右上圖
        self.grview1 = QtWidgets.QGraphicsView(self)
        self.grview1.setGeometry(400, 0, 500, 480)
        self.scene1 = QtWidgets.QGraphicsScene()
        self.scene1.setSceneRect(0, 0, 900, 480)
        self.grview1.setScene(self.scene1)
        #右下圖
        self.grview2 = QtWidgets.QGraphicsView(self)
        self.grview2.setGeometry(400, 480, 500, 480)
        self.scene2 = QtWidgets.QGraphicsScene()
        self.scene2.setSceneRect(0, 0, 900, 480)
        self.grview2.setScene(self.scene2)

    def openfile(self):
        global filePath
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName()
        if filePath:
            img = QtGui.QPixmap(filePath)
            img = img.scaled(900, 480)
            self.scene1.clear()
            self.scene1.addPixmap(img)
            self.grview1.setScene(self.scene1)
            # print(filePath)
    
    def yolomodel(self):
        self.model = YOLO("best.pt")
        result = self.model.predict(source=filePath,mode="predict",project="test",name="predict",save=True,imgsz=(512, 512),conf=0.51,device = "cpu")
        print(type(result))
        for filename in os.listdir('test\predict'):
            if filename.endswith(('.png', '.jpg', '.jpeg', '.JPG')):
                file = os.path.join('test\predict', filename)
                img = QtGui.QPixmap(file)
                # img = img.scaled(512, 512)
                self.scene2.clear()
                self.scene2.addPixmap(img)
                self.grview2.setScene(self.scene2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())
