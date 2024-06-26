from dataclasses import dataclass, field
from Shapes import ShapeList
'''from PySide6.QtGui import QPainter, QTransform'''
@dataclass
class Document:
    scene: ShapeList = ShapeList()
    file_name: str = "Untitled"
    modified: bool = True

    '''def draw(self, painter: QPainter, transform: QTransform):
        self.scene.draw(painter, transform)'''
    
    @staticmethod
    def create_example_document() -> 'Document':
        result: Document = Document([], "Example scene", False)
        return result