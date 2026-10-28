from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
)

from remote_desk.ui.styles import APP_STYLE
from remote_desk.core.device import get_device_id


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Remote Desk")
        self.resize(1100, 720)
        self.setMinimumSize(850, 600)

        self.setStyleSheet(APP_STYLE)

        central_widget = QWidget()
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)


        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(210)

        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(16, 24, 16, 20)
        sidebar_layout.setSpacing(12)

        logo = QLabel("Futura logo ;)")
        logo.setStyleSheet("""
            font-size: 19px;
            font-weight: bold;
            color: #F3F7FF;
            padding: 8px 2px 28px 2px;
        """)

        sidebar_layout.addWidget(logo)

        self.home_button = QPushButton("Início")
        self.home_button.setObjectName("nav_active")

        self.connections_button = QPushButton("Conexões")
        self.connections_button.setObjectName("nav_button")

        self.settings_button = QPushButton("Configurações")
        self.settings_button.setObjectName("nav_button")

        self.about_button = QPushButton("Sobre")
        self.about_button.setObjectName("nav_button")

        sidebar_layout.addWidget(self.home_button)
        sidebar_layout.addWidget(self.connections_button)
        sidebar_layout.addWidget(self.settings_button)
        sidebar_layout.addWidget(self.about_button)

        sidebar_layout.addStretch()

        sidebar_footer = QLabel(
            "REMOTE DESK\n"
            "Aqui vai ter um slogan\n"
            "beeem legal."
        )
        sidebar_footer.setObjectName("muted")
        sidebar_footer.setWordWrap(True)

        sidebar_layout.addWidget(sidebar_footer)

        content = QWidget()

        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(30, 28, 30, 28)
        content_layout.setSpacing(22)

        header_layout = QHBoxLayout()
        header_text = QVBoxLayout()

        title = QLabel("Remote Desk")
        title.setObjectName("app_title")

        subtitle = QLabel(
            "Acesse e gerencie seus dispositivos remotamente."
        )
        subtitle.setObjectName("muted")

        header_text.addWidget(title)
        header_text.addWidget(subtitle)

        online_label = QLabel("●  Aplicativo iniciado")
        online_label.setObjectName("online")
        online_label.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignVCenter
        )

        header_layout.addLayout(header_text)
        header_layout.addStretch()
        header_layout.addWidget(online_label)

        content_layout.addLayout(header_layout)

        
        device_card = QFrame()
        device_card.setObjectName("card")

        device_layout = QHBoxLayout(device_card)
        device_layout.setContentsMargins(24, 24, 24, 24)
        device_layout.setSpacing(20)

        computer_icon = QLabel("i")
        computer_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        computer_icon.setFixedSize(68, 68)
        computer_icon.setStyleSheet("""
            background-color: #17396A;
            color: #65A5FF;
            border-radius: 34px;
            font-size: 30px;
        """)

        device_info = QVBoxLayout()
        device_info.setSpacing(8)

        device_caption = QLabel("ID deste dispositivo")
        device_caption.setObjectName("eyebrow")

        device_id = get_device_id()

        formatted_id = (
            f"{device_id[:3]} "
            f"{device_id[3:6]} "
            f"{device_id[6:]}"
        )

        self.device_id = QLabel(formatted_id)
        self.device_id.setObjectName("device_id")

        device_description = QLabel(
            "Compartilhe este ID com quem quer se conectar "
            "ao seu dispositivo."
        )
        device_description.setObjectName("muted")
        device_description.setWordWrap(True)

        device_info.addWidget(device_caption)
        device_info.addWidget(self.device_id)
        device_info.addWidget(device_description)

        device_layout.addWidget(computer_icon)
        device_layout.addLayout(device_info, 1)

        content_layout.addWidget(device_card)


        connection_card = QFrame()
        connection_card.setObjectName("card")

        connection_layout = QVBoxLayout(connection_card)
        connection_layout.setContentsMargins(24, 24, 24, 24)
        connection_layout.setSpacing(12)

        connection_title = QLabel("Conectar com outro dispositivo")
        connection_title.setObjectName("section_title")

        connection_subtitle = QLabel(
            "Digite o identificador do dispositivo ao qual deseja acessar."
        )
        connection_subtitle.setObjectName("muted")
        connection_subtitle.setWordWrap(True)

        input_layout = QHBoxLayout()
        input_layout.setSpacing(12)

        self.remote_id_input = QLineEdit()
        self.remote_id_input.setPlaceholderText(
            "Digite o ID do computador"
        )
        self.remote_id_input.setMinimumHeight(46)

        self.connect_button = QPushButton("Conectar")
        self.connect_button.setObjectName("connect_button")
        self.connect_button.setMinimumHeight(46)
        self.connect_button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        input_layout.addWidget(self.remote_id_input, 1)
        input_layout.addWidget(self.connect_button)

        connection_layout.addWidget(connection_title)
        connection_layout.addWidget(connection_subtitle)
        connection_layout.addSpacing(8)
        connection_layout.addLayout(input_layout)

        content_layout.addWidget(connection_card)

        content_layout.addStretch()

        main_layout.addWidget(sidebar)
        main_layout.addWidget(content, 1)

        self.setCentralWidget(central_widget)

        self.connect_button.clicked.connect(self.handle_connect)
        self.remote_id_input.returnPressed.connect(self.handle_connect)

    def handle_connect(self):
        remote_id = self.remote_id_input.text().strip()

        if not remote_id:
            self.remote_id_input.setPlaceholderText(
                "Digite um ID antes de continuar!"
            )
            self.remote_id_input.setFocus()
            return

        print(
            f"Solicitação de conexão para o dispositivo: {remote_id}"
        )