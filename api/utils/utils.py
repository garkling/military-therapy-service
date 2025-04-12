import uuid
from datetime import datetime
from datetime import UTC


def get_uuid_str():
    return str(uuid.uuid4())


def get_current_date_iso_string() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
