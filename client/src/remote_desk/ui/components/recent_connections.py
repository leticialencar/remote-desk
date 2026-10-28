from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton, QVBoxLayout

from remote_desk.ui.components.empty_state import EmptyState


class RecentConnections(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("card")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(22, 16, 22, 16)
        layout.setSpacing(0)

        header = QHBoxLayout()
        title = QLabel("Conexões recentes")
        title.setObjectName("card_header")

        self.see_all_button = QPushButton("Ver tudo")
        self.see_all_button.setObjectName("link_button")
        self.see_all_button.setCursor(Qt.CursorShape.PointingHandCursor)

        header.addWidget(title)
        header.addStretch()
        header.addWidget(self.see_all_button)

        layout.addLayout(header)
        layout.addStretch()
        layout.addWidget(EmptyState("clock", "Nenhuma conexão recente"))
        layout.addStretch()