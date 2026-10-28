from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QMainWindow,
    QSizeGrip,
    QStackedWidget,
    QVBoxLayout,
)

from remote_desk.core.device import get_device_id
from remote_desk.ui.about_page import AboutPage
from remote_desk.ui.components.empty_state import EmptyState
from remote_desk.ui.components.sidebar import Sidebar
from remote_desk.ui.components.title_bar import TitleBar
from remote_desk.ui.connection_page import ConnectionPage
from remote_desk.ui.styles import APP_STYLE


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RemoteDesk")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.resize(1100, 730)
        self.setMinimumSize(900, 600)
        self.setStyleSheet(APP_STYLE)

        root = QFrame()
        root.setObjectName("window_root")
        root_layout = QVBoxLayout(root)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        self.title_bar = TitleBar(self)
        root_layout.addWidget(self.title_bar)

        body = QHBoxLayout()
        body.setContentsMargins(0, 0, 0, 0)
        body.setSpacing(0)

        self.sidebar = Sidebar()
        self.pages = QStackedWidget()

        self.connection_page = ConnectionPage(get_device_id())

        self.pages.addWidget(self.connection_page)
        self.pages.addWidget(EmptyState("settings", "Configurações em breve"))
        self.pages.addWidget(AboutPage())

        body.addWidget(self.sidebar)
        body.addWidget(self.pages, 1)
        root_layout.addLayout(body, 1)

        self.setCentralWidget(root)

        self.size_grip = QSizeGrip(self)
        self.size_grip.setFixedSize(16, 16)

        self.sidebar.page_changed.connect(self.pages.setCurrentIndex)
        self.connection_page.connect_requested.connect(self.handle_connect)
        self.connection_page.file_transfer_requested.connect(
            self.handle_file_transfer
        )

    def handle_connect(self, remote_id: str) -> None:
        print(f"Solicitação de conexão para o dispositivo: {remote_id}")

    def handle_file_transfer(self, remote_id: str) -> None:
        print(f"Solicitação de transferência de arquivo para: {remote_id}")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.size_grip.move(
            self.width() - self.size_grip.width(),
            self.height() - self.size_grip.height(),
        )

    def changeEvent(self, event):
        super().changeEvent(event)
        if hasattr(self, "title_bar"):
            self.title_bar.sync_maximized(self.isMaximized())