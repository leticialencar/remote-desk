from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel

from remote_desk.ui.components.icon_button import IconButton
from remote_desk.ui.components.svg_icon import SvgIcon


class TitleBar(QFrame):

    def __init__(self, window, parent=None):
        super().__init__(parent)
        self._window = window
        self.setObjectName("title_bar")
        self.setFixedHeight(46)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(18, 0, 10, 0)
        layout.setSpacing(10)

        layout.addWidget(SvgIcon("logo", 22))

        title = QLabel("RemoteDesk")
        title.setObjectName("title_bar_text")
        layout.addWidget(title)
        layout.addStretch()

        self.minimize_button = IconButton("minimize", 16, "#A9B8D6")
        self.close_button = IconButton("close", 16, "#A9B8D6")

        self.minimize_button.clicked.connect(self._window.showMinimized)
        self.close_button.clicked.connect(self._window.close)

        layout.addWidget(self.minimize_button)
        layout.addWidget(self.close_button)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            handle = self._window.windowHandle()
            if handle is not None:
                handle.startSystemMove()
        super().mousePressEvent(event)