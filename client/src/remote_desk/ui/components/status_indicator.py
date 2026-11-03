from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel


class StatusIndicator(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent)
        self.setObjectName("status_indicator")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 0, 0, 0)
        layout.setSpacing(10)

        dot = QFrame()
        dot.setObjectName("status_dot")
        dot.setFixedSize(8, 8)

        self.label = QLabel(text)
        self.label.setObjectName("status_text")

        layout.addWidget(dot, 0, Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(self.label, 1, Qt.AlignmentFlag.AlignVCenter)