import argparse
import sys
from scripts.replace_text import replace_text
from utils.logger import setup_logger

def main():
    global_parser = argparse.ArgumentParser(add_help=False)
    global_parser.add_argument("--verbose", action="store_true", help="Print logs")
    global_parser.add_argument("--no-log", action="store_true", help="Disable logging")

    parser = argparse.ArgumentParser(description="Управление MediaWiki через API", parents=[global_parser])
    subparsers = parser.add_subparsers(dest="command", required=True)

    replace_parser = subparsers.add_parser("replace", help="Массовая замена текста", parents=[global_parser])
    replace_parser.add_argument("--old", required=True, help="Текст для замены")
    replace_parser.add_argument("--new", required=True, help="Новый текст")
    replace_parser.add_argument("--pages", nargs="+", help="Список страниц")

    global_args, remaining_args = global_parser.parse_known_args()

    global logger
    logger = setup_logger(verbose=global_args.verbose, disable_logging=global_args.no_log)

    args = parser.parse_args()

    if args.command == "replace":
        replace_text(args.old, args.new, args.pages)
    elif args.command == None:
        parser.print_help()
    else:
        logger.error(f"Unknown command `{args.command}`! Use --help to get list of all commands")
        sys.exit(1)

if __name__ == "__main__":
    main()
