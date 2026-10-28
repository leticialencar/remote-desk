from PySide6.QtCore import Signal
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget

from remote_desk.ui.components.device_card import DeviceCard
from remote_desk.ui.components.recent_connections import RecentConnections
from remote_desk.ui.components.remote_control_card import RemoteControlCard


class ConnectionPage(QWidget):

    connect_requested = Signal(str)
    file_transfer_requested = Signal(str)

    def __init__(self, device_id: str, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(22, 14, 22, 22)
        layout.setSpacing(18)

        top_row = QHBoxLayout()
        top_row.setSpacing(18)

        self.device_card = DeviceCard(device_id)
        self.remote_card = RemoteControlCard()

        top_row.addWidget(self.device_card, 1)
        top_row.addWidget(self.remote_card, 1)

        self.device_card.setMinimumHeight(360)
        self.remote_card.setMinimumHeight(360)

        self.recent = RecentConnections()
        self.recent.setMinimumHeight(170)

        layout.addLayout(top_row)
        layout.addWidget(self.recent)
        layout.addStretch()

        self.remote_card.connect_requested.connect(self.connect_requested)
        self.remote_card.file_transfer_requested.connect(self.file_transfer_requested)