from pathlib import Path

import logging
import pytest

from logfp.processor import process_log, process_log_file

def test_info_log(caplog):
    caplog.set_level(logging.INFO)

    process_log("hello world")

    assert "Processing message: hello world" in caplog.text

def test_error_log(caplog):
    caplog.set_level(logging.ERROR)

    process_log("this is an error message")

    assert "Error detected in message!" in caplog.text

def test_warning_on_empty_message(caplog):
    caplog.set_level(logging.WARNING)

    process_log("")

    assert "Empty message received" in caplog.text

def test_none_message_raise_value_error():
    with pytest.raises(ValueError):
        process_log(None)

def test_none_string_message_raise_type_error():
    with pytest.raises(TypeError):
        process_log(123)

def test_process_log_file(tmp_path, caplog):
    caplog.set_level(logging.WARNING)

    log_file = tmp_path / "input.log"
    log_file.write_text("hello\n\nerror happened\n", encoding="utf-8")

    count = process_log_file(log_file)

    assert count == 3
    assert "Empty message received" in caplog.text
    assert "Error detected in message!" in caplog.text

def test_process_log_file_not_found(tmp_path):
    missing = tmp_path / "missing.log"

    with pytest.raises(FileNotFoundError):
        process_log_file(missing)
