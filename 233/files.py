from datetime import datetime
from pathlib import Path, PosixPath
from zipfile import ZipFile, ZIP_DEFLATED

TMP = Path("tmp")
LOG_DIR = TMP / "logs"
ZIP_FILE = "logs.zip"


def _get_file_date(_file: Path) -> datetime:
    return datetime.fromtimestamp(_file.stat().st_mtime)


def zip_last_n_files(directory: Path = LOG_DIR, zip_file: str = ZIP_FILE, n: int = 3):
    files = sorted(directory.iterdir(), key=lambda x: _get_file_date(x), reverse=True)

    with ZipFile(zip_file, "w") as zf:
        for log_file in files[:n]:
            date = _get_file_date(log_file).strftime("%Y-%m-%d")
            new_name = f"{log_file.stem}_{date}.log"
            zf.write(log_file, new_name)
