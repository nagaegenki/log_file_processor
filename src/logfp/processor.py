from pathlib import Path

import logging

logger = logging.getLogger(__name__)

def process_log(message: str) -> None:
    if message is None:
        raise ValueError("message must not be None")

    if not isinstance(message, str):
        raise TypeError("message must be a string")

    if message == "":
        logger.warning("Empty message received")
        return

    logger.info(f"Processing message: {message}")

    if "error" in message.lower():
        logger.error("Error detected in message!")

def process_log_file(path: Path) -> int:
    if not path.exists():
        raise FileNotFoundError(path)

    count = 0

    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            process_log(line)
            count += 1

    return count
