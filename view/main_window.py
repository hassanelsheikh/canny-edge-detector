# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage
import cv2
from PyQt5.QtGui import QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 360, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.Before = QtWidgets.QGraphicsView(self.centralwidget)
        self.Before.setGeometry(QtCore.QRect(90, 130, 256, 192))
        self.Before.setObjectName("Before")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 80, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.after = QtWidgets.QGraphicsView(self.centralwidget)
        self.after.setGeometry(QtCore.QRect(420, 130, 256, 192))
        self.after.setObjectName("after")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 110, 71, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(520, 110, 41, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.kernelLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.kernelLineEdit.setGeometry(QtCore.QRect(100, 420, 51, 20))
        self.kernelLineEdit.setObjectName("kernelLineEdit")
        self.lowThresholdLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lowThresholdLineEdit.setGeometry(QtCore.QRect(100, 450, 51, 20))
        self.lowThresholdLineEdit.setObjectName("lowThresholdLineEdit")
        self.highThresholdLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.highThresholdLineEdit.setGeometry(QtCore.QRect(100, 480, 51, 20))
        self.highThresholdLineEdit.setObjectName("highThresholdLineEdit")
              # Labels for input fields
        self.kernelLabel = QtWidgets.QLabel(self.centralwidget)
        self.kernelLabel.setGeometry(QtCore.QRect(20, 420, 71, 16))
        self.kernelLabel.setObjectName("kernelLabel")
        self.kernelLabel.setText("Kernel:")
        
        self.lowThresholdLabel = QtWidgets.QLabel(self.centralwidget)
        self.lowThresholdLabel.setGeometry(QtCore.QRect(20, 450, 71, 16))
        self.lowThresholdLabel.setObjectName("lowThresholdLabel")
        self.lowThresholdLabel.setText("Low Threshold:")
        
        self.highThresholdLabel = QtWidgets.QLabel(self.centralwidget)
        self.highThresholdLabel.setGeometry(QtCore.QRect(20, 480, 71, 16))
        self.highThresholdLabel.setObjectName("highThresholdLabel")
        self.highThresholdLabel.setText("High Threshold:")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuCanny_edge_detector = QtWidgets.QMenu(self.menubar)
        self.menuCanny_edge_detector.setObjectName("menuCanny_edge_detector")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCanny_edge_detector.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Apply "))
        self.pushButton_2.setText(_translate("MainWindow", "Browse image"))
        self.lineEdit.setText(_translate("MainWindow", "Initial image"))
        self.lineEdit_2.setText(_translate("MainWindow", "Result"))
        self.menuCanny_edge_detector.setTitle(_translate("MainWindow", "Canny edge detector"))

    def display_initial_image(self, image_data):
        qimage = QImage(image_data.data, image_data.shape[1], image_data.shape[0], 
                        QImage.Format_RGB888).rgbSwapped()

        # Convert QImage to QPixmap
        pixmap = QPixmap.fromImage(qimage)

        # Create a QGraphicsScene
        scene = QtWidgets.QGraphicsScene()

        # Add the QPixmap to QGraphicsScene as QGraphicsPixmapItem
        pixmap_item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(pixmap_item)

        # Set QGraphicsScene to QGraphicsView
        self.Before.setScene(scene)
        self.Before.fitInView(pixmap_item)

    def display_result_image(self, image_data):
        # the image is grayscale
        qimage = QImage(image_data.data, image_data.shape[1], image_data.shape[0], 
                        QImage.Format_Grayscale8)

        #Display in the after QGraphicsView
        pixmap = QPixmap.fromImage(qimage)
        scene = QtWidgets.QGraphicsScene()
        pixmap_item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(pixmap_item)
        self.after.setScene(scene)
        self.after.show()
        self.after.fitInView(pixmap_item)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
