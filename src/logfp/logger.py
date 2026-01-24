import logging
from pathlib import Path

def setup_logging(log_dir: Path | None = None) -> None:
    """
    アプリ全体の logging 設定を行う
    """
    if log_dir is None:
        log_dir = Path("logs")

    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "app.log"

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

    # ルートロガー
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # すでに handler があれば二重登録を防ぐ
    if root_logger.handlers:
        return

    # コンソール出力
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # ファイル出力
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)
