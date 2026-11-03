from PySide6.QtCore import Signal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMenu,
    QPushButton,
    QVBoxLayout,
)

from remote_desk.ui.components.svg_icon import make_icon

PLACEHOLDER = "ID do dispositivo remoto"


class RemoteControlCard(QFrame):

    connect_requested = Signal(str)
    file_transfer_requested = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("card")
        self._recent_ids: list[str] = []

        layout = QVBoxLayout(self)
        layout.setContentsMargins(22, 22, 22, 22)
        layout.setSpacing(6)

        title = QLabel("Controlar dispositivo remoto")
        title.setObjectName("section_title")

        subtitle = QLabel(
            "Insira o ID do dispositivo remoto para iniciar a conexão."
        )
        subtitle.setObjectName("muted")
        subtitle.setWordWrap(True)

        self.remote_id_input = QLineEdit()
        self.remote_id_input.setObjectName("select_input")
        self.remote_id_input.setPlaceholderText(PLACEHOLDER)
        self.remote_id_input.setMinimumHeight(44)

        self._dropdown_action = self.remote_id_input.addAction(
            make_icon("chevron_down", "#A9B8D6", 16),
            QLineEdit.ActionPosition.TrailingPosition,
        )
        self._dropdown_action.triggered.connect(self._show_recent_menu)

        self.file_button = QPushButton("Transferência de arquivo")
        self.file_button.setObjectName("secondary_button")
        self.file_button.setMinimumHeight(40)

        self.connect_button = QPushButton("Conectar")
        self.connect_button.setObjectName("connect_button")
        self.connect_button.setMinimumHeight(40)

        buttons = QHBoxLayout()
        buttons.setSpacing(10)
        buttons.addWidget(self.file_button, 1)
        buttons.addWidget(self.connect_button, 1)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(26)
        layout.addWidget(self.remote_id_input)
        layout.addSpacing(8)
        layout.addLayout(buttons)
        layout.addStretch()

        self.connect_button.clicked.connect(self._emit_connect)
        self.remote_id_input.returnPressed.connect(self._emit_connect)
        self.file_button.clicked.connect(self._emit_file_transfer)
        self.remote_id_input.textEdited.connect(self._reset_placeholder)

    def set_recent_ids(self, ids: list[str]) -> None:
        self._recent_ids = list(ids)

    def _show_recent_menu(self) -> None:
        menu = QMenu(self)
        if not self._recent_ids:
            empty = QAction("Nenhum ID recente", menu)
            empty.setEnabled(False)
            menu.addAction(empty)
        for remote_id in self._recent_ids:
            action = menu.addAction(remote_id)
            action.triggered.connect(
                lambda _=False, value=remote_id: self.remote_id_input.setText(value)
            )
        menu.setMinimumWidth(self.remote_id_input.width())
        menu.exec(
            self.remote_id_input.mapToGlobal(self.remote_id_input.rect().bottomLeft())
        )

    def _current_id(self) -> str | None:
        remote_id = self.remote_id_input.text().strip()
        if not remote_id:
            self.remote_id_input.setPlaceholderText("Digite um ID antes de continuar!")
            self.remote_id_input.setFocus()
            return None
        return remote_id

    def _reset_placeholder(self, _text: str) -> None:
        self.remote_id_input.setPlaceholderText(PLACEHOLDER)

    def _emit_connect(self) -> None:
        remote_id = self._current_id()
        if remote_id:
            self.connect_requested.emit(remote_id)

    def _emit_file_transfer(self) -> None:
        remote_id = self._current_id()
        if remote_id:
            self.file_transfer_requested.emit(remote_id)