import json
import secrets
from pathlib import Path


APP_DATA_DIR = Path.home() / "AppData" / "Local" / "RemoteDesk"
DEVICE_FILE = APP_DATA_DIR / "device.json"


def generate_device_id() -> str:
    return str(secrets.randbelow(900_000_000) + 100_000_000)


def save_device_id(device_id: str) -> None:
    APP_DATA_DIR.mkdir(parents=True, exist_ok=True)

    data = {
        "device_id": device_id
    }

    DEVICE_FILE.write_text(
        json.dumps(data, indent=4),
        encoding="utf-8",
    )


def load_device_id() -> str | None:
    if not DEVICE_FILE.exists():
        return None

    try:
        data = json.loads(
            DEVICE_FILE.read_text(encoding="utf-8")
        )
        device_id = data.get("device_id")

        if (
            isinstance(device_id, str)
            and len(device_id) == 9
            and device_id.isdigit()
        ):
            return device_id

    except (OSError, json.JSONDecodeError):
        pass

    return None


def get_device_id() -> str:
    device_id = load_device_id()

    if device_id is not None:
        return device_id

    device_id = generate_device_id()
    save_device_id(device_id)

    return device_id