APP_STYLE = """
QMainWindow {
    background-color: #0B1120;
}

QWidget {
    color: #E5ECF8;
    font-family: "Segoe UI";
    font-size: 14px;
}

QLabel {
    background: transparent;
}

QFrame#sidebar {
    background-color: #0F192B;
    border-right: 1px solid #1D2B43;
}

QFrame#card {
    background-color: #111D31;
    border: 1px solid #223653;
    border-radius: 14px;
}

QLabel#app_title {
    font-size: 28px;
    font-weight: bold;
    color: #F3F7FF;
}

QLabel#section_title {
    font-size: 18px;
    font-weight: bold;
    color: #F3F7FF;
}

QLabel#muted {
    color: #91A4C5;
    font-size: 13px;
}

QLabel#eyebrow {
    color: #76A9FA;
    font-size: 11px;
    font-weight: bold;
}

QLabel#device_id {
    color: #FFFFFF;
    font-size: 25px;
    font-weight: bold;
}

QLabel#online {
    color: #4ADE9A;
    font-weight: bold;
}

QPushButton {
    background-color: #172740;
    color: #DCE8FF;
    border: 1px solid #294366;
    border-radius: 8px;
    padding: 10px 16px;
}

QPushButton:hover {
    background-color: #203858;
    border-color: #3B82F6;
}

QPushButton#connect_button {
    background-color: #2878F0;
    color: white;
    font-weight: bold;
    border: none;
    padding: 12px 22px;
}

QPushButton#connect_button:hover {
    background-color: #438CFF;
}

QPushButton#nav_active {
    background-color: #17396A;
    color: #FFFFFF;
    border: 1px solid #2456A0;
    text-align: left;
    padding: 12px;
    font-weight: bold;
}

QPushButton#nav_button {
    background-color: transparent;
    border: none;
    color: #A9BADA;
    text-align: left;
    padding: 12px;
}

QPushButton#nav_button:hover {
    background-color: #172740;
    color: white;
}

QLineEdit {
    background-color: #0D1728;
    color: #F3F7FF;
    border: 1px solid #2A4163;
    border-radius: 8px;
    padding: 12px;
    selection-background-color: #2878F0;
}

QLineEdit:focus {
    border: 1px solid #438CFF;
}

QLineEdit::placeholder {
    color: #7084A8;
}
"""