from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QVBoxLayout

from remote_desk.ui.components.nav_button import NavButton
from remote_desk.ui.components.status_indicator import StatusIndicator


class Sidebar(QFrame):

    page_changed = Signal(int)

    ITEMS = [
        ("Conexão", "monitor"),
        ("Configurações", "settings"),
        ("Sobre", "info"),
    ]

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("sidebar")
        self.setFixedWidth(200)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 12, 10, 18)
        layout.setSpacing(6)

        self._buttons: list[NavButton] = []
        for index, (text, icon_name) in enumerate(self.ITEMS):
            button = NavButton(text, icon_name)
            button.clicked.connect(lambda _=False, i=index: self.select(i))
            layout.addWidget(button)
            self._buttons.append(button)

        layout.addStretch()
        layout.addWidget(StatusIndicator("Pronto para conectar"))

        self.select(0, emit=False)

    def select(self, index: int, emit: bool = True) -> None:
        for i, button in enumerate(self._buttons):
            button.set_active(i == index)
        if emit:
            self.page_changed.emit(index)