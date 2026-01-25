from logfp.processor import process_lines

def test_process_lines_basic():
    lines = [
        "hello",
        "",
        "warn: something",
        "error: happened",
    ]

    result = process_lines(lines)

    assert result["total"] == 4
    assert result["info"] == 1
    assert result["warning"] == 2
    assert result["error"] == 1

def test_process_lines_empty():
    result = process_lines([])
    assert result == {
        "total": 0,
        "info": 0,
        "warning": 0,
        "error": 0,
    }
