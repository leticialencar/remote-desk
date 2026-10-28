from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget


class AboutPage(QWidget):

    TITLE = "Sobre"
    TEXT = (
        "Aqui vai ter alguma coisa bem massa, uma biografia sobre mim "
        "ou alguma coisa do app"
    )

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(22, 14, 22, 22)
        layout.setSpacing(18)

        card = QFrame()
        card.setObjectName("card")

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(22, 22, 22, 22)
        card_layout.setSpacing(10)

        title = QLabel(self.TITLE)
        title.setObjectName("section_title")

        text = QLabel(self.TEXT)
        text.setObjectName("muted")
        text.setWordWrap(True)

        card_layout.addWidget(title)
        card_layout.addWidget(text)
        card_layout.addStretch()

        layout.addWidget(card)