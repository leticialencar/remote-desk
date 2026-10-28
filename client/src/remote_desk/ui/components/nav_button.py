from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QPushButton

from remote_desk.ui.components.svg_icon import make_icon

ICON_SIZE = 18
ICON_COLOR = "#9AABCB"
ICON_COLOR_ACTIVE = "#4F86FF"


class NavButton(QPushButton):

    def __init__(self, text: str, icon_name: str, parent=None):
        super().__init__(f"  {text}", parent)
        self._icon_name = icon_name
        self.setObjectName("nav_button")
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setIconSize(QSize(ICON_SIZE, ICON_SIZE))
        self.setMinimumHeight(44)
        self.set_active(False)

    def set_active(self, active: bool) -> None:
        self.setProperty("active", active)
        color = ICON_COLOR_ACTIVE if active else ICON_COLOR
        self.setIcon(make_icon(self._icon_name, color, ICON_SIZE))
        # força o Qt a reaplicar o QSS com a nova propriedade
        self.style().unpolish(self)
        self.style().polish(self)