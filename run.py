from logfp.logger import setup_logging
from logfp.processor import process_log

def main() -> None:
    setup_logging()

    process_log("hello world")
    process_log("this is an error message")

if __name__ == "__main__":
    main()
