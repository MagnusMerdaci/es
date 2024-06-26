from PySide6.QtCore import QPoint, QPointF, Qt 
from PySide6.QtGui import QPainter, QTransform, QColor
from typing import Optional, List
import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self, painter: QPainter, transform: QTransform):
        pass

class ShapeList(Shape):
    def __init__(self,
                 relative_transform: Optional[QTransform] = None,
                 shapes: Optional[Shape] = None):
        
        if relative_transform is not None:
            self.relative_transform = relative_transform
        else:
            self.relative_transform = QTransform()
            self.relative_transform.reset()

        if shapes is not None:
            self.shapes = List[Shape] = shapes
        else:
            self.shapes = []

    def draw(self, painter: QPainter, transform: QTransform) -> None:
        for shape in self.shapes:
            shape.draw(painter, transform * self.relative_transform)


    def addShape(self, shape: Shape):
        self.shapes.append(shape)


class Primitive(Shape):
    def __init__(self,
                 point: QPointF,
                 width: float,
                 height: float,
                 border_color: Optional[QColor] = None,
                 border_width: int = 3,
                 fill_color: Optional[QColor] = None,
                 fill_background: bool = True):
        super().__init__()
        self.coordinates = point
        self.width = width
        self.height = height
        if border_color is None:
            self.border_color: QColor = QColor(0,0,0)

        else:
            self.border_color: QColor = border_color
        self.border_width = border_width

        if fill_color is None:
            self.fill_color: QColor = QColor(255, 255, 255)
        else:
            self.fill_color: QColor = fill_color
        self.fill_background: bool = fill_background


    def draw(self, painter: QPainter, transform: QTransform):
        painter.setPen(self.border_color, self.border_width)
        if self.fill_background:
            painter.setBrush(self.fill_color)
        else:
            painter.setBrush(Qt.NoBrush)


class Rectangle(Primitive):
    def __init__(self, painter: QPainter, transform: QTransform):
        super().draw(painter, transform)
        


