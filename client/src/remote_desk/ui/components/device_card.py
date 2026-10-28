import secrets
import string

from PySide6.QtCore import QTimer
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QVBoxLayout

from remote_desk.ui.components.icon_button import IconButton


def format_device_id(device_id: str) -> str:
    """'123456789' -> '123 456 789'"""
    return f"{device_id[:3]} {device_id[3:6]} {device_id[6:]}".strip()


def generate_password(length: int = 6) -> str:
    # vai ser trocado pela senha de vdd quando o device estiver configurado 
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


class DeviceCard(QFrame):

    def __init__(self, device_id: str, parent=None):
        super().__init__(parent)
        self.setObjectName("card")

        self._raw_id = device_id
        self._password = generate_password()
        self._password_visible = False

        layout = QVBoxLayout(self)
        layout.setContentsMargins(22, 22, 22, 22)
        layout.setSpacing(6)

        title = QLabel("Este dispositivo")
        title.setObjectName("section_title")

        subtitle = QLabel(
            "Compartilhe seu ID para que outros possam se conectar "
            "a este computador."
        )
        subtitle.setObjectName("muted")
        subtitle.setWordWrap(True)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(10)
        layout.addWidget(self._build_panel())
        layout.addStretch()

        self._refresh_password()

    def _build_panel(self) -> QFrame:
        panel = QFrame()
        panel.setObjectName("inner_panel")

        layout = QVBoxLayout(panel)
        layout.setContentsMargins(18, 16, 14, 16)
        layout.setSpacing(6)

        id_caption = QLabel("ID do seu dispositivo")
        id_caption.setObjectName("field_caption")

        self.device_id_label = QLabel(format_device_id(self._raw_id))
        self.device_id_label.setObjectName("device_id")

        self.copy_button = IconButton("copy", 18, "#A9B8D6")
        self.copy_button.setToolTip("Copiar ID")
        self.copy_button.clicked.connect(self._copy_id)

        id_row = QHBoxLayout()
        id_row.addWidget(self.device_id_label)
        id_row.addStretch()
        id_row.addWidget(self.copy_button)

        divider = QFrame()
        divider.setObjectName("divider")
        divider.setFixedHeight(1)

        password_caption = QLabel("Senha de acesso")
        password_caption.setObjectName("field_caption")

        self.password_label = QLabel()
        self.password_label.setObjectName("password")

        self.visibility_button = IconButton("eye", 18, "#A9B8D6")
        self.visibility_button.setToolTip("Mostrar senha")
        self.visibility_button.clicked.connect(self._toggle_password)

        self.refresh_button = IconButton("refresh", 18, "#A9B8D6")
        self.refresh_button.setToolTip("Gerar nova senha")
        self.refresh_button.clicked.connect(self._new_password)

        password_row = QHBoxLayout()
        password_row.setSpacing(2)
        password_row.addWidget(self.password_label)
        password_row.addStretch()
        password_row.addWidget(self.visibility_button)
        password_row.addWidget(self.refresh_button)

        layout.addWidget(id_caption)
        layout.addLayout(id_row)
        layout.addSpacing(6)
        layout.addWidget(divider)
        layout.addSpacing(6)
        layout.addWidget(password_caption)
        layout.addLayout(password_row)
        return panel

    def _copy_id(self) -> None:
        QGuiApplication.clipboard().setText(self._raw_id)
        self.copy_button.set_name("check")
        QTimer.singleShot(1200, lambda: self.copy_button.set_name("copy"))

    def _toggle_password(self) -> None:
        self._password_visible = not self._password_visible
        self.visibility_button.set_name(
            "eye_off" if self._password_visible else "eye"
        )
        self.visibility_button.setToolTip(
            "Ocultar senha" if self._password_visible else "Mostrar senha"
        )
        self._refresh_password()

    def _new_password(self) -> None:
        self._password = generate_password()
        self._refresh_password()

    def _refresh_password(self) -> None:
        text = self._password if self._password_visible else "•" * len(self._password)
        self.password_label.setText(text)