import re

FONT_SCALE = 1.2


def _scale_fonts(style: str, scale: float) -> str:
    def replace(match: re.Match) -> str:
        size = int(int(match.group(1)) * scale + 0.5)
        return f"font-size: {size}px"

    return re.sub(r"font-size:\s*(\d+)px", replace, style)


_BASE_STYLE = """
QMainWindow {
    background: transparent;
}

QWidget {
    color: #E5ECF8;
    font-family: "Segoe UI", "Inter", sans-serif;
    font-size: 13px;
}

QLabel {
    background: transparent;
}

QFrame#window_root {
    background-color: #070F24;
    border: 1px solid #16233D;
    border-radius: 14px;
}

QFrame#title_bar {
    background: transparent;
    border-bottom: 1px solid #101B33;
}

QLabel#title_bar_text {
    color: #F3F7FF;
    font-size: 15px;
    font-weight: 600;
}

QPushButton#icon_button {
    background: transparent;
    border: none;
    border-radius: 6px;
    padding: 0;
}

QPushButton#icon_button:hover {
    background-color: #111D38;
}

QFrame#sidebar {
    background: transparent;
    border-right: 1px solid #101B33;
}

QPushButton#nav_button {
    background-color: transparent;
    color: #9AABCB;
    border: none;
    border-left: 3px solid transparent;
    border-radius: 8px;
    text-align: left;
    padding: 0 12px;
}

QPushButton#nav_button:hover {
    background-color: #0E1830;
    color: #FFFFFF;
}

QPushButton#nav_button[active="true"] {
    background-color: #0F1D3D;
    color: #4F86FF;
    border-left: 3px solid #3E63D6;
    font-weight: 600;
}

QFrame#status_indicator {
    background: transparent;
}

QFrame#status_dot {
    background-color: #1EBE63;
    border-radius: 4px;
}

QLabel#status_text {
    color: #C5D1E8;
    font-size: 12px;
}

QFrame#card {
    background-color: #0B1427;
    border: 1px solid #16233D;
    border-radius: 14px;
}

QFrame#inner_panel {
    background-color: #0A1326;
    border: 1px solid #16233D;
    border-radius: 10px;
}

QFrame#divider {
    background-color: #16233D;
    border: none;
}

QLabel#section_title {
    font-size: 17px;
    font-weight: 600;
    color: #F3F7FF;
}

QLabel#card_header {
    font-size: 12px;
    font-weight: 600;
    color: #F3F7FF;
}

QLabel#muted {
    color: #8EA0C4;
    font-size: 12px;
}

QLabel#muted_small {
    color: #8EA0C4;
    font-size: 11px;
}

QLabel#field_caption {
    color: #C5D1E8;
    font-size: 12px;
}

QLabel#device_id {
    color: #3E7BFF;
    font-size: 26px;
    font-weight: 700;
}

QLabel#password {
    color: #E5ECF8;
    font-size: 20px;
    letter-spacing: 2px;
}

QLineEdit {
    background-color: #0D1830;
    color: #F3F7FF;
    border: 1px solid #1C2B4A;
    border-radius: 8px;
    padding: 0 12px;
    selection-background-color: #2F63F2;
}

QLineEdit:focus {
    border: 1px solid #3E63D6;
}

QPushButton {
    background-color: #111D38;
    color: #DCE8FF;
    border: 1px solid #1C2B4A;
    border-radius: 8px;
    padding: 0 16px;
}

QPushButton#secondary_button {
    background-color: #141F37;
    color: #E5ECF8;
    border: 1px solid #1C2B4A;
    font-size: 12px;
}

QPushButton#secondary_button:hover {
    background-color: #1A2845;
    border-color: #2C4272;
}

QPushButton#connect_button {
    background-color: #2F63F2;
    color: #FFFFFF;
    border: none;
    font-weight: 600;
}

QPushButton#connect_button:hover {
    background-color: #4575F5;
}

QPushButton#link_button {
    background: transparent;
    border: none;
    color: #3E7BFF;
    font-size: 11px;
    padding: 0;
}

QPushButton#link_button:hover {
    color: #6B9BFF;
}

QMenu {
    background-color: #0D1830;
    border: 1px solid #1C2B4A;
    border-radius: 8px;
    padding: 4px;
}

QMenu::item {
    padding: 8px 14px;
    border-radius: 6px;
}

QMenu::item:selected {
    background-color: #16294D;
}

QToolTip {
    background-color: #0D1830;
    color: #E5ECF8;
    border: 1px solid #1C2B4A;
}
"""


APP_STYLE = _scale_fonts(_BASE_STYLE, FONT_SCALE)