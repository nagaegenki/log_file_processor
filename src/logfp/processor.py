import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def classify_message(line: str) -> str:
    if not line.strip():
        logger.warning("Empty message received")
        return "warning"

    lower = line.lower()
    if "error" in lower:
        logger.error("Error detected in message!")
        return "error"
    if "warn" in lower:
        logger.warning("Warning detected in message")
        return "warning"

    logger.info("Info message processed")
    return "info"

def process_lines(lines: list[str]) -> dict[str, int]:
    result = {
        "total": 0,
        "info": 0,
        "warning": 0,
        "error": 0,
    }

    for line in lines:
        level = classify_message(line)
        result["total"] += 1
        result[level] += 1

    return result

def process_log_file(path: Path) -> dict[str, int]:
    logger.info(f"Processing file: {path}")

    with path.open(encoding="utf-8") as f:
        lines = f.readlines()

    return process_lines(lines)
