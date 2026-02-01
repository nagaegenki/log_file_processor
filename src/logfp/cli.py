import argparse
import json
from pathlib import Path

from logfp.processor import process_log_file

def main() -> None:
    parser = argparse.ArgumentParser(
        description = "Process a log file and count message levels"
    )

    parser.add_argument(
        "logfile",
        type = Path,
        help = "Path to log file",
    )

    parser.add_argument(
        "--level",
        choices = ["info", "warning", "error"],
        help = "Filter output to only one level",
    )

    parser.add_argument(
        "--json",
        action = "store_true",
        help = "Output result as JSON",
    )

    parser.add_argument(
        "--output",
        type = Path,
        help = "Write result to file instead of stdout",
    )

    args = parser.parse_args()

    result = process_log_file(args.logfile)

    if args.level:
        result = {
            "total": result["total"],
            args.level: result[args.level]
        }

    if args.json:
        output_text = json.dumps(result, indent=2)
    else:
        lines = ["Result:"]
        for key, value in result.items():
            lines.append(f"  {key}: {value}")
        output_text = "\n".join(lines)
    
    if args.output:
        args.output.write_text(output_text, encoding="utf-8")
    else:
        print(output_text)

if __name__ == "__main__":
    main()
