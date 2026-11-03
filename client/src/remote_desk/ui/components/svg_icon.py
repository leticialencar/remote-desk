from PySide6.QtCore import QByteArray, QRectF, QSize, Qt
from PySide6.QtGui import QGuiApplication, QIcon, QPainter, QPixmap
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QLabel

from remote_desk.ui.icons import ICONS, LOGO_SVG


def render_svg(name: str, color: str, size: int) -> QPixmap:
    template = LOGO_SVG if name == "logo" else ICONS[name]
    svg = template.replace("{color}", color).encode("utf-8")

    screen = QGuiApplication.primaryScreen()
    ratio = screen.devicePixelRatio() if screen else 1.0

    pixmap = QPixmap(int(size * ratio), int(size * ratio))
    pixmap.fill(Qt.GlobalColor.transparent)
    pixmap.setDevicePixelRatio(ratio)

    renderer = QSvgRenderer(QByteArray(svg))
    painter = QPainter(pixmap)
    renderer.render(painter, QRectF(0, 0, size, size))
    painter.end()
    return pixmap


def make_icon(name: str, color: str, size: int) -> QIcon:
    return QIcon(render_svg(name, color, size))


class SvgIcon(QLabel):

    def __init__(self, name: str, size: int = 18, color: str = "#8EA0C4", parent=None):
        super().__init__(parent)
        self._name = name
        self._size = size
        self._color = color
        self.setFixedSize(QSize(size, size))
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self._refresh()

    def set_name(self, name: str) -> None:
        self._name = name
        self._refresh()

    def set_color(self, color: str) -> None:
        self._color = color
        self._refresh()

    def _refresh(self) -> None:
        self.setPixmap(render_svg(self._name, self._color, self._size))