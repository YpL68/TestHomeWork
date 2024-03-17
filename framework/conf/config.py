from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
LOG_FILE_PATH = str(Path(BASE_DIR / "test_app.log"))
