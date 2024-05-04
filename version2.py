from ultralytics import YOLO
from PyQt5 import QtWidgets, QtCore, QtGui
from image_viewer import ImageViewer
import sys

class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('黑潮Photo-ID')
        self.resize(1197, 822)

        #主圖片
        self.main_image = QtWidgets.QGraphicsView(self)
        self.main_image.setGeometry(QtCore.QRect(90, 50, 361, 301)) #窗口大小
        self.main_scene = QtWidgets.QGraphicsScene()
        self.main_scene.setSceneRect(0, 0, 500, 500) #內容物大小
        #這邊要修改成吃圖片List的方式顯示多張
        self.img = QtGui.QPixmap('411021230.png')
        #後面來研究好像蠻有趣的
        self.img = self.img.scaled(500, 500, aspectRatioMode = QtCore.Qt.KeepAspectRatio)
        self.main_scene.addPixmap(self.img)                   
        self.main_image.setScene(self.main_scene)

        #主操作鍵(先隨便拉後面慢慢修)
        self.folder_label = QtWidgets.QLabel('選擇資料夾:',self)
        self.folder_edit = QtWidgets.QLineEdit(self)
        self.folder_button = QtWidgets.QPushButton('瀏覽',self)
        self.folder_button.clicked.connect(self.openFolder)
        self.folder_label.setGeometry(QtCore.QRect(100, 440, 321, 28))
        self.folder_edit.setGeometry(QtCore.QRect(100, 490, 221, 28))
        self.folder_button.setGeometry(QtCore.QRect(330, 490, 91, 28))    

        self.run_button = QtWidgets.QPushButton('執行YOLO',self)
        self.run_button.setGeometry(QtCore.QRect(100, 540, 321, 28))
        #self.run_button.clicked.connect(self.openFolder)

        self.main_random_btn = QtWidgets.QPushButton('換一張',self)
        self.main_random_btn.setGeometry(QtCore.QRect(470, 240, 111, 31))
        #self.main_random_btn.clicked.connect(self.openFolder)
        self.main_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.main_viewer_btn.setGeometry(QtCore.QRect(470, 300, 111, 31))
        #self.main_viewer_btn.clicked.connect(self.openFolder)

        #top 10照片
        #top1
        self.top1_image =  QtWidgets.QGraphicsView(self)
        self.top1_image.setGeometry(QtCore.QRect(630, 20, 151, 121))
        self.top1_scene = QtWidgets.QGraphicsScene()
        self.top1_scene.setSceneRect(0, 0, 151, 121)
        self.top1img = QtGui.QPixmap('411021230.png')
        self.top1img = self.top1img.scaled(151, 121, aspectRatioMode = QtCore.Qt.KeepAspectRatio)
        self.top1_scene.addPixmap(self.top1img)                   
        self.top1_image.setScene(self.top1_scene)
        self.top1_random_btn = QtWidgets.QPushButton('換一張',self)
        self.top1_random_btn.setGeometry(QtCore.QRect(790, 70, 93, 28))
        #self.top1_random_btn.clicked.connect(self.openFolder)
        self.top1_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.top1_viewer_btn.setGeometry(QtCore.QRect(790, 110, 93, 28))
        #self.top1_viewer_btn.clicked.connect(self.openFolder)

        #top2
        self.top2_image =  QtWidgets.QGraphicsView(self)
        self.top2_image.setGeometry(QtCore.QRect(630, 200, 151, 121))
        self.top2_scene = QtWidgets.QGraphicsScene()
        self.top2_scene.setSceneRect(0, 0, 151, 121)
        self.top2img = QtGui.QPixmap('411021230.png')
        self.top2img = self.top1img.scaled(151, 121, aspectRatioMode = QtCore.Qt.KeepAspectRatio)
        self.top2_scene.addPixmap(self.top1img)                   
        self.top2_image.setScene(self.top1_scene)
        self.top2_random_btn = QtWidgets.QPushButton('換一張',self)
        self.top2_random_btn.setGeometry(QtCore.QRect(790, 250, 93, 28))
        #self.top2_random_btn.clicked.connect(self.openFolder)
        self.top2_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.top2_viewer_btn.setGeometry(QtCore.QRect(790, 290, 93, 28))
        #self.top2_viewer_btn.clicked.connect(self.openFolder)

        #top3
        self.top3_image =  QtWidgets.QGraphicsView(self)
        self.top3_image.setGeometry(QtCore.QRect(630, 360, 151, 121))
        self.top3_scene = QtWidgets.QGraphicsScene()
        self.top3_scene.setSceneRect(0, 0, 151, 121)
        self.top3img = QtGui.QPixmap('411021230.png')
        self.top3img = self.top1img.scaled(151, 121, aspectRatioMode = QtCore.Qt.KeepAspectRatio)
        self.top3_scene.addPixmap(self.top1img)                   
        self.top3_image.setScene(self.top1_scene)
        self.top3_random_btn = QtWidgets.QPushButton('換一張',self)
        self.top3_random_btn.setGeometry(QtCore.QRect(790, 410, 93, 28))
        #self.top3_random_btn.clicked.connect(self.openFolder)
        self.top3_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.top3_viewer_btn.setGeometry(QtCore.QRect(790, 450, 93, 28))
        #self.top3_viewer_btn.clicked.connect(self.openFolder)

        #top4
        self.top4_image =  QtWidgets.QGraphicsView(self)
        self.top4_image.setGeometry(QtCore.QRect(630, 510, 151, 121))
        self.top4_scene = QtWidgets.QGraphicsScene()
        self.top4_scene.setSceneRect(0, 0, 151, 121)
        self.top4img = QtGui.QPixmap('411021230.png')
        self.top4img = self.top1img.scaled(151, 121, aspectRatioMode = QtCore.Qt.KeepAspectRatio)
        self.top4_scene.addPixmap(self.top1img)                   
        self.top4_image.setScene(self.top1_scene)
        self.top4_random_btn = QtWidgets.QPushButton('換一張',self)
        self.top4_random_btn.setGeometry(QtCore.QRect(790, 560, 93, 28))
        #self.top4_random_btn.clicked.connect(self.openFolder)
        self.top4_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.top4_viewer_btn.setGeometry(QtCore.QRect(790, 600, 93, 28))
        #self.top4_viewer_btn.clicked.connect(self.openFolder)

        #top5
        self.top5_image =  QtWidgets.QGraphicsView(self)
        self.top5_image.setGeometry(QtCore.QRect(630, 670, 151, 121))
        self.top5_scene = QtWidgets.QGraphicsScene()
        self.top5_scene.setSceneRect(0, 0, 151, 121)
        self.top5img = QtGui.QPixmap('411021230.png')
        self.top5img = self.top1img.scaled(151, 121, aspectRatioMode = QtCore.Qt.KeepAspectRatio)
        self.top5_scene.addPixmap(self.top1img)                   
        self.top5_image.setScene(self.top1_scene)
        self.top5_random_btn = QtWidgets.QPushButton('換一張',self)
        self.top5_random_btn.setGeometry(QtCore.QRect(790, 720, 93, 28))
        #self.top5_random_btn.clicked.connect(self.openFolder)
        self.top5_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.top5_viewer_btn.setGeometry(QtCore.QRect(790, 760, 93, 28))
        #self.top5_viewer_btn.clicked.connect(self.openFolder)

        #top6
        self.top6_image =  QtWidgets.QGraphicsView(self)
        self.top6_image.setGeometry(QtCore.QRect(920, 20, 151, 121))
        self.top6_scene = QtWidgets.QGraphicsScene()
        self.top6_scene.setSceneRect(0, 0, 151, 121)
        self.top6img = QtGui.QPixmap('411021230.png')
        self.top6img = self.top1img.scaled(151, 121, aspectRatioMode = QtCore.Qt.KeepAspectRatio)
        self.top6_scene.addPixmap(self.top1img)                   
        self.top6_image.setScene(self.top1_scene)
        self.top6_random_btn = QtWidgets.QPushButton('換一張',self)
        self.top6_random_btn.setGeometry(QtCore.QRect(1080, 70, 93, 28))
        #self.top6_random_btn.clicked.connect(self.openFolder)
        self.top6_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.top6_viewer_btn.setGeometry(QtCore.QRect(1080, 110, 93, 28))
        #self.top6_viewer_btn.clicked.connect(self.openFolder)

        #top7
        self.top7_image =  QtWidgets.QGraphicsView(self)
        self.top7_image.setGeometry(QtCore.QRect(920, 200, 151, 121))
        self.top7_scene = QtWidgets.QGraphicsScene()
        self.top7_scene.setSceneRect(0, 0, 151, 121)
        self.top7img = QtGui.QPixmap('411021230.png')
        self.top7img = self.top1img.scaled(151, 121, aspectRatioMode = QtCore.Qt.KeepAspectRatio)
        self.top7_scene.addPixmap(self.top1img)                   
        self.top7_image.setScene(self.top1_scene)
        self.top7_random_btn = QtWidgets.QPushButton('換一張',self)
        self.top7_random_btn.setGeometry(QtCore.QRect(1080, 250, 93, 28))
        #self.top7_random_btn.clicked.connect(self.openFolder)
        self.top7_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.top7_viewer_btn.setGeometry(QtCore.QRect(1080, 290, 93, 28))
        #self.top7_viewer_btn.clicked.connect(self.openFolder)

        #top8
        self.top8_image =  QtWidgets.QGraphicsView(self)
        self.top8_image.setGeometry(QtCore.QRect(920, 360, 151, 121))
        self.top8_scene = QtWidgets.QGraphicsScene()
        self.top8_scene.setSceneRect(0, 0, 151, 121)
        self.top8img = QtGui.QPixmap('411021230.png')
        self.top8img = self.top1img.scaled(151, 121, aspectRatioMode = QtCore.Qt.KeepAspectRatio)
        self.top8_scene.addPixmap(self.top1img)                   
        self.top8_image.setScene(self.top1_scene)
        self.top8_random_btn = QtWidgets.QPushButton('換一張',self)
        self.top8_random_btn.setGeometry(QtCore.QRect(1080, 410, 93, 28))
        #self.top8_random_btn.clicked.connect(self.openFolder)
        self.top8_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.top8_viewer_btn.setGeometry(QtCore.QRect(1080, 450, 93, 28))
        #self.top8_viewer_btn.clicked.connect(self.openFolder)

        #top9
        self.top9_image =  QtWidgets.QGraphicsView(self)
        self.top9_image.setGeometry(QtCore.QRect(920, 510, 151, 121))
        self.top9_scene = QtWidgets.QGraphicsScene()
        self.top9_scene.setSceneRect(0, 0, 151, 121)
        self.top9img = QtGui.QPixmap('411021230.png')
        self.top9img = self.top1img.scaled(151, 121, aspectRatioMode = QtCore.Qt.KeepAspectRatio)
        self.top9_scene.addPixmap(self.top1img)                   
        self.top9_image.setScene(self.top1_scene)
        self.top9_random_btn = QtWidgets.QPushButton('換一張',self)
        self.top9_random_btn.setGeometry(QtCore.QRect(1080, 560, 93, 28))
        #self.top9_random_btn.clicked.connect(self.openFolder)
        self.top9_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.top9_viewer_btn.setGeometry(QtCore.QRect(1080, 600, 93, 28))
        #self.top9_viewer_btn.clicked.connect(self.openFolder)

        #top10
        self.top10_image =  QtWidgets.QGraphicsView(self)
        self.top10_image.setGeometry(QtCore.QRect(920, 670, 151, 121))
        self.top10_scene = QtWidgets.QGraphicsScene()
        self.top10_scene.setSceneRect(0, 0, 151, 121)
        self.top10img = QtGui.QPixmap('411021230.png')
        # self.top10img = self.top1img.scaled(151, 121, aspectRatioMode = QtCore.Qt.KeepAspectRatio)
        self.top10_scene.addPixmap(self.top1img)                   
        self.top10_image.setScene(self.top1_scene)
        self.top10_random_btn = QtWidgets.QPushButton('換一張',self)
        self.top10_random_btn.setGeometry(QtCore.QRect(1080, 720, 93, 28))
        #self.top10_random_btn.clicked.connect(self.openFolder)
        self.top10_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.top10_viewer_btn.setGeometry(QtCore.QRect(1080, 760, 93, 28))
        #self.top10_viewer_btn.clicked.connect(self.openFolder)


    def openFolder(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, "選擇資料夾")
        if folder_path:
            self.folder_edit.setText(folder_path)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())