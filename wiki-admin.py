import argparse
import sys
from scripts.replace_text import replace_text
from utils.logger import setup_logger

def main():
    parser = argparse.ArgumentParser(description="MediaWiki API management")
    parser.add_argument("--verbose", action="store_true", help="Print logs")
    parser.add_argument("--no-log", action="store_true", help="Disable logging")

    subparsers = parser.add_subparsers(dest="command")

    replace_parser = subparsers.add_parser("replace", help="Mass text replace")
    replace_parser.add_argument("--old", required=True, help="Text to replace")
    replace_parser.add_argument("--new", required=True, help="New text")
    replace_parser.add_argument("--pages", nargs="+", help="List of pages")

    args = parser.parse_args()

    logger = setup_logger(verbose=args.verbose, disable_logging=args.no_log)

    if args.command == "replace":
        replace_text(args.old, args.new, args.pages)
    elif args.command == None:
        parser.print_help()
    else:
        logger.error(f"Unknown command `{args.command}`! Use --help to get list of all commands")
        sys.exit(1)

if __name__ == "__main__":
    main()
