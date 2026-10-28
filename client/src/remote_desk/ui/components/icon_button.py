from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QPushButton

from remote_desk.ui.components.svg_icon import make_icon


class IconButton(QPushButton):

    def __init__(
        self,
        name: str,
        size: int = 18,
        color: str = "#8EA0C4",
        hover_color: str = "#FFFFFF",
        parent=None,
    ):
        super().__init__(parent)
        self._name = name
        self._size = size
        self._color = color
        self._hover_color = hover_color

        self.setObjectName("icon_button")
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFlat(True)
        self.setIconSize(QSize(size, size))
        self.setFixedSize(size + 12, size + 12)
        self._apply(color)

    def set_name(self, name: str) -> None:
        self._name = name
        self._apply(self._color)

    def _apply(self, color: str) -> None:
        self.setIcon(make_icon(self._name, color, self._size))

    def enterEvent(self, event):
        self._apply(self._hover_color)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._apply(self._color)
        super().leaveEvent(event)