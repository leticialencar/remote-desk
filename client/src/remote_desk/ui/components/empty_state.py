from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QWidget

from remote_desk.ui.components.svg_icon import SvgIcon


class EmptyState(QWidget):

    def __init__(self, icon_name: str, text: str, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 8, 0, 8)
        layout.setSpacing(10)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(
            SvgIcon(icon_name, 28, "#A9B8D6"), 0, Qt.AlignmentFlag.AlignHCenter
        )

        label = QLabel(text)
        label.setObjectName("muted_small")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)