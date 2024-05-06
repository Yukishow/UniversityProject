from PyQt5 import QtWidgets, QtCore, QtGui
from image_viewer import ImageViewer
from recognizer import Recognizer
# import function
import os
import random

# recognizer = Recognizer("xxoo.model")

class identifier(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('黑潮Photo-ID')
        self.resize(1197, 822)

        #主圖片
        self.main_image_path = []
        self.main_image_index = 0
        self.main_image = QtWidgets.QGraphicsView(self)
        self.main_image.setGeometry(QtCore.QRect(90, 50, 361, 301))
        self.main_scene = QtWidgets.QGraphicsScene()
        self.main_scene.setSceneRect(0, 0, 500, 500)

        #主操作鍵
        self.folder_label = QtWidgets.QLabel('選擇資料夾:',self)
        self.folder_edit = QtWidgets.QLineEdit(self)
        self.folder_button = QtWidgets.QPushButton('瀏覽',self)
        self.folder_button.clicked.connect(self.openFolder)
        self.run_button = QtWidgets.QPushButton('找top10',self)
        # self.run_button.clicked.connect()
        self.folder_label.setGeometry(QtCore.QRect(100, 440, 321, 28))
        self.folder_edit.setGeometry(QtCore.QRect(100, 490, 221, 28))
        self.folder_button.setGeometry(QtCore.QRect(330, 490, 91, 28))
        self.run_button.setGeometry(QtCore.QRect(100, 530, 321, 28))


        self.main_index = QtWidgets.QLabel(self)
        self.main_index.setAlignment(QtCore.Qt.AlignCenter)
        self.main_index.setGeometry(QtCore.QRect(470, 60, 111, 31))
        self.main_pre_btn = QtWidgets.QPushButton('上一張',self)
        self.main_pre_btn.setGeometry(QtCore.QRect(470, 120, 111, 31))
        self.main_pre_btn.clicked.connect(lambda: self.preImage())
        self.main_next_btn = QtWidgets.QPushButton('下一張',self)
        self.main_next_btn.setGeometry(QtCore.QRect(470, 180, 111, 31))
        self.main_next_btn.clicked.connect(lambda: self.nextImage())
        self.main_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.main_viewer_btn.setGeometry(QtCore.QRect(470, 240, 111, 31))
        self.main_viewer_btn.clicked.connect(lambda: self.runViewer())
        self.new_button = QtWidgets.QPushButton('新的',self)
        self.new_button.setGeometry(QtCore.QRect(470, 300, 111, 31))
        # self.new_button.clicked.connect()

        #top 10照片
        #top1
        # top1_output_dir = "D:\database_test\id_0003R"
        # self.top1_image_path = [os.path.join(top1_output_dir, filename) for filename in os.listdir(top1_output_dir) if filename.lower().endswith(('.jpg', '.png', '.jpeg', 'JPG'))]
        # self.top1_image_index = random.randint(0,len(self.top1_image_path)-1)self.top1_image_path[self.top1_image_index]

        self.top1_image =  QtWidgets.QGraphicsView(self)
        self.top1_image.setGeometry(QtCore.QRect(630, 20, 151, 121))
        self.top1_scene = QtWidgets.QGraphicsScene()
        self.top1_scene.setSceneRect(0, 0, 151, 121)
        self.top1_scene.clear()
        self.top1_image.setScene(self.top1_scene)
        self.top1label = QtWidgets.QLabel('top1', self)
        self.top1label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.top1label.setAlignment(QtCore.Qt.AlignCenter)
        self.top1label.setGeometry(QtCore.QRect(790, 20, 93, 28))
        self.top1_random_btn = QtWidgets.QPushButton('換一張',self)
        self.top1_random_btn.setGeometry(QtCore.QRect(790, 50, 93, 28))
        # self.top1_random_btn.clicked.connect(lambda: self.change_top_image(self.top1_image_path, self.top1_scene, self.top1_image))
        self.top1_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.top1_viewer_btn.setGeometry(QtCore.QRect(790, 80, 93, 28))
        # self.top1_viewer_btn.clicked.connect(lambda: self.runtop10Viewer(top1_output_dir))
        self.top1_save_btn = QtWidgets.QPushButton('儲存',self)
        self.top1_save_btn.setGeometry(QtCore.QRect(790, 110, 93, 28))
        # self.top1_save_btn.clicked.connect()


        #top2
        # output_dir = "D:\database_test\id_0001L"
        # self.top2_image_path = [os.path.join(output_dir, filename) for filename in os.listdir(output_dir) if filename.lower().endswith(('.jpg', '.png', '.jpeg', 'JPG'))]
        # self.top2_image_index = random.randint(0,len(self.top1_image_path)-1)


        self.top2_image =  QtWidgets.QGraphicsView(self)
        self.top2_image.setGeometry(QtCore.QRect(630, 200, 151, 121))
        self.top2_scene = QtWidgets.QGraphicsScene()
        self.top2_scene.setSceneRect(0, 0, 151, 121)
        self.top2_scene.clear()
        self.top2_image.setScene(self.top2_scene)
        self.top2label = QtWidgets.QLabel('top2', self)
        self.top2label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.top2label.setAlignment(QtCore.Qt.AlignCenter)
        self.top2label.setGeometry(QtCore.QRect(790, 200, 93, 28))
        self.top2_random_btn = QtWidgets.QPushButton('換一張',self)
        self.top2_random_btn.setGeometry(QtCore.QRect(790, 230, 93, 28))
        # self.top2_random_btn.clicked.connect(lambda: self.change_top_image(self.top2_image_path, self.top2_scene, self.top2_image))
        self.top2_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.top2_viewer_btn.setGeometry(QtCore.QRect(790, 260, 93, 28))
        #self.top2_viewer_btn.clicked.connect(self.openFolder)
        self.top2_save_btn = QtWidgets.QPushButton('儲存',self)
        self.top2_save_btn.setGeometry(QtCore.QRect(790, 290, 93, 28))
        # self.top2_save_btn.clicked.connect()

        #top3
        self.top3_image_path = []
        self.top3_image_index = 0
        self.top3_image =  QtWidgets.QGraphicsView(self)
        self.top3_image.setGeometry(QtCore.QRect(630, 360, 151, 121))
        self.top3_scene = QtWidgets.QGraphicsScene()
        self.top3_scene.setSceneRect(0, 0, 151, 121)
        self.top3_scene.clear()
        self.top3_image.setScene(self.top3_scene)
        self.top3label = QtWidgets.QLabel('top3', self)
        self.top3label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.top3label.setAlignment(QtCore.Qt.AlignCenter)
        self.top3label.setGeometry(QtCore.QRect(790, 360, 93, 28))
        self.top3_random_btn = QtWidgets.QPushButton('換一張',self)
        self.top3_random_btn.setGeometry(QtCore.QRect(790, 390, 93, 28))
        #self.top3_random_btn.clicked.connect(self.openFolder)
        self.top3_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.top3_viewer_btn.setGeometry(QtCore.QRect(790, 420, 93, 28))
        #self.top3_viewer_btn.clicked.connect(self.openFolder)
        self.top3_save_btn = QtWidgets.QPushButton('儲存',self)
        self.top3_save_btn.setGeometry(QtCore.QRect(790, 450, 93, 28))
        # self.top3_save_btn.clicked.connect()

        #top4
        self.top4_image_path = []
        self.top4_image_index = 0
        self.top4_image =  QtWidgets.QGraphicsView(self)
        self.top4_image.setGeometry(QtCore.QRect(630, 510, 151, 121))
        self.top4_scene = QtWidgets.QGraphicsScene()
        self.top4_scene.setSceneRect(0, 0, 151, 121)
        self.top4_scene.clear()
        self.top4_image.setScene(self.top4_scene)
        self.top4label = QtWidgets.QLabel('top4', self)
        self.top4label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.top4label.setAlignment(QtCore.Qt.AlignCenter)
        self.top4label.setGeometry(QtCore.QRect(790, 510, 93, 28))
        self.top4_random_btn = QtWidgets.QPushButton('換一張',self)
        self.top4_random_btn.setGeometry(QtCore.QRect(790, 540, 93, 28))
        #self.top4_random_btn.clicked.connect(self.openFolder)
        self.top4_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.top4_viewer_btn.setGeometry(QtCore.QRect(790, 570, 93, 28))
        #self.top4_viewer_btn.clicked.connect(self.openFolder)
        self.top4_save_btn = QtWidgets.QPushButton('儲存',self)
        self.top4_save_btn.setGeometry(QtCore.QRect(790, 600, 93, 28))
        # self.top4_save_btn.clicked.connect()

        #top5
        self.top5_image_path = []
        self.top5_image_index = 0
        self.top5_image =  QtWidgets.QGraphicsView(self)
        self.top5_image.setGeometry(QtCore.QRect(630, 670, 151, 121))
        self.top5_scene = QtWidgets.QGraphicsScene()
        self.top5_scene.setSceneRect(0, 0, 151, 121)
        self.top5_scene.clear()
        self.top5_image.setScene(self.top5_scene)
        self.top5label = QtWidgets.QLabel('top5', self)
        self.top5label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.top5label.setAlignment(QtCore.Qt.AlignCenter)
        self.top5label.setGeometry(QtCore.QRect(790, 670, 93, 28))
        self.top5_random_btn = QtWidgets.QPushButton('換一張',self)
        self.top5_random_btn.setGeometry(QtCore.QRect(790, 700, 93, 28))
        #self.top5_random_btn.clicked.connect(self.openFolder)
        self.top5_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.top5_viewer_btn.setGeometry(QtCore.QRect(790, 730, 93, 28))
        #self.top5_viewer_btn.clicked.connect(self.openFolder)
        self.top5_save_btn = QtWidgets.QPushButton('儲存',self)
        self.top5_save_btn.setGeometry(QtCore.QRect(790, 760, 93, 28))
        # self.top5_save_btn.clicked.connect()

        #top6
        self.top6_image_path = []
        self.top6_image_index = 0
        self.top6_image =  QtWidgets.QGraphicsView(self)
        self.top6_image.setGeometry(QtCore.QRect(920, 20, 151, 121))
        self.top6_scene = QtWidgets.QGraphicsScene()
        self.top6_scene.setSceneRect(0, 0, 151, 121)
        self.top6_scene.clear()
        self.top6_image.setScene(self.top6_scene)
        self.top6label = QtWidgets.QLabel('top6', self)
        self.top6label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.top6label.setAlignment(QtCore.Qt.AlignCenter)
        self.top6label.setGeometry(QtCore.QRect(1080, 20, 93, 28))
        self.top6_random_btn = QtWidgets.QPushButton('換一張',self)
        self.top6_random_btn.setGeometry(QtCore.QRect(1080, 50, 93, 28))
        #self.top6_random_btn.clicked.connect(self.openFolder)
        self.top6_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.top6_viewer_btn.setGeometry(QtCore.QRect(1080, 80, 93, 28))
        #self.top6_viewer_btn.clicked.connect(self.openFolder)
        self.top6_save_btn = QtWidgets.QPushButton('儲存',self)
        self.top6_save_btn.setGeometry(QtCore.QRect(1080, 110, 93, 28))
        # self.top6_save_btn.clicked.connect()

        #top7
        self.top7_image_path = []
        self.top7_image_index = 0
        self.top7_image =  QtWidgets.QGraphicsView(self)
        self.top7_image.setGeometry(QtCore.QRect(920, 200, 151, 121))
        self.top7_scene = QtWidgets.QGraphicsScene()
        self.top7_scene.setSceneRect(0, 0, 151, 121)
        self.top7_scene.clear()
        self.top7_image.setScene(self.top7_scene)
        self.top7label = QtWidgets.QLabel('top7', self)
        self.top7label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.top7label.setAlignment(QtCore.Qt.AlignCenter)
        self.top7label.setGeometry(QtCore.QRect(1080, 200, 93, 28))
        self.top7_random_btn = QtWidgets.QPushButton('換一張',self)
        self.top7_random_btn.setGeometry(QtCore.QRect(1080, 230, 93, 28))
        #self.top7_random_btn.clicked.connect(self.openFolder)
        self.top7_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.top7_viewer_btn.setGeometry(QtCore.QRect(1080, 260, 93, 28))
        #self.top7_viewer_btn.clicked.connect(self.openFolder)
        self.top7_save_btn = QtWidgets.QPushButton('儲存',self)
        self.top7_save_btn.setGeometry(QtCore.QRect(1080, 290, 93, 28))
        # self.top7_save_btn.clicked.connect()

        #top8
        self.top8_image_path = []
        self.top8_image_index = 0
        self.top8_image =  QtWidgets.QGraphicsView(self)
        self.top8_image.setGeometry(QtCore.QRect(920, 360, 151, 121))
        self.top8_scene = QtWidgets.QGraphicsScene()
        self.top8_scene.setSceneRect(0, 0, 151, 121)
        self.top8_scene.clear()
        self.top8_image.setScene(self.top8_scene)
        self.top8label = QtWidgets.QLabel('top8', self)
        self.top8label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.top8label.setAlignment(QtCore.Qt.AlignCenter)
        self.top8label.setGeometry(QtCore.QRect(1080, 360, 93, 28))
        self.top8_random_btn = QtWidgets.QPushButton('換一張',self)
        self.top8_random_btn.setGeometry(QtCore.QRect(1080, 390, 93, 28))
        #self.top8_random_btn.clicked.connect(self.openFolder)
        self.top8_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.top8_viewer_btn.setGeometry(QtCore.QRect(1080, 420, 93, 28))
        #self.top8_viewer_btn.clicked.connect(self.openFolder)
        self.top8_save_btn = QtWidgets.QPushButton('儲存',self)
        self.top8_save_btn.setGeometry(QtCore.QRect(1080, 450, 93, 28))
        # self.top8_save_btn.clicked.connect()

        #top9
        self.top9_image_path = []
        self.top9_image_index = 0
        self.top9_image =  QtWidgets.QGraphicsView(self)
        self.top9_image.setGeometry(QtCore.QRect(920, 510, 151, 121))
        self.top9_scene = QtWidgets.QGraphicsScene()
        self.top9_scene.setSceneRect(0, 0, 151, 121)
        self.top9_scene.clear()
        self.top9_image.setScene(self.top9_scene)
        self.top9label = QtWidgets.QLabel('top9', self)
        self.top9label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.top9label.setAlignment(QtCore.Qt.AlignCenter)
        self.top9label.setGeometry(QtCore.QRect(1080, 510, 93, 28))
        self.top9_random_btn = QtWidgets.QPushButton('換一張',self)
        self.top9_random_btn.setGeometry(QtCore.QRect(1080, 540, 93, 28))
        #self.top9_random_btn.clicked.connect(self.openFolder)
        self.top9_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.top9_viewer_btn.setGeometry(QtCore.QRect(1080, 570, 93, 28))
        #self.top9_viewer_btn.clicked.connect(self.openFolder)
        self.top9_save_btn = QtWidgets.QPushButton('儲存',self)
        self.top9_save_btn.setGeometry(QtCore.QRect(1080, 600, 93, 28))
        # self.top9_save_btn.clicked.connect()

        #top10
        self.top10_image_path = []
        self.top10_image_index = 0
        self.top10_image =  QtWidgets.QGraphicsView(self)
        self.top10_image.setGeometry(QtCore.QRect(920, 670, 151, 121))
        self.top10_scene = QtWidgets.QGraphicsScene()
        self.top10_scene.setSceneRect(0, 0, 151, 121)
        self.top10_scene.clear()
        self.top10_image.setScene(self.top10_scene)
        self.top10label = QtWidgets.QLabel('top10', self)
        self.top10label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.top10label.setAlignment(QtCore.Qt.AlignCenter)
        self.top10label.setGeometry(QtCore.QRect(1080, 670, 93, 28))
        self.top10_random_btn = QtWidgets.QPushButton('換一張',self)
        self.top10_random_btn.setGeometry(QtCore.QRect(1080, 700, 93, 28))
        #self.top10_random_btn.clicked.connect(self.openFolder)
        self.top10_viewer_btn = QtWidgets.QPushButton('放大',self)
        self.top10_viewer_btn.setGeometry(QtCore.QRect(1080, 730, 93, 28))
        #self.top10_viewer_btn.clicked.connect(self.openFolder)
        self.top10_save_btn = QtWidgets.QPushButton('儲存',self)
        self.top10_save_btn.setGeometry(QtCore.QRect(1080, 760, 93, 28))
        # self.top10_save_btn.clicked.connect()

    

    def change_top_image(self,image_path,top_scene,topimage):
        change_image = QtGui.QPixmap(image_path[random.randint(0,len(image_path)-1)])
        change_image = change_image.scaled(224, 224, aspectRatioMode = QtCore.Qt.KeepAspectRatio)
        top_scene.addPixmap(change_image)
        topimage.setScene(top_scene)

    # def runtop10model():
    #     embls = recognizer.get_embeddings("xxoo.dir")
        # self.top1img = QtGui.QPixmap()
        # self.top1img = self.top1img.scaled(151, 121, aspectRatioMode = QtCore.Qt.KeepAspectRatio)
        # self.top1_scene.addPixmap(self.top1img)                   
        # self.top1_image.setScene(self.top1_scene)



    def runtop10Viewer(self,folder_path):
        self.viewer = ImageViewer()
        self.viewer.loadImagePaths(folder_path)
        self.viewer.show()
    
    def runViewer(self):
        folder_path = self.folder_edit.text()
        if folder_path:
            self.viewer = ImageViewer()
            self.viewer.loadImagePaths(folder_path)
            self.viewer.show()

    def openFolder(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, "選擇資料夾")
        if folder_path:
            self.main_image_index = 0
            self.main_scene.clear()
            self.main_image.setScene(self.main_scene)
            self.folder_edit.setText(folder_path)
            self.main_image_dir = folder_path
            self.main_image_path = [os.path.join(self.main_image_dir, filename) for filename in os.listdir(self.main_image_dir) if filename.lower().endswith(('.jpg', '.png', '.jpeg', 'JPG'))]
            self.img = QtGui.QPixmap(self.main_image_path[self.main_image_index])
            self.img = self.img.scaled(500, 500, aspectRatioMode = QtCore.Qt.KeepAspectRatio)
            self.main_scene.addPixmap(self.img)                   
            self.main_image.setScene(self.main_scene)
            self.main_index.setText(f"Image {self.main_image_index + 1}/{len(self.main_image_path)}")

    def preImage(self):
        if self.main_image_path:
            self.main_scene.clear()
            self.main_image.setScene(self.main_scene)
            self.main_image_index = (self.main_image_index - 1) % len(self.main_image_path)
            self.img = QtGui.QPixmap(self.main_image_path[self.main_image_index])
            self.img = self.img.scaled(500, 500, aspectRatioMode = QtCore.Qt.KeepAspectRatio)
            self.main_scene.addPixmap(self.img)
            self.main_image.setScene(self.main_scene)
            self.main_index.setText(f"Image {self.main_image_index + 1}/{len(self.main_image_path)}")

    def nextImage(self):
        if self.main_image_path:
            self.main_scene.clear()
            self.main_image.setScene(self.main_scene)
            self.main_image_index = (self.main_image_index + 1) % len(self.main_image_path)
            self.img = QtGui.QPixmap(self.main_image_path[self.main_image_index])
            self.img = self.img.scaled(500, 500, aspectRatioMode = QtCore.Qt.KeepAspectRatio)
            self.main_scene.addPixmap(self.img)
            self.main_image.setScene(self.main_scene)
            self.main_index.setText(f"Image {self.main_image_index + 1}/{len(self.main_image_path)}")