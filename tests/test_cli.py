from pathlib import Path
import subprocess
import sys

def test_cli_runs(tmp_path: Path):
    log_file = tmp_path / "input.log"
    log_file.write_text("hello\nerror happened\n", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "logfp.cli",
            str(log_file),
        ],
        capture_output = True,
        text = True,
    )

    assert result.returncode == 0
    assert "total" in result.stdout
    assert "error" in result.stdout

def test_cli_level_filter(tmp_path: Path):
    log_file = tmp_path / "input.log"
    log_file.write_text("hello\nerror happened\n", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "logfp.cli",
            str(log_file),
            "--level",
            "error",
        ],
        capture_output = True,
        text = True,
    )

    assert result.returncode == 0
    assert "error" in result.stdout
    assert "info" not in result.stdout

def test_cli_json_output(tmp_path: Path):
    log_file = tmp_path / "input.log"
    log_file.write_text("hello\nerror happened\n", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "logfp.cli",
            str(log_file),
            "--json",
        ],
        capture_output = True,
        text = True,
    )

    assert result.returncode == 0
    assert '"error": 1' in result.stdout
