from ultralytics import YOLO
from PyQt5 import QtWidgets, QtGui
from PIL import Image
from pathlib import Path
import shutil
import sys
import os

#檔案開啟
def openfile():
    global filePath
    filePath, _ = QtWidgets.QFileDialog.getOpenFileName(filter='IMAGE(*.jpg *.png *.JPG)') #限制檔案.jpg .png .JPG
    if filePath:
        img = QtGui.QPixmap(filePath)
        img = img.scaled(900, 480)
        openscene.addPixmap(img)
        opengrview.setScene(openscene)
        # print(filePath)
    return

#Yolo model(這邊應該還要再修)
def yolomodel():
    global filename
    model = YOLO("YOLO/best.pt")
    model.predict(source=filePath,mode="predict",project="temp",name='predict',save=True,imgsz=(512, 512),conf=0.51,device = "cpu")
    # print(result)
    #一次一張，垃圾桶會出問題
    filename = (os.listdir('temp/predict'))[0]
    if filename.endswith(('.png', '.jpg', '.JPG')):
        file = os.path.join('temp/predict', filename)
        img = QtGui.QPixmap(file)
        img = img.scaled(900, 480)
        modelscene.clear()
        modelscene.addPixmap(img)
        modelgrview.setScene(modelscene)
        #檔案搬移
        shutil.move(file,'test') #修改寫法
        shutil.rmtree(Path('temp'))

def savefile():
    filePath, _= QtWidgets.QFileDialog.getSaveFileName(filter='IMAGE(*.jpg *.png *.JPG)') #限制檔案.jpg .png .JPG
    if filePath:
        img = os.path.join('test', filename)
        shutil.move(img,filePath)
        # shutil.rmtree(Path('temp'))
        

#介面框架
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("KURO SHIO PHOTO-ID") # 設定標題
MainWindow.resize(1000, 800) #視窗大小應該還需要調整
#MainWindow.setStyleSheet('background:#fcc;') #背景顏色(不是很懂反正改了很醜?)

openbtn = QtWidgets.QPushButton(MainWindow)
openbtn.move(20, 20)
openbtn.setText('選擇圖片')
openbtn.clicked.connect(openfile)

modelbtn = QtWidgets.QPushButton(MainWindow)
modelbtn.move(20, 50)
modelbtn.setText('執行YOLO')
modelbtn.clicked.connect(yolomodel)

savelbtn = QtWidgets.QPushButton(MainWindow)
savelbtn.move(20, 80)
savelbtn.setText('儲存檔案')
savelbtn.clicked.connect(savefile)

#右上圖(原圖應該不需要)
opengrview = QtWidgets.QGraphicsView(MainWindow)
opengrview.setGeometry(500, 0, 500, 400)
openscene = QtWidgets.QGraphicsScene()
openscene.setSceneRect(0, 0, 900, 480)
opengrview.setScene(openscene)
#右下圖(Yolo的結果圖)
modelgrview = QtWidgets.QGraphicsView(MainWindow)
modelgrview.setGeometry(500, 400, 500, 400)
modelscene = QtWidgets.QGraphicsScene()
modelscene.setSceneRect(0, 0, 900, 480)
modelgrview.setScene(modelscene)


MainWindow.show()
sys.exit(app.exec_())