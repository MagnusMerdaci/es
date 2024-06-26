from PySide6.QtWidgets import QMainWindow, QMenu, QWidget, QMessageBox, QMenuBar, QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QPixmap, QCloseEvent, QTransform
from Documents import Document
from Shapes import ShapeList

import sys



class Paint_Area(QWidget):
    def __init__(self, parent: QWidget, scene: ShapeList):
        super().__int__(parent)
        self.setMinimumWidth(640)
        self.setMinimumHeight(540)
        self.scene = scene
        self.zoom: float = 1.0


        self.PAN_MODE: int = 0
        self.ZOOM_MODE: int = 1
        self.MODE: int = self.PAN_MODE


        self.setMouseTracking(True)

    def compute_transform(self) -> QTransform:
        width: int = self.width()
        height: int = self.height()
        return (QTransform.fromScale(self.zoom, self.zoom)
                *QTransform.fromScale(height/2, width/2)
                * QTransform.fromTranslate(width/2.0, height/2.0)
                * QTransform.fromTranslate(self.pan.x(), self.pan.y()))



class MyWindow(QMainWindow):

    def info_action_handler(self):
        QMessageBox.information(self, 'Info', 'Manüli :) ∑ƒ(π)', QMessageBox.Ok)

    def open_doc_action_handler(self):
        QMessageBox.information(self, "Missing Feature...",
                                "Not yet implemented.", QMessageBox.Ok)
    def save_action_handler(self):
        QMessageBox.information(self, 'Error', 
                                'Feature not yet implemented', QMessageBox.Ok)
        
    def quit_action_handler(self):
        self.close()

    def closeEvent(self, ev: QCloseEvent):
        if QMessageBox.question(self, 'Leave?',
                    'Are you sure you want to leave?', 
                    QMessageBox.Yes | QMessageBox.yes) == QMessageBox.Yes:
            ev.setAccepted(True)
        else:
            ev.setAccepted(False)


    def __init__(self, parent):
        super().__init__(parent)

        self.document: Document = Document.create_example_document()


        self.file_menu: QMenu = self.menuBar().addMenu("&File")

        self.open_action = self.file_menu.addAction('&Open')
        self.open_action.setShortcut(QKeySequence(Qt.CTRL | Qt.Key_O))
        self.open_action.setIcon(QPixmap("open_32x32.png"))
        self.open_action.triggered.connect(self.open_doc_action_handler)

        self.save_action = self.file_menu.addAction('&Save')
        self.save_action.setShortcut(QKeySequence((Qt.CTRL | Qt.Key_P)))
        self.save_action.setIcon(QPixmap("saveas_26x26.png"))
        self.save_action.triggered.connect(self.save_action_handler)

        self.file_menu.addSeparator()

        self.quit_action = self.file_menu.addAction('&Quit')
        self.quit_action.setShortcut(QKeySequence((Qt.CTRL | Qt.Key_Q)))
        self.quit_action.setIcon(QPixmap("quit_26x26.png"))
        self.quit_action.triggered.connect(self.quit_action_handler)

        self.info_action = self.file_menu.addAction('&Info')
        self.info_action.setShortcut(QKeySequence((Qt.CTRL | Qt.Key_I)))
        self.info_action.setIcon(QPixmap("info_32x32.png"))
        self.info_action.triggered.connect(self.info_action_handler)

if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    mainwindow: MyWindow = MyWindow(None)
    mainwindow.show()
    app.exec()



